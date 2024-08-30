from config import app
from models import db, Guide, Plant, User, National_Park, Plant_Guide_Join, Plant_NP_Join

with app.app_context():

    # Delete all data in tables to start from scratch
    print("Deleting data...")
    db.session.query(Plant).delete()
    db.session.query(National_Park).delete()
    db.session.query(Guide).delete()
    # db.session.query(User).delete()
    db.session.commit()


    print("creating plants!")
    plant1 = Plant(name= "Alfalfa", type= "edible", img_1="https://michelleandvitaadventures.wordpress.com/wp-content/uploads/2013/06/alfalfa.jpg?w=2000&h=", description="The seeds of alfalfa can not only be sprouted, but also roasted or made into flour. The flowers, leaves, and young shoots can also be eaten, but I have to say I am most excited about sprouting the seeds." )
    plant2 = Plant(name= "Yarrow", type= "medicinal", subtype="hemostatic", img_1="https://michelleandvitaadventures.wordpress.com/wp-content/uploads/2013/06/yarrow.jpg?w=2000&h=", description=" Along with its styptic qualities, it is also anti-inflammatory, slightly antimicrobial and antibacterial, and can induce sweating (which can be very helpful in bringing down a fever or helping the body sweat out toxins). Use as tea, tincture, or poultice." )

    print("creating parks!")
    nationalpark1 = National_Park(name= 'Yosemite', state ="CA")
    nationalpark2 = National_Park(name= 'Rocky Mountain', state = 'CO')
    
    print("creating users!")
    user1 = User(email='nancyleebechtold@gmail.com', password_hash= 'meow123')
    user2 = User(email='annbechtold0883@gmail.com', password_hash= 'woof123')

    print("creating guides!")
    guide1 = Guide(title='trip to yosemite')
    guide2 = Guide(title= 'trip to rocky mountain')
    
    plants = [plant1, plant2]
    parks =[nationalpark1, nationalpark2]
    users= [user1,user2]
    guides = [guide1,guide2]
    
    db.session.add_all(plants)
    db.session.add_all(parks)
    db.session.add_all(users)
    db.session.add_all(guides)
    
    db.session.commit()
    
    print("creating join table entries!")
    # Create join table entries
    plant_guide_join1 = Plant_Guide_Join(plant_id=plant1.id, guide_id=guide1.id)
    plant_guide_join2 = Plant_Guide_Join(plant_id=plant2.id, guide_id=guide2.id)

    plant_np_join1 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark2.id)

    join_entries = [plant_guide_join1, plant_guide_join2, plant_np_join1, plant_np_join2]
    
    db.session.add_all(join_entries)
    db.session.commit()
    