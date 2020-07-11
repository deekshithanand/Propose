from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True,

    )
    username = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        unique=True,
        nullable=False

    )
    password = db.Column(
        db.String(200),
        nullable=False
    )

    def __repr__(self):
        return f'<User{self.username}>'


class Topic(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(200),
        nullable=False,
        unique = True
    )
    description = db.Column(
        db.String(200),
    )
    def __repr__(self):
        return f'<Topic{self.name}>'
    
    post = db.relationship('Post',backref= 'topic')


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(200),unique = True,nullable = False)
    description = db.Column(db.String(600),nullable = False) #user has to put something into the description
    def __repr__(self):
        return f'<Post{self.id}>'
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))

# class Person(db.Model):
#     __tablename__ = 'person'
#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#     )

#     name = db.Column(
#         db.String(20),
#     )
#     pets = db.relationship('Pets', backref='owner', passive_deletes=True)


# class Pets(db.Model):
#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#     )
#     name = db.Column(
#         db.String(100),
#         nullable=False
#     )
#     p_id = db.Column(
#         db.Integer,
#         db.ForeignKey('person.id', ondelete='CASCADE')
#     )
