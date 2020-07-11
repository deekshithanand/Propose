from flask import Blueprint, url_for, request, redirect, render_template,flash
from src.models import Topic, Post
from werkzeug.exceptions import NotFound, InternalServerError
from .forms import PostForm
from src import db

post_bp = Blueprint('post_bp', __name__, template_folder='templates')


# TODO:
# CRUD OPS for posts within topic.


@post_bp.route("/topic/<int:topic_id>/")
@post_bp.route("/topic/<int:topic_id>/posts/")
def get_posts(topic_id):
    # return existing posts
    # check if topic_id exists:
    id = Topic.query.with_entities(Topic.id).filter(Topic.id == topic_id).first()
    if id:
        posts = Post.query.filter(Post.topic_id == topic_id).all()
        return render_template("posts.html", posts=posts)
    else:
        raise NotFound


@post_bp.route("/topic/<int:topic_id>/edit_post/<int:post_id>/", methods=['GET', 'POST'])
def edit_post(post_id, topic_id):
    # edit post if there else not found
    if request.method == 'GET':
        # send in the form
        return "Edit post"

    if request.method == 'POST':
        # update post.
        return redirect(url_for('post_bp.get_posts'))


# create post
@post_bp.route("/topic/<int:topic_id>/create_post/", methods=['GET', 'POST'])
def create_post(topic_id):
    if request.method == 'GET':
        form = PostForm()
        return render_template('create_post.html',form= form,id = topic_id)

    if request.method == 'POST':
        #create topic
        formData = PostForm(request.form)
        if formData.validate(): #for csrf token validation
            new_post = Post(name = formData.name.data,description = formData.description.data,topic_id = topic_id)
            try:
                db.session.add(new_post)
                db.session.flush()
                db.session.commit()
                return redirect(url_for('post_bp.get_posts',topic_id=topic_id))
            except :
                raise InternalServerError
        else:
            flash("Form validation error!",'danger')
            return render_template('create_post.html',form = formData,id = topic_id)
        

# # delete post entry


# @post_bp.route("/topic/<int:topic_id>/delete_post/<int:post_id>/", method=['GET', 'POST'])
# def delete_post(post_id, topic_id):
#     if request.method == 'GET':
#         return "DEL POST"
#     if request.method == 'POST':
#         return 'POST DELETED'


