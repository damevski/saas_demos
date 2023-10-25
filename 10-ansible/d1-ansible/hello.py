import os
from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPDigestAuth

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

db = SQLAlchemy(app)

class ValidationError(ValueError):
    pass

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        json_post = {
            'username': self.username,
        }
        return json_post

    def from_json(json_post):
        username = json_post.get('username')
        if username is None or username == '':
            raise ValidationError('user does not have a name')
        return User(username=username)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'Page Is Not Here'}), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message':'Something is Broke'}), 500


@app.route('/users', methods=['GET'])
@auth.login_required
def index():
   users = User.query.all()
   return jsonify({
        'users': [user.to_json() for user in users]
   }) 


@app.route('/user', methods=['POST'])
@auth.login_required
def user_post():
    user = User.from_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201    


@app.route('/user/<username>', methods=['GET'])
@auth.login_required
def user_get(username):
    if username is None or username == '':
        raise ValidationError('user does not have a name')
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
