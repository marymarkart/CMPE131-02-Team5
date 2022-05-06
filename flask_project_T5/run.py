from project import app


if __name__ == '__main__':
    from project import db
    db.create_all()
    app.run(debug=True)
