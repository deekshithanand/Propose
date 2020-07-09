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
