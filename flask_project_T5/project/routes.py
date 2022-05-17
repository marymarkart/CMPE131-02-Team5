from email.mime import image
import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from project import app, db, bcrypt
from project.forms import (RegistrationForm, LoginForm, UpdateAccountForm, PostForm, SearchForm)
from project.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/cart")
@login_required
def cart():
    return render_template('cart.html', title='Cart')


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

@app.route("/post/<int:post_id>/add-to-cart", methods=['POST'])
@login_required
def add_cart(post_id):


    flash('Added Item to Cart!', 'success')
    return render_template('cart.html')


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('user_posts.html', posts=posts, user=user, image_file=image_file)