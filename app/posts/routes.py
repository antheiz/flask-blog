import imp
from flask import (render_template, redirect, 
                  request, url_for, flash, 
                  abort, Blueprint)
from flask_login import login_required, current_user
from app import db
from app.models import Post
from app.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['get','post'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        posts = Post(title=form.title.data, content=form.content.data, author=current_user )
        db.session.add(posts)
        db.session.commit()        
        flash('Postingan berhasil diupload','success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', form=form, judul='New Post', legend='Create Postingan')


@posts.route('/post/<int:post_id>')
def postingan(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('postingan.html', judul=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
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
        return redirect(url_for('main.index'))
    else:
        form.title.data = post.title
        form.content.data = post.content    
    return render_template('create_post.html', form=form, judul=post.title, post=post, legend='Update Postingan')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Postingan berhasil dihapus','success')
    return redirect(url_for('main.index'))
