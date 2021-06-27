from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
import uuid
import pam


p = pam.pam()

class User(object):
    def __init__(self, username):
        self.id = str(uuid.uuid4())
        self.username = username

    def __str__(self):
        return "User(id='%s')" % self.id

users = {}

def authenticate(username, password):
    result = p.authenticate(username, password)
    if result:
        user = User(username)
        users[username] = user
        return user

    return None

def identity(payload):
    user_id = payload['identity']
    for _, user in users.items():
        if user.id == user_id:
            return user

    return None

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity


if __name__ == '__main__':
    app.run()
