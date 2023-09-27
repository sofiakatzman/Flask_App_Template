from flask_restful import Resource
from models.models import User
from config import api, db, request, make_response, abort, session

class Login(Resource):
    def post(self):
        try:
            request_json = request.get_json()
            username = request_json['username']
            password = request_json['password']
            user = User.query.filter_by(username=username).first()
            
            if user and user.authenticate(password):
                session['user_id'] = user.id
                response = make_response(user.to_dict(), 200)
                return response
            else:
                abort(401, "Incorrect username or password")
        except:
            abort(401, "Incorrect username or password")

api.add_resource(Login, '/api/login')

class Signup(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {'error': 'Username already exists'}, 409
        birthday = request_json.get('birthday')
        
        user = User(
            username=username,
            birthday=birthday
        )
        user.password_hash = request_json['password']

        try:
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return make_response(user.to_dict(), 201)
        except:
            return {'error': '422 Unprocessable Entity'}, 422

api.add_resource(Signup, '/api/signup')

class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            response = make_response(
                user.to_dict(),
                200
            )
            return response
        except:
            abort(401, "Unauthorized")

api.add_resource(AuthorizedSession, '/api/authorized')

class Logout(Resource):
    def delete(self):
        session['user_id']=None 
        response = make_response('', 204)
        return response     
    
api.add_resource(Logout, '/api/logout')