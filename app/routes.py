import os
import secrets
from PIL import Image
from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request, abort
from .forms import LoginForm, RegisterForm, AccountForm, PostForm
from .models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET','POST'])
def index():
    # posts = Post.query.all()
    page = request.args.get('page', type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template ('index.html',judul='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', judul='About')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        flash('Akun berhasil dibuat, silakan', 'success')
        return redirect(url_for('register'))
    return render_template ('register.html', form=form ,judul='Register')


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('gagal login, silakan coba lagi.','danger')
    return render_template ('login.html', form=form, judul='Login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


#for image settings 
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)
    # form_picture.save(picture_path)

    output_size = (225,225)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/account', methods=['get','post'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data     
        db.session.commit()
        flash('profil berhasil diupdate','success')
        return redirect(url_for('account'))
    else:
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('account.html', image_file=image_file, form=form, judul='Account')


@app.route('/post/new', methods=['get','post'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        posts = Post(title=form.title.data, content=form.content.data, author=current_user )
        db.session.add(posts)
        db.session.commit()        
        flash('Postingan berhasil diupload','success')
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form, judul='New Post', legend='Create Postingan')


@app.route('/post/<int:post_id>')
def postingan(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('postingan.html', judul=post.title, post=post)


@app.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data 
        post.content = form.content.data    
        db.session.commit()
        flash('Postingan anda berhasil diupdate','success')
        return redirect(url_for('index'))
    else:
        form.title.data = post.title
        form.content.data = post.content    
    return render_template('create_post.html', form=form, judul=post.title, post=post, legend='Update Postingan')


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Postingan berhasil dihapus','success')
    return redirect(url_for('index'))

# @app.route('/user/<string:username>')
# def user_post():
#     page = request.args.get('page', type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
#     return render_template ('user_post.html',judul='User', posts=posts, user=user)
@app.route("/user/<string:username>")
def user_post(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_post.html', judul=user.username, posts=posts, user=user)