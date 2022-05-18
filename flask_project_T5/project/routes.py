from email.mime import image
from genericpath import exists
import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from project import app, db, bcrypt
from project.forms import (RegistrationForm, LoginForm, UpdateAccountForm, PostForm, SearchForm)
from project.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import stripe

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/posts")
def posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('posts.html', posts=posts)

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route('/search', methods=["GET","POST"])
def search():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    search_posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    posts = Post.query
    if form.validate_on_submit():
        post.searched = form.searched.data
        posts = posts.filter(Post.content.like('%' + post.searched + '%'))
        posts = posts.order_by(Post.title).all()
        return render_template("search.html", form=form, searched=post.searched, posts=posts, search_posts=search_posts)
    return render_template("search.html")


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return render_template('home.html')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Signup', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('home.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else render_template('home.html')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return render_template('home.html')


def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    i = Image.open(form_picture)
    i.save(picture_path)

    return picture_fn

def save_item_picture(form_item_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_item_image.filename)
    item_image_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/item_pics', item_image_fn)

    i = Image.open(form_item_image)
    i.save(picture_path)

    return item_image_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_profile_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/account/<int:user_id>/delete", methods=['GET','POST'])
def delete_account(user_id):
        try:
            logout_user()
            account = User.query.get_or_404(user_id)
            while True:
                post = Post.query.filter_by(user_id=user_id).first()
                if post:
                    db.session.delete(post)
                    db.session.commit()
                else:
                    break
            db.session.delete(account)
            db.session.commit()
        except:
           abort(404)
        flash('Your account has been deleted!', 'success')
        return render_template('home.html')


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.item_image.data:
            image_file = save_item_picture(form.item_image.data)
            db.session.commit()
            post = Post(title=form.title.data, content=form.content.data, item_price=form.item_price.data, author=current_user, item_image=image_file)
        else:
            post = Post(title=form.title.data, content=form.content.data, item_price=form.item_price.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return render_template('home.html')
    return render_template('create_post.html', title='New Post',
                             form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.item_image.data:
            image_file = save_item_picture(form.item_image.data)
            post.item_image = image_file
        post.title = form.title.data
        post.content = form.content.data
        post.item_price = form.item_price.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.item_price.data = post.item_price
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return render_template('home.html')

cart_items = []
item_posts = []
@app.route("/post/<int:post_id>/add-to-cart", methods=['POST'])
@login_required
def add_cart(post_id):
    cart_items.append(post_id)
    for i in cart_items:
        post = Post.query.get_or_404(i)
        item_posts.append(post)
    cart_items.clear()
    flash('Added Item to Cart!', 'success')
    return render_template('cart.html', cart=item_posts)

@app.route("/cart")
@login_required
def cart():
    return render_template('cart.html', cart=item_posts)

@app.route("/cart/delete/<int:post_id>", methods=['GET','POST'])
@login_required
def delete_cart_item(post_id):
    for i in item_posts:
        if i.id == post_id:
            item_posts.remove(i)
    return render_template('cart.html', cart=item_posts)


app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51KzDsRGP6AuS3BWDr9gBCQZ9Blv0eE9hEbhS0RiY6OyDu7Z1MCvYIFNX4oM9YPat8lmNOsXVsRZYB2LYMy9SJfGg00SoiNXlHN'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51KzDsRGP6AuS3BWDpzvoLfbWZ6sBDqxbQhrZutddiiYkCHFcVPEZ3jQLjTrNnNbMAJn5H3qRYGd7WlTwlkHu6wl500sNhDnpZH'
stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route("/checkout")
@login_required
def checkout():
    full_price = 0
    for i in item_posts:
        full_price = i.item_price + full_price
    return render_template('checkout.html', full_price=full_price)

@app.route('/stripe_pay')
@login_required
def stripe_pay():
    full_price = 0
    for i in item_posts:
        full_price = i.item_price + full_price
        session_price = full_price * 100
        checkout_price = int(session_price)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': checkout_price,
                'product_data': {
                    'name': 'Your Total Is',
                    'description': 'Have A Great Day!',
                    },
            },
            'adjustable_quantity': {
                'enabled': True,
                'minimum': 1,
                'maximum': 10,
                },
            'quantity' : 1,
            }],
        mode='payment',
        success_url=url_for('thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=url_for('checkout', _external=True),
    )
    return {
        'checkout_session_id': session['id'],
        'checkout_public_key': app.config['STRIPE_PUBLIC_KEY']
    }

@app.route('/thanks')
@login_required
def thanks():
    return render_template('thanks.html')

@app.route('/stripe_webhook', methods=['POST'])
@login_required
def stripe_webhook():
    print('WEBHOOK CALLED')

    if request.content_length > 1024 * 1024:
        print('REQUEST TOO BIG')
        abort(400)
    payload = request.get_data()
    sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = 'whsec_c6ada773f8b6ca0ff6a062047aa205496db85ed1f70edc2c2762a1208e562948'
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print('INVALID PAYLOAD')
        return {}, 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('INVALID SIGNATURE')
        return {}, 400

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items['data'][0]['description'])

    return {}


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('user_posts.html', posts=posts, user=user, image_file=image_file)
