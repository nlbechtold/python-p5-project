#!/usr/bin/env python3

from flask import Flask, request, session, jsonify
from flask_restful import Resource
from models import Plant, Guide, National_Park, User, Plant_Guide_Join, Plant_NP_Join
from config import app, db, api



# @app.before_request
# def check_credentials():
#     valid_routes = ("/checksessions","/login", "/users")
#     print('youre in method')
#     if request.path not in valid_routes and 'user_id' not in session:
#         return {"error": "please login"},401
#     else:
#         print(session)
#         pass

class UserGuides(Resource):
    def get(self, user_id):
        print(session)
        user_id = session.get('user_id')    
        if user_id:
            user = User.query.get(user_id)  # Query the User object
            if user:
                guides = user.guides
                return [guide.to_dict() for guide in guides], 200
            else:
                return {"error": "User not found"}, 404
        else:
            return {"error": "User not logged in"}, 401
        
    def post(self,user_id):
        print(session)
        try:
            user_id = session.get('user_id')
            if not user_id:
                return {"error": "User not logged in"}, 401
            data = request.get_json()
            g = Guide(
                title=data["title"],
                description=data["description"],
                user_id= user_id 
            )
            db.session.add(g)
            db.session.commit()
            return g.to_dict(), 201
        except Exception as e:
            print(e)
            return {"error": "Not valid guide"}, 400

api.add_resource(UserGuides, '/user/<int:user_id>/guides')

class Users(Resource):
    def get(self):
        au = User.query.all()
        return [user.to_dict() for user in au]

    def post(self):
        print("Here")
        try:
            data = request.get_json()
            u = User(
                email=data["email"],
                password_hash=data["password"],
            )
            # u._password_hash= data["password"]
            db.session.add(u)
            db.session.commit()
            return u.to_dict(), 201
        except Exception as e:
            print(e)
            print("Here")
            return {"error": "Not valid user"}, 400

api.add_resource(Users, '/users')

# YAAY this WORKS below
class OneNationalPark(Resource):
    def get(self, national_park_id):  
        np = National_Park.query.filter(National_Park.id == national_park_id).first()
        if np:
            return np.to_dict()
        else:
            return {
                "error": "not valid id"
            }, 400


api.add_resource(OneNationalPark, '/national_park/<int:national_park_id>')

# YAAAY full CRUD for guide works
class OneGuide(Resource):
    def get(self, guide_id): 
        guide = Guide.query.filter(Guide.id == guide_id).first()  
        if guide:
            return guide.to_dict()
        else:
            return {
                "error": "not valid id"
            }, 400

    def post(self):  # New POST method
        try:
           
            data = request.get_json()
            
            # Create a new Guide instance
            new_guide = Guide(
                title=data.get('title'),
                description=data.get('description'),
                user_id=data.get('user_id') 
            )
            
      
            db.session.add(new_guide)
            db.session.commit()
            
         
            return new_guide.to_dict(), 201
        
        except Exception as e:
            print(e)
            return {
                "error": "Failed to create guide"
            }, 400

    def patch(self, guide_id):  
        guide = Guide.query.filter(Guide.id == guide_id).first()  
        if guide:
            try:
                data = request.get_json()
                for key in data:
                    setattr(guide, key, data[key])
                db.session.add(guide)
                db.session.commit()
                return guide.to_dict()
            except Exception as e:
                print(guide)
                return {
                    "error": "validation error"
                }, 400
        else:
            return {
                "error": "not valid id"
            }, 400

    def delete(self, guide_id): 
        guide = Guide.query.get(guide_id)
        if not guide:
            return {"error": "Guide not found"}, 404

        try:
            db.session.delete(guide)
            db.session.commit()
            return {"message": "guide deleted"}, 200
        except Exception as e:
            db.session.rollback()
            print(e)
            return {"error": "Failed to delete guide"}, 500


api.add_resource(OneGuide, '/guide', '/guide/<int:guide_id>')


class AddPlantsToGuide(Resource):
    def post(self):
        """
        Adds multiple plants to a specific guide based on provided guide ID and plant IDs.
        Expected JSON input: { "guide_id": <guide_id>, "plant_ids": [<plant_id1>, <plant_id2>, ...] }
        """
        data = request.get_json()
        
   
        guide_id = data.get('guide_id')
        plant_ids = data.get('plant_ids', [])

        if not guide_id:
            return {"error": "Guide ID is required"}, 400
        
        if not plant_ids:
            return {"error": "List of plant IDs is required"}, 400

        # Fetch the guide to ensure it exists
        guide = Guide.query.get(guide_id)
        if not guide:
            return {"error": "Guide not found"}, 404

        # Fetch all plants to ensure they exist
        plants = Plant.query.filter(Plant.id.in_(plant_ids)).all()
        if len(plants) != len(plant_ids):
            return {"error": " plant IDs are invalid or not found"}, 404

        try:
            # Add each plant to the guide
            for plant in plants:
                plant_guide_join = Plant_Guide_Join(plant_id=plant.id, guide_id=guide.id)
                db.session.add(plant_guide_join)
            
            # Commit the session
            db.session.commit()
            return {"message": "Plants added to guide successfully"}, 201
        
        except Exception as e:
            db.session.rollback()
            print(e)
            return {"error": "Failed to add plants to guide"}, 500

api.add_resource(AddPlantsToGuide, '/add_plants_to_guide')

# YAAYY this WOrks
class All_Plants(Resource):
    def get(self):
        plants = Plant.query.all()
        return [plant.to_dict() for plant in plants], 200
    
api.add_resource(All_Plants,'/plants')


class Login(Resource):
    def post(self):
        data = request.get_json()
        print("Login data received:", data)
        user = User.query.filter(User.email == data['email']).first()
        print("User found:", user)
        if user and user.authenticate(data['password']):
            session['stay_logged_in'] = data.get('stayLoggedIn', False)
            session['user_id'] = user.id 
            print("User authenticated, session created:", session)
            return jsonify(user.to_dict()) 
        else:
            print("Authentication failed.")
            return jsonify({"Error": "Invalid email or password"}), 400
        
api.add_resource(Login, '/login')


class Logout(Resource):
    def delete(self):
        session.clear()
        return {}
api.add_resource(Logout,'/logout')

class SaveSession(Resource):
    def get(self):
        print(session)
        return {}
    
    def post(self):
        print(session)
        data = request.get_json()
        session['data'] = data['data']
        print(data)
        return {}

api.add_resource(SaveSession,'/session')

# checks back end to see if saved a session
class CheckSession(Resource):
    def get(self):
        print(session)
        if session.get('stay_logged_in') == True:
            user = User.query.filter(User.id == session.get('user_id')).first()
            return user.to_dict()
        else:
            return {}, 404
        
api.add_resource(CheckSession,'/checksessions')



if __name__ == '__main__':
    app.run(port=5555, debug=True)


