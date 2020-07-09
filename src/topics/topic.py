from flask import Blueprint,render_template,request,redirect,url_for,Response,flash
from src.models import Topic
from .forms import TopicForm
from src import db
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import InternalServerError,NotFound
#blueprint
topics_bp = Blueprint('topic',__name__,template_folder='templates')
#TODO:
#create topic
#delete topic
#retrive topics

@topics_bp.route('/')
def topics():
    #get all the topics that are registered
    topics = Topic.query.all()
    #gotta implement pagination  
    return render_template('topic.html',topics = topics)


@topics_bp.route('/create_topic/',methods =['GET','POST'] )
def create_topic():
    if request.method == 'GET':
        #send the form for create topic!
        formData = TopicForm()
        return render_template('create-topic.html',form = formData)
    if request.method == 'POST':
        # check the post method and redirect
        formData = TopicForm(request.form)
        if formData.validate():
            # data base operations
            new_topic = Topic(name = formData.topic_name.data,
            description = formData.topic_name.data)
            try:
                db.session.add(new_topic)
                db.session.flush()
                db.session.commit()
                flash(" New Topic Added Successfully!",'success')
                return redirect(url_for('topic.topics'))
            except :
                db.session.rollback()
                flash("Topic Already Exists!",'warning')
                # raise InternalServerError
                return render_template('create-topic.html',form = formData), 409 #code for record exists
                
        

@topics_bp.route('/edit_topic/<int:topic_id>/',methods = ['GET','POST'])
def edit_topic(topic_id):
    if request.method == 'GET':
        ## form with existing data 
        topic = Topic.query.filter(Topic.id == topic_id).first()
        if topic:
            formData = TopicForm()
            formData.topic_name.data = topic.name
            formData.topic_description.data = topic.description
            return render_template('edit-form.html',form = formData,id = topic_id)
        else:
            raise NotFound

        ##handle update request
    if request.method == 'POST':
        ## save edits and redirect
        formData = TopicForm(request.form)
        if formData.validate():
            #later add this to g variable and test it:
            topic = Topic.query.filter(Topic.id == topic_id).first()
            topic.name = formData.topic_name.data
            topic.description = formData.topic_description.data
            try:
                db.session.flush()
                db.session.commit()
                flash("Topic Updated Successfully!",'success')
                return redirect(url_for('topic.topics'))
            except IntegrityError:
                db.session.rollback()
                flash("Topic by that name already exists! Please keep topic name Unique",'danger')
                return render_template('edit-form.html',form = formData,id = topic_id)

@topics_bp.route('/delete_topic/<int:topic_id>/',methods =['GET','POST'])
def delete_topic(topic_id):
    if request.method == 'GET':
        ## show confirmation page
        topic = Topic.query.filter(Topic.id == topic_id).first()
        if topic:
            formData = TopicForm()
            formData.topic_name.data = topic.name
            return render_template('delete-topic.html',form = formData,id=topic_id)
        else:
            raise NotFound
    if request.method == 'POST':
        ## delete and redirect
        topic = Topic.query.filter(Topic.id == topic_id).first()
        if topic:
            try:
                db.session.delete(topic)
                db.session.flush()
                db.session.commit()
                flash("Deleted Successfully!",'success')
                return redirect(url_for('topic.topics'))
            except:
                raise InternalServerError
        else:
            raise NotFound
