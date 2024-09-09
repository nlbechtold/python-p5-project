from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class Plant_Guide_Join(db.Model, SerializerMixin):
    __tablename__ = 'plants_guides_join'
    id = db.Column(db.Integer, primary_key=True)
    guide_id= db.Column(db.Integer, db.ForeignKey('guides.id'))
    plant_id= db.Column(db.Integer, db.ForeignKey('plants.id'))

class Plant_NP_Join(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'plants_nps_join'
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    national_park_id = db.Column(db.Integer, db.ForeignKey('national_parks.id'))
    

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    guides = db.relationship('Guide', back_populates='user', cascade="all, delete-orphan")
    
    serialize_rules = ('-guides.user','-_password_hash')
    
    @validates('email')
    def validate_image(self, key, email):
        if "@" in email:
            return email
        else:
            raise ValueError('invalid email')
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))
    
class Guide(db.Model, SerializerMixin):
    __tablename__ = 'guides'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False) 
    description = db.Column(db.String, nullable=False)
    

    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='guides')
    
    plants = db.relationship('Plant', secondary='plants_guides_join', back_populates='guides')

    serialize_rules = ('-user.guides', '-plants.guides',)
    



class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    subtype = db.Column(db.String)
    description = db.Column(db.String, nullable=False)

    guides = db.relationship('Guide', secondary='plants_guides_join', back_populates='plants')
    national_parks = db.relationship('National_Park', secondary='plants_nps_join', back_populates='plants')

    serialize_rules = ('-guides','-national_parks.id')    
    
    @validates('img_1')
    def validate_image(self, key, img_1):
        if "http" in img_1:
            return img_1
        else:
            raise ValueError('Image must be a valid URL')
        
    @validates('description')
    def validate_description(self, key, description):
        if 10 <= len(description) <= 300:
            return description
        else:
            raise ValueError('Description must be between 10 and 300 characters')
    @validates('name')
    def validate_description(self, key, name):
        if 5 <= len(name) <= 30:
            return name
        else:
            raise ValueError('Description must be between 5 and 30 characters')
        

    
class National_Park(db.Model, SerializerMixin):
    __tablename__ = 'national_parks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    
    plants = db.relationship('Plant', secondary='plants_nps_join', back_populates='national_parks')
    
    serialize_rules = ('-plants.national_parks',)
    
    @validates('name')
    def validate_description(self, key, name):
        if 5 <= len(name) <= 30:
            return name
        else:
            raise ValueError('Description must be between 5 and 30 characters')
        
