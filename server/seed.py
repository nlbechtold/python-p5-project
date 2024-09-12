from app import app  # Import from app.py, not config.py
from config import db
from models import db, Guide, Plant, User, National_Park, Plant_Guide_Join, Plant_NP_Join

with app.app_context():

    # Delete all data in tables to start from scratch
    print("Deleting data...")
    db.session.query(Plant).delete()
    db.session.query(National_Park).delete()
    db.session.query(Guide).delete()
    db.session.query(User).delete()
    db.session.commit()



print("creating plants!")

plants =[
{"name": "Blueberry", "type": "edible", "img": "https://cdn.britannica.com/90/9490-050-F5B059F5/Blueberries.jpg", "description": "Blueberries ripen from July to September. Eat them fresh, or use them in pies and jams. They are also high in antioxidants and vitamin C."},
{"name": "Wintergreen", "type": "medicinal", "img": "https://cdn.britannica.com/94/189494-050-F1C6B0C9/Wintergreen-berries.jpg", "description": "The leaves and berries can be chewed or brewed into tea. The tea was traditionally used for headaches, colds, and as a pain reliever."},
{"name": "Dandelion", "type": "edible", "img": "https://cdn.britannica.com/27/1927-050-33CD1597/Dandelion.jpg", "description": "All parts of the dandelion are edible. The leaves can be used in salads, and the roots can be dried and roasted to make a coffee substitute."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow leaves and flowers can be made into a tea to relieve colds, fevers, and improve digestion."},
{"name": "Birch", "type": "medicinal", "img": "https://cdn.britannica.com/46/75646-050-A946A602/Birch.jpg", "description": "The bark can be boiled to make a tea, used to treat fevers and headaches. The sap can be consumed as an early spring tonic."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams and desserts. Raspberry leaves can also be brewed into tea for menstrual pain relief."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "Blooms from March to July. The boiled stems have been used to make tea, which works as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling. Can be eaten raw or made into jams and jellies. The pads (nopales) can be cooked and eaten as well."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit of the yucca plant are edible. They can be eaten raw or cooked, and are often used in stews."},
{"name": "Desert Sage", "type": "medicinal", "img": "https://cdn.britannica.com/28/186528-050-F78E9E9F/Desert-sage.jpg", "description": "The leaves of desert sage can be brewed into a tea, used to treat colds, fevers, and sore throats."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave plant can be roasted for food or fermented into an alcoholic beverage. The sap can be used for sweeteners."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "The flower buds of the cholla cactus are edible after boiling. The fruits can also be eaten after being peeled."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling. Can be eaten raw or made into jams and jellies. The pads (nopales) can be cooked and eaten as well."},
{"name": "Wild Onion", "type": "edible", "img": "https://cdn.britannica.com/77/184177-050-B9C0B984/Wild-onions.jpg", "description": "The bulbs of wild onions are edible and can be used similarly to domesticated onions, added to stews or eaten raw."},
{"name": "Buffalo Berry", "type": "edible", "img": "https://cdn.britannica.com/86/202786-050-CDAAB979/Buffalo-berry.jpg", "description": "The berries can be eaten fresh or dried and used in jams or sauces. They are a good source of vitamin C."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea, which is good for boosting the immune system."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be used to make tea, which is good for colds, stomach issues, and as an antiseptic."},
{"name": "Bitterroot", "type": "edible", "img": "https://cdn.britannica.com/67/176767-050-18DF9CC0/Bitterroot-flower.jpg", "description": "The roots are edible and can be boiled or dried. Traditionally used by Native Americans as a food source."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "Boiled stems have been used to make a tea, which acts as a decongestant and energy booster."},
{"name": "Sotol", "type": "edible", "img": "https://cdn.britannica.com/87/178787-050-1CDA7F5F/Sotol-leaves.jpg", "description": "The heart of the plant can be roasted or ground into flour. It's also used to make an alcoholic beverage."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour for baking or made into syrup. It was traditionally used by Native Americans for sustenance."},
{"name": "Ocotillo", "type": "medicinal", "img": "https://cdn.britannica.com/15/211815-050-3A72638C/Ocotillo-flowers.jpg", "description": "Ocotillo flowers can be brewed into tea, which was traditionally used to treat coughs and inflammation."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave plant can be roasted for food or fermented into an alcoholic beverage. The sap can be used for sweeteners."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots have been used traditionally as a soap."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "Leaves are used in a tea to treat colds, coughs, and skin infections. The resin was used as an antiseptic and healing salve."},
{"name": "Sea Grape", "type": "edible", "img": "https://cdn.britannica.com/34/173434-050-9C3F3F1D/Sea-grape.jpg", "description": "The fruit can be eaten raw or used to make jelly or wine. It ripens in late summer and is sweet when fully ripe."},
{"name": "Mangrove", "type": "medicinal", "img": "https://cdn.britannica.com/82/196282-050-863DDF8D/Mangroves.jpg", "description": "Mangrove bark can be boiled to make a tea traditionally used to treat wounds and diarrhea."},
{"name": "Coconut Palm", "type": "edible", "img": "https://cdn.britannica.com/70/183370-050-95A73308/Coconut-palm.jpg", "description": "Coconut fruit can be eaten raw, and the water is a natural electrolyte drink. The oil is used for cooking or skin care."},
{"name": "Saw Palmetto", "type": "medicinal", "img": "https://cdn.britannica.com/28/164228-050-3D01F9F2/Saw-palmetto-fruit.jpg", "description": "The berries are used to make a tea or extract that is traditionally used for prostate health."},
{"name": "Papaya", "type": "edible", "img": "https://cdn.britannica.com/30/217730-050-C8F67012/Papaya-fruits.jpg", "description": "The fruit is edible and can be eaten raw or used in salads. The seeds have been used traditionally as an anti-parasitic remedy."},
{"name": "Spanish Moss", "type": "medicinal", "img": "https://cdn.britannica.com/49/165249-050-FCEC2B3E/Spanish-moss.jpg", "description": "Traditionally used as an anti-inflammatory and for wound healing. The fibers have been used as bandages."},
{"name": "Buttonwood", "type": "medicinal", "img": "https://cdn.britannica.com/56/181956-050-56A4C6A9/Buttonwood-tree.jpg", "description": "Buttonwood bark can be boiled to create a tea used for digestive issues and fever reduction."},
{"name": "Juniper", "type": "medicinal", "img": "https://cdn.britannica.com/34/9234-050-D6F3AD36/Juniper.jpg", "description": "Juniper berries are used to make tea that is traditionally used for treating colds, urinary infections, and as a digestive aid."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be used to make tea, which is good for colds, stomach issues, and as an antiseptic."},
{"name": "Pinyon Pine", "type": "edible", "img": "https://cdn.britannica.com/81/139081-050-6615904F/Pinyon-pine-cones.jpg", "description": "Pinyon nuts are edible and highly nutritious. They can be eaten raw or roasted."},
{"name": "Chokecherry", "type": "edible", "img": "https://cdn.britannica.com/46/196746-050-4BCE5E1B/Chokecherry-fruit.jpg", "description": "Chokecherry fruit can be eaten raw or made into jams and syrups. It is also used to make wine."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea, which boosts the immune system."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow leaves and flowers can be made into a tea to relieve colds, fevers, and improve digestion."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems have been used to make tea, which acts as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling. Can be eaten raw or made into jams and jellies."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit of the yucca plant are edible. They can be eaten raw or cooked and are often used in stews."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush can be brewed into a tea to treat colds, indigestion, and used as an antiseptic."},
{"name": "Juniper", "type": "medicinal", "img": "https://cdn.britannica.com/34/9234-050-D6F3AD36/Juniper.jpg", "description": "Juniper berries are used to make tea traditionally used for treating urinary infections and digestive issues."},
{"name": "Pinyon Pine", "type": "edible", "img": "https://cdn.britannica.com/81/139081-050-6615904F/Pinyon-pine-cones.jpg", "description": "Pinyon nuts are edible and nutritious. They can be eaten raw or roasted."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems have been used to make a tea, which works as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling. Can be eaten raw or made into jams and jellies."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots have been used traditionally as soap."},
{"name": "Desert Sage", "type": "medicinal", "img": "https://cdn.britannica.com/28/186528-050-F78E9E9F/Desert-sage.jpg", "description": "The leaves of desert sage can be brewed into tea used to treat colds, fevers, and sore throats."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "Cholla cactus flower buds are edible after boiling, and the fruits can be peeled and eaten."},
{"name": "Pinyon Pine", "type": "edible", "img": "https://cdn.britannica.com/81/139081-050-6615904F/Pinyon-pine-cones.jpg", "description": "Pinyon nuts are edible and highly nutritious. They can be eaten raw or roasted."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "Boiled stems are used to make tea, which acts as a decongestant and energy booster."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots were used traditionally as soap."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be brewed into a tea to treat stomach issues and colds."},
{"name": "Pinyon Pine", "type": "edible", "img": "https://cdn.britannica.com/81/139081-050-6615904F/Pinyon-pine-cones.jpg", "description": "Pinyon nuts are highly nutritious and can be eaten raw or roasted."},
{"name": "Fourwing Saltbush", "type": "edible", "img": "https://cdn.britannica.com/26/160426-050-4E593E8F/Fourwing-saltbush.jpg", "description": "The seeds can be ground into flour and used in traditional cooking. The leaves were also consumed during famine."},
{"name": "Sotol", "type": "edible", "img": "https://cdn.britannica.com/87/178787-050-1CDA7F5F/Sotol-leaves.jpg", "description": "The heart of the plant can be roasted or ground into flour. It's also used to make an alcoholic beverage."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems are used to make tea, which acts as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit and pads are edible. The fruit can be eaten raw or made into jams, while the pads can be cooked."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "Leaves are used in tea for treating colds and skin infections. The resin is applied as an antiseptic and healing salve."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart can be roasted or fermented into an alcoholic beverage. The sap can also be used as a sweetener."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots were used traditionally as soap."},
{"name": "Wild Radish", "type": "edible", "img": "https://cdn.britannica.com/47/148447-050-8B913F48/Wild-radish.jpg", "description": "The leaves, flowers, and seeds are edible. The leaves can be used in salads, while the seeds can be ground into a spice."},
{"name": "Sea Fig", "type": "edible", "img": "https://cdn.britannica.com/19/155419-050-0BBACB96/Sea-fig.jpg", "description": "The fruit can be eaten raw and is sometimes referred to as a beach snack."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries can be cooked and used to make syrups, jams, and pies. The flowers can also be brewed into tea."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Leaves can be brewed into tea to treat digestive problems and colds."},
{"name": "Manzanita", "type": "edible", "img": "https://cdn.britannica.com/39/187839-050-14527714/Manzanita.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in teas or as sweeteners."},
{"name": "Yerba Santa", "type": "medicinal", "img": "https://cdn.britannica.com/99/229499-050-F5D43D99/Yerba-santa.jpg", "description": "The leaves are brewed into tea for respiratory ailments and used as an expectorant."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The fruit can be eaten fresh, used in jams, or made into wine."},
{"name": "Persimmon", "type": "edible", "img": "https://cdn.britannica.com/23/176723-050-1D31D329/Persimmon.jpg", "description": "The fruit is edible once fully ripe. It can be eaten raw or used in desserts and jams."},
{"name": "Sassafras", "type": "medicinal", "img": "https://cdn.britannica.com/86/120886-050-5F623B68/Sassafras.jpg", "description": "The roots can be boiled to make a tea, traditionally used as a tonic. Leaves are used to thicken soups and stews."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used in syrups, jams, and teas. They are also believed to boost the immune system."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit can be eaten raw, with a flavor similar to banana and mango. It can also be used in desserts."},
{"name": "Blackberry", "type": "edible", "img": "https://cdn.britannica.com/28/171528-050-79D1563A/Blackberries.jpg", "description": "The berries can be eaten raw or used in jams, pies, and desserts."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries can be eaten fresh or used in pies, jams, and syrups. They are rich in vitamins and antioxidants."},
{"name": "Oregon Grape", "type": "medicinal", "img": "https://cdn.britannica.com/97/200597-050-B7987D09/Oregon-grape.jpg", "description": "The berries can be eaten raw or used in jellies. The root has been used to treat infections and digestive issues."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and are used to make tea, which can boost the immune system."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be made into a tea to help with colds and digestion."},
{"name": "Douglas Fir", "type": "medicinal", "img": "https://cdn.britannica.com/60/186760-050-13C6EBC9/Douglas-fir.jpg", "description": "The needles can be brewed into a tea rich in vitamin C, traditionally used to boost the immune system."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Black Walnut", "type": "edible", "img": "https://cdn.britannica.com/99/189699-050-354D40D5/Black-walnuts.jpg", "description": "The nuts are edible and can be used in baking or eaten raw. The hulls are also used in herbal medicine for skin health."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams and desserts."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used to make syrup, tea, and wine. They are believed to boost the immune system."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The grapes can be eaten fresh or used to make wine and jelly."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit can be eaten raw, with a flavor similar to banana and mango."},
{"name": "Dandelion", "type": "edible", "img": "https://cdn.britannica.com/27/1927-050-33CD1597/Dandelion.jpg", "description": "All parts of the dandelion are edible. The leaves can be used in salads, and the roots can be dried and roasted to make coffee."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "Leaves are used in a tea to treat colds and skin infections. The resin is applied as an antiseptic."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems have been used to make tea, which works as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour or used to make syrup. They have been a traditional food source."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots were used traditionally as soap."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave can be roasted or fermented into an alcoholic beverage. The sap can also be used as a sweetener."},
{"name": "Saw Palmetto", "type": "medicinal", "img": "https://cdn.britannica.com/28/164228-050-3D01F9F2/Saw-palmetto-fruit.jpg", "description": "The berries are used to make tea for treating prostate health."},
{"name": "Cabbage Palm", "type": "edible", "img": "https://cdn.britannica.com/46/195446-050-24B5DC70/Cabbage-palm.jpg", "description": "The heart of the palm is edible and is known as 'swamp cabbage.' It can be eaten raw or cooked."},
{"name": "Sea Grape", "type": "edible", "img": "https://cdn.britannica.com/34/173434-050-9C3F3F1D/Sea-grape.jpg", "description": "The fruit can be eaten raw or made into jelly or wine."},
{"name": "Mangrove", "type": "medicinal", "img": "https://cdn.britannica.com/82/196282-050-863DDF8D/Mangroves.jpg", "description": "Mangrove bark can be boiled to make a tea used to treat wounds and digestive problems."},
{"name": "Coconut Palm", "type": "edible", "img": "https://cdn.britannica.com/70/183370-050-95A73308/Coconut-palm.jpg", "description": "Coconut fruit is edible, and its water is a natural electrolyte drink."},
{"name": "Spanish Needle", "type": "medicinal", "img": "https://cdn.britannica.com/75/205375-050-9D04CE3A/Spanish-needle.jpg", "description": "Leaves are used in traditional medicine for treating inflammation and wounds."},
{"name": "Papaya", "type": "edible", "img": "https://cdn.britannica.com/30/217730-050-C8F67012/Papaya-fruits.jpg", "description": "The fruit can be eaten raw, and the seeds have been used traditionally as an anti-parasitic treatment."},
{"name": "Wild Onion", "type": "edible", "img": "https://cdn.britannica.com/77/184177-050-B9C0B984/Wild-onions.jpg", "description": "The bulbs can be eaten raw or cooked, and the greens can be used like chives."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The fruit can be eaten fresh, made into jelly, or fermented into wine."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries can be cooked into syrups and jams. Elderflower tea is also a traditional remedy for colds."},
{"name": "Persimmon", "type": "edible", "img": "https://cdn.britannica.com/23/176723-050-1D31D329/Persimmon.jpg", "description": "The fruit can be eaten raw when ripe or used in desserts and jams."},
{"name": "Black Walnut", "type": "edible", "img": "https://cdn.britannica.com/99/189699-050-354D40D5/Black-walnuts.jpg", "description": "The nuts are edible and can be used in baking or eaten raw."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit can be eaten raw and has a flavor similar to banana and mango."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh, used in pies, jams, and syrups."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The fruit is edible and can be eaten fresh or used in jams."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Beargrass", "type": "medicinal", "img": "https://cdn.britannica.com/36/125236-050-102D6366/Beargrass-flowers.jpg", "description": "Traditionally used by Native Americans for medicinal purposes, though not commonly consumed today."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are used to make tea, which is rich in vitamin C and boosts the immune system."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow is made into a tea to treat colds, fevers, and improve digestion."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems have been used to make tea, which acts as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling. The pads can also be cooked and eaten."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots have been used traditionally as soap."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush can be brewed into tea, which is good for colds and stomach issues."},
{"name": "Juniper", "type": "medicinal", "img": "https://cdn.britannica.com/34/9234-050-D6F3AD36/Juniper.jpg", "description": "Juniper berries are used to make tea traditionally used for treating urinary infections and digestive problems."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "The flower buds are edible after boiling. The fruits can also be eaten raw after peeling."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh or used in pies, jams, and syrups."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be used in jams or desserts."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be made into tea to relieve fevers, colds, and aid digestion."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The fruit is edible and can be eaten fresh or made into jam."},
{"name": "Oregon Grape", "type": "medicinal", "img": "https://cdn.britannica.com/97/200597-050-B7987D09/Oregon-grape.jpg", "description": "The berries can be used to make jellies, and the roots have been used to treat digestive and skin conditions."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be brewed into tea to treat colds, stomach issues, and as an antiseptic."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems are used to make a tea that acts as a decongestant and energy booster."},
{"name": "Juniper", "type": "medicinal", "img": "https://cdn.britannica.com/34/9234-050-D6F3AD36/Juniper.jpg", "description": "Juniper berries are used to make a tea to treat colds and urinary infections."},
{"name": "Pinyon Pine", "type": "edible", "img": "https://cdn.britannica.com/81/139081-050-6615904F/Pinyon-pine-cones.jpg", "description": "Pinyon nuts are highly nutritious and can be eaten raw or roasted."},
{"name": "Bitterroot", "type": "edible", "img": "https://cdn.britannica.com/67/176767-050-18DF9CC0/Bitterroot-flower.jpg", "description": "The roots can be boiled and eaten. Traditionally used by Native Americans for sustenance."},
{"name": "Indian Ricegrass", "type": "edible", "img": "https://cdn.britannica.com/49/187649-050-26E13ECF/Indian-ricegrass.jpg", "description": "The seeds can be ground into flour and used in traditional cooking."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems can be made into a tea, which works as a decongestant and energy booster."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "The flower buds can be boiled and eaten. The fruits are also edible after peeling."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "The leaves can be brewed into tea to treat digestive problems and colds."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots were used traditionally as soap."},
{"name": "Blackberry", "type": "edible", "img": "https://cdn.britannica.com/28/171528-050-79D1563A/Blackberries.jpg", "description": "The berries are edible and can be eaten fresh, used in jams, or added to desserts."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are used to make syrups, jams, and teas, and are known for their immune-boosting properties."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The grapes can be eaten fresh or used to make wine and jelly."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit can be eaten raw and has a flavor similar to banana and mango."},
{"name": "Wild Strawberry", "type": "edible", "img": "https://cdn.britannica.com/67/7667-050-4A73A32B/Wild-strawberries.jpg", "description": "The berries are edible and can be eaten fresh or used in desserts and jams."},
{"name": "Sassafras", "type": "medicinal", "img": "https://cdn.britannica.com/86/120886-050-5F623B68/Sassafras.jpg", "description": "The roots can be brewed into tea, traditionally used as a spring tonic."},
{"name": "Dandelion", "type": "edible", "img": "https://cdn.britannica.com/27/1927-050-33CD1597/Dandelion.jpg", "description": "All parts of the dandelion are edible. The leaves can be eaten in salads, and the roots can be dried and roasted."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems have been used to make tea, which works as a decongestant and energizer."},
{"name": "Sotol", "type": "edible", "img": "https://cdn.britannica.com/87/178787-050-1CDA7F5F/Sotol-leaves.jpg", "description": "The heart of the plant can be roasted or ground into flour. It is also used to make an alcoholic beverage."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave can be roasted and eaten or fermented into an alcoholic beverage. The sap can also be used as a sweetener."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots have been used traditionally as soap."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour or used to make syrup."},
{"name": "Ocotillo", "type": "medicinal", "img": "https://cdn.britannica.com/15/211815-050-3A72638C/Ocotillo-flowers.jpg", "description": "The flowers can be brewed into tea traditionally used to treat coughs and inflammation."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The grapes can be eaten fresh, made into jelly, or fermented into wine."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit can be eaten raw and has a flavor similar to banana and mango."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are used to make syrups, jams, and teas. Elderberry is known for boosting the immune system."},
{"name": "Persimmon", "type": "edible", "img": "https://cdn.britannica.com/23/176723-050-1D31D329/Persimmon.jpg", "description": "The fruit can be eaten raw when ripe or used in desserts and jams."},
{"name": "Black Walnut", "type": "edible", "img": "https://cdn.britannica.com/99/189699-050-354D40D5/Black-walnuts.jpg", "description": "The nuts are edible and can be used in baking or eaten raw."},
{"name": "Sassafras", "type": "medicinal", "img": "https://cdn.britannica.com/86/120886-050-5F623B68/Sassafras.jpg", "description": "The roots can be brewed into tea, traditionally used as a spring tonic and to flavor root beer."},
{"name": "Wild Strawberry", "type": "edible", "img": "https://cdn.britannica.com/67/7667-050-4A73A32B/Wild-strawberries.jpg", "description": "The berries are edible and can be eaten fresh or used in desserts and jams."},
{"name": "Blackberry", "type": "edible", "img": "https://cdn.britannica.com/28/171528-050-79D1563A/Blackberries.jpg", "description": "The berries can be eaten fresh or used in jams, pies, and desserts."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams and desserts."},
{"name": "Dandelion", "type": "edible", "img": "https://cdn.britannica.com/27/1927-050-33CD1597/Dandelion.jpg", "description": "All parts of the dandelion are edible. The leaves can be eaten raw in salads, and the roots can be roasted to make a coffee substitute."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The grapes can be eaten fresh or used to make wine and jelly."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries can be used to make syrups, jams, and teas. Elderberry is known for boosting the immune system."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or used in jams."},
{"name": "Blueberry", "type": "edible", "img": "https://cdn.britannica.com/90/9490-050-F5B059F5/Blueberries.jpg", "description": "The berries are edible and can be eaten fresh, used in pies, or made into jams."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams and desserts."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea, which boosts the immune system."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to relieve colds, fevers, and improve digestion."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems can be made into a tea, which acts as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "The leaves are used to make tea for treating colds, coughs, and skin infections."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour for baking or made into syrup."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave can be roasted for food or fermented into an alcoholic beverage."},
{"name": "Ocotillo", "type": "medicinal", "img": "https://cdn.britannica.com/15/211815-050-3A72638C/Ocotillo-flowers.jpg", "description": "The flowers can be brewed into tea, which is traditionally used to treat coughs and inflammation."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots have been used as soap."},
{"name": "Manzanita", "type": "edible", "img": "https://cdn.britannica.com/39/187839-050-14527714/Manzanita.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in teas or as a sweetener."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush can be brewed into tea to treat digestive problems and colds."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea that boosts the immune system."},
{"name": "Pine Nut", "type": "edible", "img": "https://cdn.britannica.com/13/71313-050-87BEA009/Pine-nuts.jpg", "description": "The seeds of the pine cones are edible and can be eaten raw or roasted. They are high in protein and fats."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries can be cooked and used in syrups, jams, and teas. They are believed to boost the immune system."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten fresh or used in pies and jams."},
{"name": "Yerba Santa", "type": "medicinal", "img": "https://cdn.britannica.com/99/229499-050-F5D43D99/Yerba-santa.jpg", "description": "The leaves are brewed into a tea for respiratory ailments and are used as an expectorant."},
{"name": "Manzanita", "type": "edible", "img": "https://cdn.britannica.com/39/187839-050-14527714/Manzanita.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in teas or as a sweetener."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are used to make tea, which is rich in vitamin C and helps boost the immune system."},
{"name": "Oregon Grape", "type": "medicinal", "img": "https://cdn.britannica.com/97/200597-050-B7987D09/Oregon-grape.jpg", "description": "The berries can be eaten raw or used in jellies. The root has been used to treat infections and digestive issues."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into a tea to relieve fevers, colds, and improve digestion."},
{"name": "Douglas Fir", "type": "medicinal", "img": "https://cdn.britannica.com/60/186760-050-13C6EBC9/Douglas-fir.jpg", "description": "The needles can be brewed into a tea rich in vitamin C, used to boost the immune system."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries can be eaten fresh or used in pies, jams, and syrups."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit can be eaten raw and has a flavor similar to banana and mango."},
{"name": "Blackberry", "type": "edible", "img": "https://cdn.britannica.com/28/171528-050-79D1563A/Blackberries.jpg", "description": "The berries can be eaten fresh or used in jams, pies, and desserts."},
{"name": "Wild Strawberry", "type": "edible", "img": "https://cdn.britannica.com/67/7667-050-4A73A32B/Wild-strawberries.jpg", "description": "The berries are edible and can be eaten fresh or used in desserts and jams."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The grapes can be eaten fresh or made into wine and jelly."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used to make syrups, jams, and teas. They are believed to boost the immune system."},
{"name": "Sassafras", "type": "medicinal", "img": "https://cdn.britannica.com/86/120886-050-5F623B68/Sassafras.jpg", "description": "The roots can be brewed into tea, traditionally used as a spring tonic and to flavor root beer."},
{"name": "Persimmon", "type": "edible", "img": "https://cdn.britannica.com/23/176723-050-1D31D329/Persimmon.jpg", "description": "The fruit can be eaten raw or used in desserts and jams when fully ripe."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit of the yucca plant are edible. The roots were used traditionally as soap."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems can be made into a tea, which works as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "The flower buds are edible after boiling. The fruits can also be eaten raw after peeling."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave can be roasted for food or fermented into an alcoholic beverage. The sap can be used as a sweetener."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour or used to make syrup. It was a traditional food source."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh or used in pies, jams, and syrups."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or used in jams."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to relieve colds, fevers, and improve digestion."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea, which boosts the immune system."},
{"name": "Douglas Fir", "type": "medicinal", "img": "https://cdn.britannica.com/60/186760-050-13C6EBC9/Douglas-fir.jpg", "description": "The needles can be brewed into tea rich in vitamin C, used to boost the immune system."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Beargrass", "type": "medicinal", "img": "https://cdn.britannica.com/36/125236-050-102D6366/Beargrass-flowers.jpg", "description": "Beargrass is traditionally used by Native Americans for medicinal purposes, though it is not commonly consumed today."},
{"name": "Blackberry", "type": "edible", "img": "https://cdn.britannica.com/28/171528-050-79D1563A/Blackberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams, pies, and desserts."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit is edible and has a tropical flavor similar to bananas and mangos."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The fruit can be eaten fresh or made into jelly and wine."},
{"name": "Persimmon", "type": "edible", "img": "https://cdn.britannica.com/23/176723-050-1D31D329/Persimmon.jpg", "description": "The fruit can be eaten raw when fully ripe or used in jams and desserts."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used in syrups, teas, and jams and are believed to boost the immune system."},
{"name": "Sassafras", "type": "medicinal", "img": "https://cdn.britannica.com/86/120886-050-5F623B68/Sassafras.jpg", "description": "The roots can be brewed into tea traditionally used as a tonic and to flavor root beer."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh or used in pies, jams, and syrups."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or used in jams."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea that boosts the immune system."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to relieve colds, fevers, and improve digestion."},
{"name": "Oregon Grape", "type": "medicinal", "img": "https://cdn.britannica.com/97/200597-050-B7987D09/Oregon-grape.jpg", "description": "The berries can be eaten raw or made into jelly, and the roots are used to treat skin and digestive issues."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh or used in pies, jams, and syrups."},
{"name": "Salmonberry", "type": "edible", "img": "https://cdn.britannica.com/28/185228-050-4136F7D4/Salmonberry.jpg", "description": "The berries are edible and can be eaten raw or used in jams."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or made into jam."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea that boosts the immune system."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to treat colds, fevers, and digestive issues."},
{"name": "Devil’s Club", "type": "medicinal", "img": "https://cdn.britannica.com/27/229127-050-F58B55B4/Devils-club.jpg", "description": "The roots and inner bark are used in traditional medicine to treat arthritis, colds, and respiratory conditions."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems can be made into a tea that acts as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots have been used traditionally as soap."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "The leaves are brewed into tea to treat colds and skin infections."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave can be roasted for food or fermented into an alcoholic beverage. The sap can also be used as a sweetener."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "The flower buds are edible after boiling, and the fruits can also be eaten after peeling."},
{"name": "Manzanita", "type": "edible", "img": "https://cdn.britannica.com/39/187839-050-14527714/Manzanita.jpg", "description": "The berries can be eaten raw or dried. They are often used in teas or as a sweetener."},
{"name": "Yerba Santa", "type": "medicinal", "img": "https://cdn.britannica.com/99/229499-050-F5D43D99/Yerba-santa.jpg", "description": "The leaves are brewed into a tea traditionally used to treat respiratory ailments."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be brewed into tea to treat digestive problems and colds."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and are used to make tea that boosts the immune system."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used to make syrups, jams, and teas and are believed to boost the immune system."},
{"name": "Pine Nut", "type": "edible", "img": "https://cdn.britannica.com/13/71313-050-87BEA009/Pine-nuts.jpg", "description": "Pine nuts are edible and can be eaten raw or roasted. They are rich in protein and fats."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh or used in pies, jams, and syrups."},
{"name": "Salmonberry", "type": "edible", "img": "https://cdn.britannica.com/28/185228-050-4136F7D4/Salmonberry.jpg", "description": "The berries are edible and can be eaten raw or used in jams."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea that boosts the immune system."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or used in jams."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to relieve colds, fevers, and digestive issues."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh, used in pies, or made into jams."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams and desserts."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea, which boosts the immune system."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to treat colds, fevers, and improve digestion."},
{"name": "Pinyon Pine", "type": "edible", "img": "https://cdn.britannica.com/81/139081-050-6615904F/Pinyon-pine-cones.jpg", "description": "Pinyon nuts are edible and highly nutritious. They can be eaten raw or roasted."},
{"name": "Juniper", "type": "medicinal", "img": "https://cdn.britannica.com/34/9234-050-D6F3AD36/Juniper.jpg", "description": "Juniper berries are used to make tea traditionally used for treating urinary infections and digestive issues."},
{"name": "Saguaro Cactus", "type": "edible", "img": "https://cdn.britannica.com/46/195146-050-4E64E68B/Saguaro-cactus.jpg", "description": "The fruit of the saguaro is edible and can be eaten fresh or made into syrup or jam."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling. The pads can be cooked and eaten."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "The leaves are brewed into tea to treat colds, coughs, and skin infections."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems can be made into tea that works as a decongestant and energizer."},
{"name": "Ocotillo", "type": "medicinal", "img": "https://cdn.britannica.com/15/211815-050-3A72638C/Ocotillo-flowers.jpg", "description": "The flowers can be brewed into tea, traditionally used to treat coughs and inflammation."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour for baking or made into syrup."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "The flower buds of the cholla cactus are edible after boiling. The fruits can also be peeled and eaten."},
{"name": "Manzanita", "type": "edible", "img": "https://cdn.britannica.com/39/187839-050-14527714/Manzanita.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in teas or as a sweetener."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be brewed into tea to treat digestive problems and colds."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea that boosts the immune system."},
{"name": "Pine Nut", "type": "edible", "img": "https://cdn.britannica.com/13/71313-050-87BEA009/Pine-nuts.jpg", "description": "Pine nuts are edible and can be eaten raw or roasted. They are rich in protein and fats."},
{"name": "Yerba Santa", "type": "medicinal", "img": "https://cdn.britannica.com/99/229499-050-F5D43D99/Yerba-santa.jpg", "description": "The leaves are brewed into tea to treat respiratory ailments and are used as an expectorant."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used in syrups, jams, and teas and are believed to boost the immune system."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten fresh or dried. They are often used in pies and jams."},
{"name": "Blackberry", "type": "edible", "img": "https://cdn.britannica.com/28/171528-050-79D1563A/Blackberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams, pies, and desserts."},
{"name": "Pawpaw", "type": "edible", "img": "https://cdn.britannica.com/55/188755-050-7FE59EB4/Pawpaw-fruit.jpg", "description": "The fruit is edible and has a tropical flavor similar to banana and mango."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams and desserts."},
{"name": "Wild Grape", "type": "edible", "img": "https://cdn.britannica.com/88/128388-050-EBFBB9BD/Wild-grape-vines.jpg", "description": "The grapes can be eaten fresh or used to make jelly and wine."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used to make syrups, jams, and teas and are known for boosting the immune system."},
{"name": "Sassafras", "type": "medicinal", "img": "https://cdn.britannica.com/86/120886-050-5F623B68/Sassafras.jpg", "description": "The roots can be brewed into tea, traditionally used as a spring tonic and to flavor root beer."},
{"name": "Dandelion", "type": "edible", "img": "https://cdn.britannica.com/27/1927-050-33CD1597/Dandelion.jpg", "description": "All parts of the dandelion are edible. The leaves can be eaten raw in salads, and the roots can be roasted to make a coffee substitute."},
{"name": "Buffalo Berry", "type": "edible", "img": "https://cdn.britannica.com/86/202786-050-CDAAB979/Buffalo-berry.jpg", "description": "The berries can be eaten fresh or dried and are used in jams, jellies, and sauces."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Wild Onion", "type": "edible", "img": "https://cdn.britannica.com/77/184177-050-B9C0B984/Wild-onions.jpg", "description": "The bulbs are edible and can be used similarly to domesticated onions, added to stews or eaten raw."},
{"name": "Chokecherry", "type": "edible", "img": "https://cdn.britannica.com/46/196746-050-4BCE5E1B/Chokecherry-fruit.jpg", "description": "The berries can be used to make jelly, syrup, or wine. They were traditionally a food source for Native Americans."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be brewed into tea to treat digestive problems and colds."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to relieve fevers, colds, and aid digestion."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit are edible, and the roots were used traditionally as soap."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit is edible after peeling, and the pads can be cooked and eaten."},
{"name": "Sotol", "type": "edible", "img": "https://cdn.britannica.com/87/178787-050-1CDA7F5F/Sotol-leaves.jpg", "description": "The heart of the plant can be roasted or ground into flour. It’s also used to make an alcoholic beverage."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "Leaves are brewed into tea to treat colds and skin infections. The resin is used as an antiseptic."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems are used to make tea, which acts as a decongestant and energizer."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour for baking or made into syrup."},
{"name": "Buffalo Berry", "type": "edible", "img": "https://cdn.britannica.com/86/202786-050-CDAAB979/Buffalo-berry.jpg", "description": "The berries are edible and can be eaten fresh or dried. They are commonly used in jams and sauces."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling. The pads can be cooked and eaten as well."},
{"name": "Wild Onion", "type": "edible", "img": "https://cdn.britannica.com/77/184177-050-B9C0B984/Wild-onions.jpg", "description": "The bulbs can be eaten raw or cooked, similar to domesticated onions."},
{"name": "Chokecherry", "type": "edible", "img": "https://cdn.britannica.com/46/196746-050-4BCE5E1B/Chokecherry-fruit.jpg", "description": "The berries can be made into jelly, syrup, or wine."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush leaves can be brewed into tea, traditionally used to treat colds and stomach issues."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to relieve fevers and colds, and improve digestion."},
{"name": "Huckleberry", "type": "edible", "img": "https://cdn.britannica.com/95/118395-050-89E9DBB7/Huckleberries.jpg", "description": "The berries are edible and can be eaten fresh or used in pies, jams, and syrups."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried, commonly used in pies and jams."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or made into jams."},
{"name": "Yarrow", "type": "medicinal", "img": "https://cdn.britannica.com/59/2459-050-85A15DC1/Yarrow-flowers.jpg", "description": "Yarrow can be brewed into tea to relieve colds, fevers, and improve digestion."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea that boosts the immune system."},
{"name": "Juniper", "type": "medicinal", "img": "https://cdn.britannica.com/34/9234-050-D6F3AD36/Juniper.jpg", "description": "Juniper berries can be made into tea traditionally used to treat colds and urinary infections."},
{"name": "Manzanita", "type": "edible", "img": "https://cdn.britannica.com/39/187839-050-14527714/Manzanita.jpg", "description": "The berries can be eaten raw or dried. They are often used in teas or as a sweetener."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or used in jams."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten raw or dried. They are often used in pies and jams."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea that boosts the immune system."},
{"name": "Yerba Santa", "type": "medicinal", "img": "https://cdn.britannica.com/99/229499-050-F5D43D99/Yerba-santa.jpg", "description": "The leaves are brewed into tea, traditionally used for respiratory ailments."},
{"name": "Sagebrush", "type": "medicinal", "img": "https://cdn.britannica.com/95/202695-050-4CEBC0E3/Sagebrush.jpg", "description": "Sagebrush can be brewed into tea to treat colds and digestive problems."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used in syrups, teas, and jams, and are known for their immune-boosting properties."},
{"name": "Mormon Tea", "type": "medicinal", "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg", "description": "The boiled stems have been used to make a tea that acts as a decongestant and energizer."},
{"name": "Prickly Pear Cactus", "type": "edible", "img": "https://cdn.britannica.com/91/200391-050-3EAD9E85/Prickly-pear-cactus.jpg", "description": "The fruit, known as tuna, is edible after peeling, and the pads can also be cooked and eaten."},
{"name": "Yucca", "type": "edible", "img": "https://cdn.britannica.com/51/211451-050-11B6036D/Yucca-plant.jpg", "description": "The flowers and fruit of the yucca plant are edible. The roots were used traditionally as soap."},
{"name": "Cholla Cactus", "type": "edible", "img": "https://cdn.britannica.com/33/128133-050-973EAACB/Cholla-cactus.jpg", "description": "The flower buds of the cholla cactus are edible after boiling. The fruits can also be peeled and eaten."},
{"name": "Mesquite", "type": "edible", "img": "https://cdn.britannica.com/28/206128-050-35CBEA88/Mesquite-tree.jpg", "description": "Mesquite pods can be ground into flour for baking or made into syrup."},
{"name": "Creosote Bush", "type": "medicinal", "img": "https://cdn.britannica.com/77/204377-050-1E23C172/Creosote-bush.jpg", "description": "The leaves are brewed into tea to treat colds, coughs, and skin infections."},
{"name": "Agave", "type": "edible", "img": "https://cdn.britannica.com/07/200507-050-789B78D7/Agave.jpg", "description": "The heart of the agave can be roasted for food or fermented into an alcoholic beverage. The sap can be used as a sweetener."},
{"name": "Wild Raspberry", "type": "edible", "img": "https://cdn.britannica.com/83/111283-050-ED9BCE7B/Raspberries.jpg", "description": "The berries are edible and can be eaten fresh or used in jams and desserts."},
{"name": "Blueberry", "type": "edible", "img": "https://cdn.britannica.com/90/9490-050-F5B059F5/Blueberries.jpg", "description": "Blueberries are edible and can be eaten fresh or used in pies and jams."},
{"name": "Thimbleberry", "type": "edible", "img": "https://cdn.britannica.com/20/128120-050-21FDE803/Thimbleberry-fruits.jpg", "description": "The berries are edible and can be eaten fresh or made into jams."},
{"name": "Elderberry", "type": "edible", "img": "https://cdn.britannica.com/60/126060-050-453EC5A6/Elderberries.jpg", "description": "The berries are often used in syrups, jams, and teas, and are known for boosting the immune system."},
{"name": "Serviceberry", "type": "edible", "img": "https://cdn.britannica.com/03/227203-050-A00CCF5C/Serviceberry.jpg", "description": "The berries are edible and can be eaten fresh or dried, often used in pies and jams."},
{"name": "Wild Rose", "type": "medicinal", "img": "https://cdn.britannica.com/54/179054-050-55605ED8/Wild-rose.jpg", "description": "Rose hips are rich in vitamin C and can be used to make tea to boost the immune system."}
]

    
    
    
    
    
    
    
    
    
    

# plants = [
#     {
#         "name": "Japanese Knotweed",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/45/246545-050-677C999F/Japanese-knotweed-plant.jpg",
#         "description": "Once established, this perennial herbaceous plant can grow up to 10 feet in one growing season. Its young shoots are the most consumed part, as they are tender and have a tart flavor reminiscent of rhubarb."},
#     {
#         "name": "Garlic Mustard",
#         "type": "edible",
#         "img": "https://mucc.org/wp-content/uploads/2024/03/20210502-garlic-mustard-1a-c-JJ-Prekop-Jr.webp",
#         "description": "Garlic mustard is a biennial, which means it produces seed on its second year that spreads by seed dispersal and can grow up to six feet tall. It’s best to harvest when the plant is younger and only eat the leaves."},
#     {
#         "name": "Blueberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14798/content_c1-Image-by-Tim-Rains_-of-Denali-National-Park-and-Preserve.-Droplets-of-Ice--Blueberry.-Denali-National-Park-and-Preserve.jpg",
#         "description": "Starting in July through August, diverse and delectable species of wild Maine blueberries are ripening. Acadia National park, with its ledges and naturally acidic soils are prime places to see these wild plants."},
#     {
#         "name": "Serviceberries",
#         "type": "edible",
#         "img": "https://www.gardenista.com/wp-content/uploads/2023/06/serviceberries-june-marie-viljoen.jpg",
#         "description": "Many people make the mistake of harvesting Amelanchier fruit while it’s still red. Red berries are certainly edible, but they are not fully ripe. Berries are at their best when they ripen to a dark, purple-blue. At this stage they are sweet, plump, and juicy. The fruit ripens gradually, over a period of weeks, so this will be a graduated harvest. "
#     },

#        {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."},
#     {
#         "name": "Raspberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
#         "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
#     },
#      {
#         "name": "Red Currants",
#         "type": "medicinal",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14800/content_c3-Image-by-Emilie-Barbier.-Wild-Red-Currant.jpg",
#         "description": "Red currants are small, round, and almost spherical, with a translucent skin that can sometimes show the pips inside. They have ribs that resemble lines of longitude on a globe. Red currants have a tart flavor due to their high content of organic acids and polyphenols."
#     },
#        {
#         "name": "Elderberries",
#         "type": "medicinal",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14801/content_c4-Image-by-Mark-Robinson.-Elderberries.jpg",
#         "description": "Berries and flowers are used in traditional remedies for immune support and to treat colds and flu. Berries must be cooked before consumption to avoid toxicity."},
#     {
#         "name": "Hickory Nuts",
#         "type": "edible",
#         "img": "https://www.mossyoak.com/sites/default/files/inline-images/green-hickory-nuts.jpg",
#         "description": "Hickory nuts can taste sweet, dense, and rich, and some say they taste better than pecans or walnuts. However, the taste varies by species, with some being bitter. For example, bitternut hickory nuts are so bitter that many squirrels avoid them."
#     },
#        {
#         "name": "Chestnuts",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/92/182092-050-114F4DA5/European-chestnut.jpg?w=400&h=300&c=crop",
#         "description": "Chestnuts grow inside a spiky husk that splits open when the nuts are mature. The number of nuts in a husk depends on the species, but it's usually one to seven. The nuts are edible and have been a vital food source for rural populations, especially in the winter"},
#     {
#         "name": "Beechnuts",
#         "type": "edible",
#         "img": "https://naturallycuriouswithmaryholland.wordpress.com/wp-content/uploads/2019/08/8-7-19-beechnuts-0u1a0160.jpg",
#         "description": "Beech nuts can taste bitter, astringent, or mild and nut-like. Some say they taste like a cross between a pine nut and a hazelnut."
#     },
    
#       {
#         "name": "Fiddlehead",
#         "type": "edible",
#         "img": "https://www.recordonline.com/gcdn/authoring/2017/03/18/NTHR/ghows-TH-4acb951e-3b2d-42d3-e053-0100007f6645-c481c407.jpeg",
#         "description": "Do not eat this plant raw, if you can make a fire, you should cook for at least 5 minutes. The spring plant peaks in May and the sprouts are generally foraged or picked from late April to early June before the plant grows into a fiddlehead fern."
#     },
#         {
#         "name": "Sweetgrass",   
#         "type": "medicinal",
#         "img": "https://i.etsystatic.com/20994514/r/il/6ab59d/3248729537/il_fullxfull.3248729537_dprx.jpg",
#         "description": "You can make tea from this plant to treat coughs and sore throats. Windburn and chapping were treated through an infusion of sweetgrass stems soaked in water or a salve of sweetgrass water and grease. The sweetgrass water was also used as an eyewash."
#     },
#           {
#         "name": "Mormon Tea",
#         "type": "medicinal",
#        "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#         "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
#     },
#             {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#          {
#         "name": "Garlic Mustard",
#         "type": "edible",
#         "img": "https://mucc.org/wp-content/uploads/2024/03/20210502-garlic-mustard-1a-c-JJ-Prekop-Jr.webp",       
#         "description": "Garlic mustard is a biennial, which means it produces seed on its second year that spreads by seed dispersal and can grow up to six feet tall. It’s best to harvest when the plant is younger and only eat the leaves."},
    
#     {
#         "name": "Wild Spinach",
#         "type": "edible",
#         "img": "https://loganspader.com/wp-content/uploads/2022/08/wild-spinach-sd-wild-edible-plant-sss.jpg?strip=info&w=528",
#         "description":"Also known as lambs quarters this wild plant is best eaten raw as a snack while hiking but also works great in salads or sandwiches. Starts growing in South Dakota in the early summer."
#     },
#       {
#         "name": "Purlsane",
#         "type": "edible",
#         "img": "https://loganspader.com/wp-content/uploads/2022/08/purslane-close-up-sioux-falls-lawn-weed-edible-sss.jpg?strip=info&w=800",
#         "description":"This starts growing midsummer in SD and should be eaten raw"
#     },
#         {
#         "name": "Stinging nettle",
#         "type": "edible",
#         "img": "https://loganspader.com/wp-content/uploads/2022/08/stinging-nettle-plant-wild-edible-food-22-sss.jpg?strip=info&w=800",
#        "description": "Can be eaten raw, just watch out for the pricks."
#     },
#           {
#         "name": "Cattail",
#         "type": "edible",
#         "img": "https://www.fs.usda.gov/Internet/FSE_MEDIA/stelprdb5070148.jpg",
#         "description":"Pluck out of the water and slice the lower end open (just above the roots) like a banana until you get to the crisp core. Be sure to look for young shoots."
#           },
#             {
#         "name": "Wood Sorrel",
#         "type": "edible",
#         "img": "https://loganspader.com/wp-content/uploads/2022/08/wood-sorel-great-bear-sd-22-sss.jpg?strip=info&w=800",
#         "description":"Can be eaten raw."
#     },
#               {
#         "name": "Mulberries",
#         "type": "edible",
#         "img": "https://loganspader.com/wp-content/uploads/2022/08/mulberry-leaves-sd-s.jpg?strip=info&w=1080",
#         "description":"Dark berry that can be eaten raw, and July is the best time to forage them."
#     },
#           {
#         "name": "Wild Licorice",
#         "type": "medicinal",
#         "img": "https://www.prairiemoon.com/mm5/graphics/00000001/glycyrrhiza-lepidota-wild-licorice_main_548x730.jpg",
#         "description":"Native Americans used the root extensively as an herbal remedy for common things like fever, stomach ache, toothache, ear infection and sore throat. The Dakota's steeped the licorice leaves in boiling water to make a topical medicine for earache. The root was also chewed and held in the mouth to relieve toothache. The Blackfeet made a tea from bitter tasting root to relieve coughs, chest pain and sore throat."
#     },
     
#                         {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#                                {
#         "name": "Lechuguilla",
#         "type": "edible",
#         "img": "https://coldhardycactus.com/cdn/shop/products/YuccalechuguillaGuadalupes1.jpg?v=1607876162",
#         "description":"Although primarily known for its fibrous leaves used in traditional crafts, the base and young flower stalks can be cooked and eaten in survival situations."
#     },
#                                       {
#         "name": "Ocotillo",
#         "type": "medicinal",
#         "img": "https://m.media-amazon.com/images/I/811+ITLQT3L.jpg",
#         "description":"This plant is known for its ability to sprout leaves rapidly after rain. It has traditional medicinal uses, such as creating a soothing tea from its flowers to treat symptoms like coughs and chest congestion."
#     },
#                                              {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
#                                                     {
#         "name": "Honey Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },
#         {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
#            {
#         "name": "Mormon Tea",
#         "type": "medicinal",
#         "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#         "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
#     },
#                                          {
#         "name": "Beautyberry",
#         "type": "edible",
#         "img": "https://gardeningsolutions.ifas.ufl.edu/images/plants/shrubs/beautyberry2021.jpg",
#         "description":"Native Americans used the beautyberry for a variety of medicinal purposes, including treating malaria, rheumatism, dizziness, stomachaches, and dysentery. Leaves and other parts of the plant were boiled for use in sweat baths to treat malarial fevers and rheumatism. "
#     },
#                                                     {
#         "name": "Dandelion",
#         "type": "edible",
#         "img":"https://images.immediate.co.uk/production/volatile/sites/10/2018/02/61078405-281c-4a49-8d1e-2e445fe64960-378bd75.jpg?quality=90&webp=true&resize=900,600",      
#         "description":"Leafs and flowers can be eaten raw."
#     },
                              
#                                                                           {
#         "name": "Orache",
#         "type": "edible",
#         "img": "https://thumbs.dreamstime.com/z/atriplex-hortensis-orache-used-as-leaf-vegetable-salads-spring-edible-plant-orach-grows-garden-closeup-also-known-248814192.jpg",
#         "description":"Can be eaten raw."
#     },
#                    {
#         "name": "Musk Mustard",
#         "type": "edible",
#         "img": "data:image/jpeg;base64,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",
#         "description":"Like all mustards, the entire plant can be eaten! Musk mustard is one of the mustards that tastes pretty good and lacks a lot of the bitter or hot flavors that can be common in these plants."
#     },
#                               {
#         "name": "Curly Dock",
#         "type": "edible",
#         "img": "https://images.squarespace-cdn.com/content/v1/61fc74eb0ad5900c8e413b64/f2afb1bc-0d1e-4d8f-b12d-8b2f5292bc9d/Dock3.jpeg?format=1500w",
#         "description":"Harvest curly dock in the spring before the plant flowers. Once the plant flowers, the stems become tough and fibrous and are no longer edible."
#     },
#                                          {
#         "name": "Salsify",
#         "type": "edible",
#         "img": "https://nurturenaturecenter.org/wp-content/uploads/2022/06/DSCF2489-382x509.jpg",
#         "description":"Young roots can be eaten raw, otherwise you can boil the leaves and roots."
#     },
#                        {
#         "name": "Prickly Lettuce",
#         "type": "edible",
#         "img": "https://crops.extension.iastate.edu/files/resize/article/prklyletplant-600x896.jpg",
#         "description":"Leaves can be eaten raw, or you can boil the shoots. Prickly lettuce has a distinctive line of reddish bristles on the underside of the leaf midrib. When you cut the plant, a milky juice will come out of the leaves and stem."
#     },
#                             {
#         "name": "Fireweed",
#         "type": "edible",
#         "img": "https://i0.wp.com/practicalselfreliance.com/wp-content/uploads/2021/05/Fireweed-Plant1-.jpg?resize=1200%2C1800&ssl=1",
#         "description":"Can eat seeds and flowers raw, and can cook the roots. It's best to eat leaves raw when they are young. The seeds can also be a firestarter!"
#     },
#                             {
#         "name": "Arrowleaf Balsamroot ",
#         "type": "medicinal",
#         "img": "https://www.fs.usda.gov/wildflowers/plant-of-the-week/images/arrowleafbalsamroot/balsamorhiza_sagittata.jpg",
#         "description":"Medicinally, Native Americans used the large coarse balsamroot leaves as a poultice for burns. Some tribes boiled the roots for a medicinal tea for tuberculosis and whooping cough, rheumatism, headaches, insect bites. Other tribes made an infusion to use as a poultice for wounds, cuts and bruises."
#     },
#                             {
#         "name": "Fern-leaf Desert Parsley",
#         "type": "edible",
#         "img": "https://gardenshop.symbiop.com/cdn/shop/products/lom_dispsd_1200x1200.jpg?v=1638219109",
#         "description":"The roots are edible and can be eaten roasted, steamed, or boiled, or ground into flour. The young leaves and shoots can be eaten raw or cooked."
#     },
#                             {
#         "name": "Fern-leaf Desert Parsley",
#         "type": "medicinal",
#         "img": "https://gardenshop.symbiop.com/cdn/shop/products/lom_dispsd_1200x1200.jpg?v=1638219109",
#         "description":"The roots are used to make medicine for a variety of conditions, including asthma, colds, flu, lung injuries, pneumonia, tuberculosis, and viral infections. It can also be applied as a dressing to treat sores, cuts, boils, bruises, sprains, broken bones, burns, and other skin wounds"
#     },
#                             {
#         "name": "Greenleaf Manzanita",
#         "type": "edible",
#         "img": "https://bloomcalifornia.org/wp-content/uploads/2021/09/arctostaphylos-glauca_big-berry-manzanita_inat-800.jpg",
#         "description":"It features simple, green leaves and reddish-brown bark. The plant produces pink, urn-shaped flowers in small clusters during spring, followed by green berries that turn rusty red when ripe. The seeds can be roasted or ground into flour, and the young shoots and leaves are also edible."
#     },
#                             {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#         {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
    
#                             {
#         "name": "Evening Primrose",
#         "type": "edible",
#         "img": "https://commonsensehome.com/wp-content/uploads/2023/09/common-evening-primrose-flower.jpg",
#         "description":"You can eat the leaves from a young plant, or boil the shoots."
#     },
    
#                             {
#         "name": "Four O'Clock",
#         "type": "medicinal",
#         "img": "https://www.kitchengardenseeds.com/media/catalog/product/cache/b8afbc9b375ff88a260fed7bdf351322/4/o/4oclocks1-w.jpg",
#         "description":"This plant has a long history of use by Native American tribes such as the Navajo and Hopi. It is primarily used for its roots, which are made into poultices to treat skin conditions and infections. The plant features trumpet-shaped flowers that bloom in the evening."
#     },
#          {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
    
#         {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
    
#                             {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
    
#                             {
#         "name": "Fourwing saltbush",
#         "type": "edible",
#         "img": "https://cdn11.bigcommerce.com/s-9ht3qzdye/images/stencil/960w/products/357/2923/fourwingsaltbush_Atriplex_canescens_var_canescens_3__93515.1657035474.jpg?c=1",
#         "description":"The seeds of this shrub are a valuable food source for wildlife and birds. Native Americans also ate the seeds and ground them into flour, and boiled the leaves to make a yellow dye. "
#     },
    
#        {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
    
#                             {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
#        {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
    
#                             {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
#                              {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
#        {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
#      {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#       {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
                            
                
#                                                     {
#         "name": "Honey Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#                                                     },
#     {
#         "name": "Cholla",
#         "type": "edible",
#         "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
#         "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
#     },
#       {
#         "name": "Catalina Cherry",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Prunus_ilicifolia_ne1.jpg/440px-Prunus_ilicifolia_ne1.jpg",
#         "description":"This plant can grow as a shrub or a tree, and its fruit is edible. The fruit is dark purple to black when ripe, and has a large seed and pulpy flesh. The pits can be boiled to remove toxic chemicals, then mashed and eaten"
#     },
#       {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#       {
#         "name": "Manzanita",
#         "type": "edible",
#         "img": "https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153664648468496389.jpeg?x-oss-process=image/format,webp/resize,s_600&v=1.0",
#         "description":" The berries are edible and can be eaten raw or used to make cider. The leaves have been used in traditional remedies for treating stomach ailments."
#     },
#       {
#         "name": "Deer Grass",
#         "type": "edible",
#         "img": "https://www.cpp.edu/biotrek/img/ethnobotany/Ethnobotany%20Images/muhlenbergia_rigens_1.jpeg",
#         "description":" The foundation of the plant materials were used for coiled baskets. The seeds are edible and were often eaten by natives."
#     },
#       {
#         "name": "Lemonade Berry ",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Lemonadeberry2.jpg/440px-Lemonadeberry2.jpg",
#         "description":"The berries of this plant can be soaked in water to make a lemonade-like drink. The plant also has medicinal uses, including as a treatment for respiratory issues"
#     },
#         {
#         "name": "Pawpaw",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Asimina_triloba3.jpg/440px-Asimina_triloba3.jpg",
#         "description": "Produces a large, yellowish-green fruit that is edible and has a custard-like taste. It is rich in nutrients and can be eaten raw or used in various recipes."
#     },
#     {
#         "name": "Spicebush",
#         "type": "medicinal",
#         "img": "https://www.joyfulbutterfly.com/wp-content/uploads/2015/02/Lindera_benzoin.jpg",
#         "description": "The berries and leaves are used to make tea, traditionally used to treat fevers, colds, and gastrointestinal issues."
#     },
#     {
#         "name": "Jewelweed",
#         "type": "medicinal",
#         "img": "https://www.adirondackalmanack.com/wp-content/uploads/2015/07/Jewelweed-540x702.jpg",
#         "description": "Known for treating skin irritations, such as poison ivy rashes. The leaves and juice from the stem are applied directly to the skin."
#     },
#     {
#         "name": "Wild Ginger",
#         "type": "edible",
#         "img": "https://www.eattheweeds.com/wp-content/uploads/2017/09/Asarum_canadense.jpg",
#         "description": "The roots can be used as a spice or brewed into a tea. It has been used to aid digestion and treat intestinal ailments."
#     },
#     {
#         "name": "Greenbrier",
#         "type": "edible",
#         "img": "https://www.carolinanature.com/trees/smro6025.jpg",
#         "description": "The young shoots and leaves are edible raw or cooked, similar to asparagus. The roots can be used to make a starchy paste."
#     },
#     {
#         "name": "Nettle",
#         "type": "medicinal",
#         "img": "https://www.wildedible.com/sites/default/files/styles/1200wide/public/stinging-nettles-p.jpg.webp?itok=DBoqFtXF",
#         "description": "Once cooked, the leaves are safe to eat and very nutritious. Nettle has been used medicinally for its anti-inflammatory properties and as a diuretic."
#     },
#      {
#         "name": "Oregon Grape",
#         "type": "medicinal",
#         "img": "https://www.nps.gov/articles/000/images/B_aquifolium_Bruce_Newhouse_ORFloraProject_permission.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
#         "description": "The roots contain berberine, used as an antimicrobial agent. The berries are tart but edible and can be made into jellies or fermented into wine."
#     },
#                     {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#     {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },
#     {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."
#     },
#     {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#      {
#         "name": "Jewelweed",
#         "type": "medicinal",
#         "img": "https://www.adirondackalmanack.com/wp-content/uploads/2015/07/Jewelweed-540x702.jpg",
#         "description": "Known for treating skin irritations, such as poison ivy rashes. The leaves and juice from the stem are applied directly to the skin."
#     },
#     {
#         "name": "Wild Ginger",
#         "type": "edible",
#         "img": "https://www.eattheweeds.com/wp-content/uploads/2017/09/Asarum_canadense.jpg",
#         "description": "The roots can be used as a spice or brewed into a tea. It has been used to aid digestion and treat intestinal ailments."
#     },
#      {
#         "name": "Elderberries",
#         "type": "medicinal",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14801/content_c4-Image-by-Mark-Robinson.-Elderberries.jpg",
#         "description": "Berries and flowers are used in traditional remedies for immune support and to treat colds and flu. Berries must be cooked before consumption to avoid toxicity."},
#   {
#         "name": "Raspberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
#         "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
#     },
#       {
#         "name": "Nettle",
#         "type": "medicinal",
#         "img": "https://www.wildedible.com/sites/default/files/styles/1200wide/public/stinging-nettles-p.jpg.webp?itok=DBoqFtXF",
#         "description": "Once cooked, the leaves are safe to eat and very nutritious. Nettle has been used medicinally for its anti-inflammatory properties and as a diuretic."
#     },
#       {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
    
#       {
#         "name": "Cholla",
#         "type": "edible",
#         "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
#         "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
#     },
#          {
#         "name": "Mormon Tea",
#         "type": "medicinal",
#         "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#         "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
#     },
#      {
#         "name": "Desert Holly",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/California_Death_Valley_Ubehebe_plant.jpg/440px-California_Death_Valley_Ubehebe_plant.jpg",
#         "description": "The leaves of Desert Holly can be eaten raw or cooked. They have a salty flavor and are often used as a seasoning."
#     },
#                    {
#         "name": "Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },
#                      {
#         "name": "Sea Grape",
#         "type": "edible",
#         "img": "https://www.tcpalm.com/gcdn/presto/2019/11/05/PTCN/4e32f5d7-4f63-4006-95c5-ec15f405ad57-Coccoloba_uvifera_Nov_17.JPG?width=600&height=636&fit=crop&format=pjpg&auto=webp",
#         "description": "Sea Grape fruits can be eaten fresh or made into jellies and wines. The large leaves can also be used for relief from sunburn."
#     },
#     {
#         "name": "Scaevola Taccada",
#         "type": "medicinal",
#         "img": "https://toptropicals.com/pics/garden/m2/2014/8/20140830_115553Scaevola_taccada_TA.jpg",
#         "description": "Also known as sea lettuce, the leaves of this plant are used in traditional medicine to treat eye infections and as a general antiseptic."
#     },
#     {
#         "name": "Buttonwood",
#         "type": "medicinal",
#         "img": "https://tinezfarms.com/cdn/shop/files/buttonwood-standard-green-conocarpus-erectus-plantologyusa-3-gallon-148229_jpg_1024x.webp?v=1720462168",
#         "description": "The bark of Buttonwood is used in traditional remedies for headaches and muscle pain."
#     },
#     {
#         "name": "Saw Palmetto",
#         "type": "medicinal",
#         "img": "https://www.meadowbeautynursery.com/wp-content/uploads/2017/01/Charleston-067.jpg",
#         "description": "Saw Palmetto berries are used in traditional medicine for their benefits to prostate health and hormone regulation."
#     },
#    {
#         "name": "Cattail",
#         "type": "edible",
#         "img": "https://www.fs.usda.gov/Internet/FSE_MEDIA/stelprdb5070148.jpg",
#         "description":"Pluck out of the water and slice the lower end open (just above the roots) like a banana until you get to the crisp core. Be sure to look for young shoots."
#           },
#     {
#         "name": "Cocoplum",
#         "type": "edible",
#         "img": "https://images.squarespace-cdn.com/content/v1/58458123ff7c506672298481/1538408730987-1Y3IFQ3TYP5PVRX17P2P/Plant+Creations+Nursery+Cocoplum+Chrysobalanus+icaco?format=750w",
#         "description": "Cocoplum fruit can be eaten fresh or made into jams and jellies. The stone inside can also be cracked open to extract an edible kernel."
#     },
#     {
#         "name": "Mangrove",
#         "type": "medicinal",
#         "img": "https://npr.brightspotcdn.com/dims4/default/9ec1db0/2147483647/strip/true/crop/5725x3822+0+0/resize/840x560!/format/webp/quality/90/?url=https%3A%2F%2Fnpr.brightspotcdn.com%2Fd9%2Faa%2Fa8bbc4cb4394a52629701f0d82d1%2F42394815810-08191c1c4b-o.jpg",
#         "description": "Mangrove bark is used in traditional medicine to treat skin conditions and wounds due to its antiseptic properties."
#     },
#                                           {
#         "name": "Dandelion",
#         "type": "edible",
#         "img":"https://images.immediate.co.uk/production/volatile/sites/10/2018/02/61078405-281c-4a49-8d1e-2e445fe64960-378bd75.jpg?quality=90&webp=true&resize=900,600",
#         "description":"Leafs and flowers can be eaten raw."
#     },
#                                            {
#         "name": "Plantain",
#         "type": "medicinal",
#         "img": "https://weedid.missouri.edu/images/images_optimized/2455optimized.jpg",
#         "description": "Plantain leaves are known for their medicinal properties, particularly for treating skin irritations and wounds. They can be crushed and applied as a poultice directly to the skin to soothe inflammation."
#     },
#     {
#         "name": "White Clover",
#         "type": "edible",
#         "img": "https://www.thespruce.com/thmb/ojIM2rHV6W2v4UdsLdhFFbRDp58=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/growing-white-clover-trifolium-repens-5101230-hero-e134e5d705eb48309508c55110bff91d.jpg",
#         "description": "White clover flowers and leaves are edible, often used in teas and salads. The flowers can also be dried and added to baked goods for a sweet, vanilla-like flavor."
#     },
#     {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
#        {
#         "name": "Fireweed",
#         "type": "edible",
#         "img": "https://i0.wp.com/practicalselfreliance.com/wp-content/uploads/2021/05/Fireweed-Plant1-.jpg?resize=1200%2C1800&ssl=1",
#         "description":"Can eat seeds and flowers raw, and can cook the roots. It's best to eat leaves raw when they are young. The seeds can also be a firestarter!"
#     },
#           {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#             {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },
#     {
#         "name": "Beargrass",
#         "type": "medicinal",
#         "img": "https://www.fs.usda.gov/wildflowers/plant-of-the-week/images/beargrass/Xerophyllum_tenax1_Barbara_Mumblo.jpg",
#         "description": "While not edible, beargrass has traditional medicinal uses, such as poultices made from its roots to treat burns and insect bites."
#     },
#     {
#         "name": "Wild Mint",
#         "type": "medicinal",
#         "img": "https://eattheplanet.org/wp-content/uploads/2020/05/Mentha_canadensis_2.jpg",
#         "description": "Wild mint found in the park can be used to make a refreshing tea that helps in digestion and can relieve symptoms of colds and flu."
#     },
#                  {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#                                                              {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
#                                                                                          {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
#                                                                                          {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#                                                                                               {
#         "name": "Mormon Tea",
#         "type": "medicinal",
#        "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#         "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
#     },
#                                                                                                           {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },
#                                                                                                               {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."},
#     {
#         "name": "Raspberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
#         "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
#     },
#     {
#         "name": "Serviceberries",
#         "type": "edible",
#         "img": "https://www.gardenista.com/wp-content/uploads/2023/06/serviceberries-june-marie-viljoen.jpg",
#         "description": "Many people make the mistake of harvesting Amelanchier fruit while it’s still red. Red berries are certainly edible, but they are not fully ripe. Berries are at their best when they ripen to a dark, purple-blue. At this stage they are sweet, plump, and juicy. The fruit ripens gradually, over a period of weeks, so this will be a graduated harvest. "
#     },
#           {
#         "name": "Stinging nettle",
#         "type": "edible",
#         "img": "https://loganspader.com/wp-content/uploads/2022/08/stinging-nettle-plant-wild-edible-food-22-sss.jpg?strip=info&w=800",
#        "description": "Can be eaten raw, just watch out for the pricks."
#     },
# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
#                        {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#     {
#         "name": "Oregon Grape",
#         "type": "medicinal",
#         "img": "https://www.nps.gov/articles/000/images/B_aquifolium_Bruce_Newhouse_ORFloraProject_permission.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
#         "description": "The roots contain berberine, used as an antimicrobial agent. The berries are tart but edible and can be made into jellies or fermented into wine."
#     },
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
     
#         {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
# { "name": "Indian Ricegrass", "type": "edible", "img": "https://www.fs.usda.gov/wildflowers/plant-of-the-week/images/indianricegrass/achnatherum_hymenoides_Monroe.jpg", "description": "The seeds can be ground into flour and used to make bread or porridge." },

#                         {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },

# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
#                        {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
      
#      {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
# { "name": "Indian Ricegrass", "type": "edible", "img": "https://www.fs.usda.gov/wildflowers/plant-of-the-week/images/indianricegrass/achnatherum_hymenoides_Monroe.jpg", "description": "The seeds can be ground into flour and used to make bread or porridge." },

#                         {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },

# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
#                        {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
#                       {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },


     
#               "name": "Elderberries",
#         "type": "medicinal",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14801/content_c4-Image-by-Mark-Robinson.-Elderberries.jpg",
#         "description": "Berries and flowers are used in traditional remedies for immune support and to treat colds and flu. Berries must be cooked before consumption to avoid toxicity."},


# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
    
#     {
#         "name": "Beechnuts",
#         "type": "edible",
#         "img": "https://naturallycuriouswithmaryholland.wordpress.com/wp-content/uploads/2019/08/8-7-19-beechnuts-0u1a0160.jpg",
#         "description": "Beech nuts can taste bitter, astringent, or mild and nut-like. Some say they taste like a cross between a pine nut and a hazelnut."
#     },
#      {
#         "name": "Pawpaw",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Asimina_triloba3.jpg/440px-Asimina_triloba3.jpg",
#         "description": "Produces a large, yellowish-green fruit that is edible and has a custard-like taste. It is rich in nutrients and can be eaten raw or used in various recipes."
#     },
# { 
#  "name": "Chickweed", "type": "edible", "img": "https://media.greg.app/cGxhbnQtZGItcGhvdG9zL2NvbW1vbl9jaGlja3dlZWQuanBn?format=pjpeg&optimize=high&auto=webp&precrop=1000:1000,smart&fit=crop&width=1000&height=1000", "description": "The leaves, stems, and flowers of this plant are edible and are often used in salads or cooked."

# },

# { "name": "Echinacea (Purple Coneflower)", "type": "medicinal", "img": "https://ujamaaseeds.com/cdn/shop/products/ECHINACEAHERB_720x.jpg?v=1641132561", "description": "Known for boosting the immune system and fighting colds and infections." },

# { "name": "Black Cohosh", "type": "medicinal", "img": "https://assets.americanmeadows.com/media/catalog/product/b/l/black-cohosh-white-blooms.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Used traditionally to treat menstrual issues, menopause symptoms, and as a pain reliever." },

# { "name": "Bloodroot", "type": "medicinal", "img": "https://hort.extension.wisc.edu/files/2015/12/Sang_canad-habitat.jpg", "description": "Historically used to treat respiratory conditions and as a topical antiseptic." },
#   {
#         "name": "Wild Ginger",
#         "type": "edible",
#         "img": "https://www.eattheweeds.com/wp-content/uploads/2017/09/Asarum_canadense.jpg",
#         "description": "The roots can be used as a spice or brewed into a tea. It has been used to aid digestion and treat intestinal ailments."
#     },


# { "name": "Wild Grape", "type": "edible", "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy1_ZkAe70rryqG64rq0rCwMypV3hbGEvlVOLWMptj_BIzKBVhL9dZ8J7qG684mQwT06tB6dj3hsL-mATKNFEUyjJWX0M_S_MkP0cXy4SIL8JttjIPfx0FsZnZlKqI8FHdKHRu9LfjoL9n/s640/IMG_6376.JPG", "description": "Wild grapes are small, tart, and can be eaten fresh or used in jams and wines." },

#                        {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#                      {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#             {
#         "name": "Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },
#   {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
#                            {
#         "name": "Ocotillo",
#         "type": "medicinal",
#         "img": "https://m.media-amazon.com/images/I/811+ITLQT3L.jpg",
#         "description":"This plant is known for its ability to sprout leaves rapidly after rain. It has traditional medicinal uses, such as creating a soothing tea from its flowers to treat symptoms like coughs and chest congestion."
#     },
#     {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#                                                                                   {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
#                                        {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
# { "name": "Sotol", "type": "edible", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Dasylirion_wheeleri_1.jpg/220px-Dasylirion_wheeleri_1.jpg", "description": "The base of the plant is traditionally roasted and eaten. The stems can also be used to make a beverage." },

# { "name": "Agave", "type": "edible", "img": "https://www.penick.net/digging/images/2010_02_05_Wildflower%20Center/Agave_&_grasses_2.JPG", "description": "The heart of the agave can be roasted and eaten, while the sap is used to make sweeteners and beverages." },

# { "name": "Yerba Mansa", "type": "medicinal", "img": "https://strictlymedicinalseeds.com/wp-content/uploads/2017/08/yerba-mansa-Anemopsis-californica-seed-plant-3.jpg.bmp", "description": "Known for treating inflammation, wounds, and infections. It is used in teas for digestive and respiratory issues." },
#      {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },
#    {
#         "name": "Pawpaw",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Asimina_triloba3.jpg/440px-Asimina_triloba3.jpg",
#         "description": "Produces a large, yellowish-green fruit that is edible and has a custard-like taste. It is rich in nutrients and can be eaten raw or used in various recipes."
#     },
# { "name": "Persimmon", "type": "edible", "img": "https://www.isons.com/wp-content/uploads/2020/04/shutterstock_2195585-600x897.jpg", "description": "The fruit of the persimmon tree is sweet when fully ripe and can be eaten fresh or used in puddings and baked goods." },

# { "name": "Black Walnut", "type": "edible", "img": "https://files.nc.gov/parks/styles/event_image/public/images/2022-11/black-walnut-stone-mountain-j-mickey-16343.jpg?VersionId=8oELAZJwTPlI_poKUVSpq30dBwCxB3NU&itok=7fWbBoRz", "description": "The nuts can be harvested and eaten raw or roasted, providing a rich, nutty flavor." },
#               {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
# { "name": "Echinacea (Purple Coneflower)", "type": "medicinal", "img": "https://ujamaaseeds.com/cdn/shop/products/ECHINACEAHERB_720x.jpg?v=1641132561", "description": "Known for boosting the immune system and fighting colds and infections." },

# { "name": "Blackberry", "type": "edible", "img": "https://gardenerspath.com/wp-content/uploads/2021/05/Rubus-Lacinatus.jpeg", "description": "The fruit can be eaten. Used as a remedy for diarrhea and inflammation, the leaves and root bark can be made into a tea." },

#   {
#         "name": "Wild Ginger",
#         "type": "edible",
#         "img": "https://www.eattheweeds.com/wp-content/uploads/2017/09/Asarum_canadense.jpg",
#         "description": "The roots can be used as a spice or brewed into a tea. It has been used to aid digestion and treat intestinal ailments."
#     },

# { "name": "Sassafras", "type": "medicinal", "img": "https://www.thespruce.com/thmb/uABgqC7IwKzBBotVZ_87FgGMa0Y=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/sassafras-tree-plant-profile-5199214-hero-47efb45305de42398241eaeb9a0561d5.JPG", "description": "The roots and bark were traditionally used to treat colds, fevers, and as a blood purifier." },
     
     
# { "name": "Persimmon", "type": "edible", "img": "https://www.isons.com/wp-content/uploads/2020/04/shutterstock_2195585-600x897.jpg", "description": "The fruit of the persimmon tree is sweet when fully ripe and can be eaten fresh or used in puddings and baked goods." },

# { "name": "Blackberry", "type": "edible", "img": "https://gardenerspath.com/wp-content/uploads/2021/05/Rubus-Lacinatus.jpeg", "description": "The fruit can be eaten. Used as a remedy for diarrhea and inflammation, the leaves and root bark can be made into a tea." },

# { "name": "Pokeweed", "type": "edible", "img": "https://www.nwcb.wa.gov/images/weeds/pokeweed/_fullsize/Phytolacca_americana_naturalized_alien_-_Italy.jpg", "description": "The young shoots and leaves can be boiled and eaten like spinach. Care must be taken as the plant is toxic if not properly prepared." },
  
# { 
#  "name": "Chickweed", "type": "edible", "img": "https://media.greg.app/cGxhbnQtZGItcGhvdG9zL2NvbW1vbl9jaGlja3dlZWQuanBn?format=pjpeg&optimize=high&auto=webp&precrop=1000:1000,smart&fit=crop&width=1000&height=1000", "description": "The leaves, stems, and flowers of this plant are edible and are often used in salads or cooked."

# },

#                  {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
# { "name": "Sassafras", "type": "medicinal", "img": "https://www.thespruce.com/thmb/uABgqC7IwKzBBotVZ_87FgGMa0Y=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/sassafras-tree-plant-profile-5199214-hero-47efb45305de42398241eaeb9a0561d5.JPG", "description": "The roots and bark were traditionally used to treat colds, fevers, and as a blood purifier." },
#           {
#         "name": "Plantain",
#         "type": "medicinal",
#         "img": "https://weedid.missouri.edu/images/images_optimized/2455optimized.jpg",
#         "description": "Plantain leaves are known for their medicinal properties, particularly for treating skin irritations and wounds. They can be crushed and applied as a poultice directly to the skin to soothe inflammation."
#     },
#     {
#         "name": "Jewelweed",
#         "type": "medicinal",
#         "img": "https://www.adirondackalmanack.com/wp-content/uploads/2015/07/Jewelweed-540x702.jpg",
#         "description": "Known for treating skin irritations, such as poison ivy rashes. The leaves and juice from the stem are applied directly to the skin."
#     },
# { "name": "Echinacea (Purple Coneflower)", "type": "medicinal", "img": "https://ujamaaseeds.com/cdn/shop/products/ECHINACEAHERB_720x.jpg?v=1641132561", "description": "Known for boosting the immune system and fighting colds and infections." },

#  {
#         "name": "Blueberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14798/content_c1-Image-by-Tim-Rains_-of-Denali-National-Park-and-Preserve.-Droplets-of-Ice--Blueberry.-Denali-National-Park-and-Preserve.jpg",
#         "description": "Starting in July through August, diverse and delectable species of wild Maine blueberries are ripening. Acadia National park, with its ledges and naturally acidic soils are prime places to see these wild plants."},

#        {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."},

#     {
#         "name": "Raspberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
#         "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
#     },
#  {
#         "name": "Serviceberries",
#         "type": "edible",
#         "img": "https://www.gardenista.com/wp-content/uploads/2023/06/serviceberries-june-marie-viljoen.jpg",
#         "description": "Many people make the mistake of harvesting Amelanchier fruit while it’s still red. Red berries are certainly edible, but they are not fully ripe. Berries are at their best when they ripen to a dark, purple-blue. At this stage they are sweet, plump, and juicy. The fruit ripens gradually, over a period of weeks, so this will be a graduated harvest. "
#     },
#   {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },
#   {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },

#     {
#         "name": "Jewelweed",
#         "type": "medicinal",
#         "img": "https://www.adirondackalmanack.com/wp-content/uploads/2015/07/Jewelweed-540x702.jpg",
#         "description": "Known for treating skin irritations, such as poison ivy rashes. The leaves and juice from the stem are applied directly to the skin."
#     },
#     {
#         "name": "Wild Mint",
#         "type": "medicinal",
#         "img": "https://eattheplanet.org/wp-content/uploads/2020/05/Mentha_canadensis_2.jpg",
#         "description": "Wild mint found in the park can be used to make a refreshing tea that helps in digestion and can relieve symptoms of colds and flu."
#     },

# { "name": "Labrador Tea", "type": "medicinal", "img": "https://cdn.britannica.com/66/1966-004-44359187/Labrador-tea.jpg?w=400&h=300&c=crop", "description": "The leaves are brewed into a tea used to treat colds, sore throats, and respiratory issues." },

#  { "name": "Red Clover", "type": "medicinal", "img": "https://assets.americanmeadows.com/media/catalog/product/r/e/red-clover.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Used in teas to promote digestion, improve circulation, and as a remedy for respiratory issues." },
     
#                       {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#                                   {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
#       {
#         "name": "Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },

# { "name": "Joshua Tree Seeds", "type": "edible", "img": "https://ravenjake.typepad.com/.a/6a013486e82765970c01901b870b15970b-320wi", "description": "The seeds of the Joshua tree can be roasted and eaten. The young flower buds are also edible when cooked." },
#   {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#   {
#     "name": "Mormon Tea",
#     "type": "medicinal",
#     "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#     "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant."
# },

# { "name": "Black Oak Acorn", "type": "edible", "img": "https://extension.usu.edu/yardandgarden/images/branch-acorns-in-the-fall.jpg", "description": "Acorns from the black oak can be ground into flour after leaching the tannins, traditionally used to make breads or porridges." },

#      {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },

#                   {
#         "name": "Greenleaf Manzanita",
#         "type": "edible",
#         "img": "https://bloomcalifornia.org/wp-content/uploads/2021/09/arctostaphylos-glauca_big-berry-manzanita_inat-800.jpg",
#         "description":"It features simple, green leaves and reddish-brown bark. The plant produces pink, urn-shaped flowers in small clusters during spring, followed by green berries that turn rusty red when ripe. The seeds can be roasted or ground into flour, and the young shoots and leaves are also edible."
#     },
#    {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."
#     },
#                 {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
#                     {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },
#                 {
#         "name": "Greenleaf Manzanita",
#         "type": "edible",
#         "img": "https://bloomcalifornia.org/wp-content/uploads/2021/09/arctostaphylos-glauca_big-berry-manzanita_inat-800.jpg",
#         "description":"It features simple, green leaves and reddish-brown bark. The plant produces pink, urn-shaped flowers in small clusters during spring, followed by green berries that turn rusty red when ripe. The seeds can be roasted or ground into flour, and the young shoots and leaves are also edible."
#     },

#        {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#    {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },
# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },

#                 {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },

#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },

  
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },

# { "name": "Willow", "type": "medicinal", "img": "https://shop-static.arborday.org/media/0003288_weeping-willow_510.jpeg", "description": "Willow leaves can also be harvested for medicine in spring through summer and dried in baskets or paper bags. For tea, use 1 heaping tablespoon per cup of hot water and steep 15 minutes.Traditionally used for pain relief and to reduce fever." },
 
#  { "name": "Blackberry", "type": "edible", "img": "https://gardenerspath.com/wp-content/uploads/2021/05/Rubus-Lacinatus.jpeg", "description": "The fruit can be eaten. Used as a remedy for diarrhea and inflammation, the leaves and root bark can be made into a tea." },

#         {
#         "name": "Pawpaw",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Asimina_triloba3.jpg/440px-Asimina_triloba3.jpg",
#         "description": "Produces a large, yellowish-green fruit that is edible and has a custard-like taste. It is rich in nutrients and can be eaten raw or used in various recipes."
#     },
# { "name": "Persimmon", "type": "edible", "img": "https://www.isons.com/wp-content/uploads/2020/04/shutterstock_2195585-600x897.jpg", "description": "The fruit of the persimmon tree is sweet when fully ripe and can be eaten fresh or used in puddings and baked goods." },

# { "name": "Wild Grape", "type": "edible", "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy1_ZkAe70rryqG64rq0rCwMypV3hbGEvlVOLWMptj_BIzKBVhL9dZ8J7qG684mQwT06tB6dj3hsL-mATKNFEUyjJWX0M_S_MkP0cXy4SIL8JttjIPfx0FsZnZlKqI8FHdKHRu9LfjoL9n/s640/IMG_6376.JPG", "description": "Wild grapes are small, tart, and can be eaten fresh or used in jams and wines." },

# { 
#  "name": "Chickweed", "type": "edible", "img": "https://media.greg.app/cGxhbnQtZGItcGhvdG9zL2NvbW1vbl9jaGlja3dlZWQuanBn?format=pjpeg&optimize=high&auto=webp&precrop=1000:1000,smart&fit=crop&width=1000&height=1000", "description": "The leaves, stems, and flowers of this plant are edible and are often used in salads or cooked."

# },

#           {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
# { "name": "Sassafras", "type": "medicinal", "img": "https://www.thespruce.com/thmb/uABgqC7IwKzBBotVZ_87FgGMa0Y=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/sassafras-tree-plant-profile-5199214-hero-47efb45305de42398241eaeb9a0561d5.JPG", "description": "The roots and bark were traditionally used to treat colds, fevers, and as a blood purifier." },


# { "name": "Black Cohosh", "type": "medicinal", "img": "https://assets.americanmeadows.com/media/catalog/product/b/l/black-cohosh-white-blooms.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Used traditionally to treat menstrual issues, menopause symptoms, and as a pain reliever." },

# { "name": "Bloodroot", "type": "medicinal", "img": "https://hort.extension.wisc.edu/files/2015/12/Sang_canad-habitat.jpg", "description": "Historically used to treat respiratory conditions and as a topical antiseptic." },

# {"name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#         {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
 
#             {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
    
# { "name": "Indian Ricegrass", "type": "edible", "img": "https://www.fs.usda.gov/wildflowers/plant-of-the-week/images/indianricegrass/achnatherum_hymenoides_Monroe.jpg", "description": "The seeds can be ground into flour and used to make bread or porridge." },

#  {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#     {
#         "name": "Mormon Tea",
#         "type": "medicinal",
#         "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#         "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
#     },

#             {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },

# {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."},

#      {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },

#       {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#     {
#         "name": "Oregon Grape",
#         "type": "medicinal",
#         "img": "https://www.nps.gov/articles/000/images/B_aquifolium_Bruce_Newhouse_ORFloraProject_permission.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
#         "description": "The roots contain berberine, used as an antimicrobial agent. The berries are tart but edible and can be made into jellies or fermented into wine."
#     },
#     {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
    
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
  

# { "name": "Blackberry", "type": "edible", "img": "https://gardenerspath.com/wp-content/uploads/2021/05/Rubus-Lacinatus.jpeg", "description": "The fruit can be eaten. Used as a remedy for diarrhea and inflammation, the leaves and root bark can be made into a tea." },

#  {
#         "name": "Pawpaw",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Asimina_triloba3.jpg/440px-Asimina_triloba3.jpg",
#         "description": "Produces a large, yellowish-green fruit that is edible and has a custard-like taste. It is rich in nutrients and can be eaten raw or used in various recipes."
#     },


# { "name": "Wild Grape", "type": "edible", "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy1_ZkAe70rryqG64rq0rCwMypV3hbGEvlVOLWMptj_BIzKBVhL9dZ8J7qG684mQwT06tB6dj3hsL-mATKNFEUyjJWX0M_S_MkP0cXy4SIL8JttjIPfx0FsZnZlKqI8FHdKHRu9LfjoL9n/s640/IMG_6376.JPG", "description": "Wild grapes are small, tart, and can be eaten fresh or used in jams and wines." },

#   {
#         "name": "Beechnuts",
#         "type": "edible",
#         "img": "https://naturallycuriouswithmaryholland.wordpress.com/wp-content/uploads/2019/08/8-7-19-beechnuts-0u1a0160.jpg",
#         "description": "Beech nuts can taste bitter, astringent, or mild and nut-like. Some say they taste like a cross between a pine nut and a hazelnut."
#     },
# { "name": "Echinacea (Purple Coneflower)", "type": "medicinal", "img": "https://ujamaaseeds.com/cdn/shop/products/ECHINACEAHERB_720x.jpg?v=1641132561", "description": "Known for boosting the immune system and fighting colds and infections." },

# { "name": "Black Cohosh", "type": "medicinal", "img": "https://assets.americanmeadows.com/media/catalog/product/b/l/black-cohosh-white-blooms.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Used traditionally to treat menstrual issues, menopause symptoms, and as a pain reliever." },

# { "name": "Bloodroot", "type": "medicinal", "img": "https://hort.extension.wisc.edu/files/2015/12/Sang_canad-habitat.jpg", "description": "Historically used to treat respiratory conditions and as a topical antiseptic." },
 

# { "name": "Sassafras", "type": "medicinal", "img": "https://www.thespruce.com/thmb/uABgqC7IwKzBBotVZ_87FgGMa0Y=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/sassafras-tree-plant-profile-5199214-hero-47efb45305de42398241eaeb9a0561d5.JPG", "description": "The roots and bark were traditionally used to treat colds, fevers, and as a blood purifier." },
     

#                        {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#             {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },
#     {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."},
    
#    {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },
#  {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#            {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#    {
#         "name": "Oregon Grape",
#         "type": "medicinal",
#         "img": "https://www.nps.gov/articles/000/images/B_aquifolium_Bruce_Newhouse_ORFloraProject_permission.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
#         "description": "The roots contain berberine, used as an antimicrobial agent. The berries are tart but edible and can be made into jellies or fermented into wine."
#     },
#     {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
    
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
#               {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },
#     {
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."},
    
#    {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },

#            {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#    {
#         "name": "Oregon Grape",
#         "type": "medicinal",
#         "img": "https://www.nps.gov/articles/000/images/B_aquifolium_Bruce_Newhouse_ORFloraProject_permission.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
#         "description": "The roots contain berberine, used as an antimicrobial agent. The berries are tart but edible and can be made into jellies or fermented into wine."
#     },
#     {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
#                     {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#         {
#         "name": "Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },

#                                                              {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
# {
#         "name": "Cholla",
#         "type": "edible",
#         "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
#         "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
#     },
# {"name": "Saguaro Cactus", "type": "edible", "img": "https://media.istockphoto.com/id/1012796578/photo/mature-saguaro-cactus-fruit.jpg?s=612x612&w=0&k=20&c=yT19Rb8JkelEjdyDOc0tUfi1CTGlGqPT6rZEDdHD56g=", "description": "The fruit of the saguaro cactus can be eaten raw or used to make syrups, jams, or dried into fruit leather." },
   
#         {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
#            {
#         "name": "Mormon Tea",
#         "type": "medicinal",
#         "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#         "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant. "
#     },
#     {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },

#          {
#         "name": "Greenleaf Manzanita",
#         "type": "edible",
#         "img": "https://bloomcalifornia.org/wp-content/uploads/2021/09/arctostaphylos-glauca_big-berry-manzanita_inat-800.jpg",
#         "description":"It features simple, green leaves and reddish-brown bark. The plant produces pink, urn-shaped flowers in small clusters during spring, followed by green berries that turn rusty red when ripe. The seeds can be roasted or ground into flour, and the young shoots and leaves are also edible."
#     },
#     {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },


# { "name": "Wild Grape", "type": "edible", "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy1_ZkAe70rryqG64rq0rCwMypV3hbGEvlVOLWMptj_BIzKBVhL9dZ8J7qG684mQwT06tB6dj3hsL-mATKNFEUyjJWX0M_S_MkP0cXy4SIL8JttjIPfx0FsZnZlKqI8FHdKHRu9LfjoL9n/s640/IMG_6376.JPG", "description": "Wild grapes are small, tart, and can be eaten fresh or used in jams and wines." },

# { "name": "Black Oak Acorn", "type": "edible", "img": "https://extension.usu.edu/yardandgarden/images/branch-acorns-in-the-fall.jpg", "description": "Acorns from the black oak can be ground into flour after leaching the tannins, traditionally used to make breads or porridges." },


#        {
#         "name": "Elderberries",
#         "type": "medicinal",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14801/content_c4-Image-by-Mark-Robinson.-Elderberries.jpg",
#         "description": "Berries and flowers are used in traditional remedies for immune support and to treat colds and flu. Berries must be cooked before consumption to avoid toxicity."},
    
#                {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#     {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
# { "name": "Yerba Santa", "type": "medicinal", "img": "https://followingdeercreek.com/wp-content/uploads/2018/09/20180626_112948-600x600.jpg", "description": "Used to treat respiratory issues such as colds, bronchitis, and asthma. Often brewed as a tea." },

# { "name": "Mugwort", "type": "medicinal", "img": "https://www.thespruce.com/thmb/BtZ5LliZNMt80LIaCzDogW_KqQE=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/how-to-grow-mugwort-5077403-hero-75c95bdf02114d04b9e8325a62f7a7bc.JPG", "description": "Known for treating digestive disorders, insomnia, and anxiety. Mugwort is often brewed as a tea or used as a topical treatment." },

#  { "name": "California Bay Laurel", "type": "medicinal", "img": "https://www.fs.usda.gov/database/feis/plants/tree/umbcal/FlowerBuds.jpg", "description": "The leaves are used to treat headaches, sinus infections, and for pain relief. They can be brewed into tea or used in a steam bath." },

#             {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },

#           {                                                                                            
#         "name": "Thimbleberries",
#         "type": "edible",
#         "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
#         "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."},
    
#   {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },
#    {
#         "name": "Oregon Grape",
#         "type": "medicinal",
#         "img": "https://www.nps.gov/articles/000/images/B_aquifolium_Bruce_Newhouse_ORFloraProject_permission.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
#         "description": "The roots contain berberine, used as an antimicrobial agent. The berries are tart but edible and can be made into jellies or fermented into wine."
#     },
#               {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },

#  { "name": "California Bay Laurel", "type": "medicinal", "img": "https://www.fs.usda.gov/database/feis/plants/tree/umbcal/FlowerBuds.jpg", "description": "The leaves are used to treat headaches, sinus infections, and for pain relief. They can be brewed into tea or used in a steam bath." },


#   {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },

#       {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },
#     {
#         "name": "Serviceberries",
#         "type": "edible",
#         "img": "https://www.gardenista.com/wp-content/uploads/2023/06/serviceberries-june-marie-viljoen.jpg",
#         "description": "Many people make the mistake of harvesting Amelanchier fruit while it’s still red. Red berries are certainly edible, but they are not fully ripe. Berries are at their best when they ripen to a dark, purple-blue. At this stage they are sweet, plump, and juicy. The fruit ripens gradually, over a period of weeks, so this will be a graduated harvest. "
#     },
#     {
#         "name": "Raspberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
#         "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
#     },
# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
  
#              {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
  
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
       
# },

# { "name": "Willow", "type": "medicinal", "img": "https://shop-static.arborday.org/media/0003288_weeping-willow_510.jpeg", "description": "Willow leaves can also be harvested for medicine in spring through summer and dried in baskets or paper bags. For tea, use 1 heaping tablespoon per cup of hot water and steep 15 minutes.Traditionally used for pain relief and to reduce fever." },
 
#                 {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#     {
#         "name": "Cholla",
#         "type": "edible",
#         "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
#         "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
#     },
# {"name": "Saguaro Cactus", "type": "edible", "img": "https://media.istockphoto.com/id/1012796578/photo/mature-saguaro-cactus-fruit.jpg?s=612x612&w=0&k=20&c=yT19Rb8JkelEjdyDOc0tUfi1CTGlGqPT6rZEDdHD56g=", "description": "The fruit of the saguaro cactus can be eaten raw or used to make syrups, jams, or dried into fruit leather." },
   
#            {
#         "name": "Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },

# { "name": "Agave", "type": "edible", "img": "https://www.penick.net/digging/images/2010_02_05_Wildflower%20Center/Agave_&_grasses_2.JPG", "description": "The heart of the agave can be roasted and eaten, while the sap is used to make sweeteners and beverages." },

#                      {
#         "name": "Ocotillo",
#         "type": "medicinal",
#         "img": "https://m.media-amazon.com/images/I/811+ITLQT3L.jpg",
#         "description":"This plant is known for its ability to sprout leaves rapidly after rain. It has traditional medicinal uses, such as creating a soothing tea from its flowers to treat symptoms like coughs and chest congestion."
#     },
#     {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#   {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
# {
#     "name": "Mormon Tea",
#     "type": "medicinal",
#     "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#     "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant."
# },

# { "name": "Yerba Santa", "type": "medicinal", "img": "https://followingdeercreek.com/wp-content/uploads/2018/09/20180626_112948-600x600.jpg", "description": "Used to treat respiratory issues such as colds, bronchitis, and asthma. Often brewed as a tea." },


#                             {
#         "name": "Greenleaf Manzanita",
#         "type": "edible",
#         "img": "https://bloomcalifornia.org/wp-content/uploads/2021/09/arctostaphylos-glauca_big-berry-manzanita_inat-800.jpg",
#         "description":"It features simple, green leaves and reddish-brown bark. The plant produces pink, urn-shaped flowers in small clusters during spring, followed by green berries that turn rusty red when ripe. The seeds can be roasted or ground into flour, and the young shoots and leaves are also edible."
#     },
#      {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#    {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
 
# { "name": "Black Oak Acorn", "type": "edible", "img": "https://extension.usu.edu/yardandgarden/images/branch-acorns-in-the-fall.jpg", "description": "Acorns from the black oak can be ground into flour after leaching the tannins, traditionally used to make breads or porridges." },

#           {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#  {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
                    

#  { "name": "California Bay Laurel", "type": "medicinal", "img": "https://www.fs.usda.gov/database/feis/plants/tree/umbcal/FlowerBuds.jpg", "description": "The leaves are used to treat headaches, sinus infections, and for pain relief. They can be brewed into tea or used in a steam bath." },

# { "name": "Blackberry", "type": "edible", "img": "https://gardenerspath.com/wp-content/uploads/2021/05/Rubus-Lacinatus.jpeg", "description": "The fruit can be eaten. Used as a remedy for diarrhea and inflammation, the leaves and root bark can be made into a tea." },

#   {
#         "name": "Pawpaw",
#         "type": "edible",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Asimina_triloba3.jpg/440px-Asimina_triloba3.jpg",
#         "description": "Produces a large, yellowish-green fruit that is edible and has a custard-like taste. It is rich in nutrients and can be eaten raw or used in various recipes."
#     },
# { "name": "Persimmon", "type": "edible", "img": "https://www.isons.com/wp-content/uploads/2020/04/shutterstock_2195585-600x897.jpg", "description": "The fruit of the persimmon tree is sweet when fully ripe and can be eaten fresh or used in puddings and baked goods." },

# { "name": "Wild Grape", "type": "edible", "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy1_ZkAe70rryqG64rq0rCwMypV3hbGEvlVOLWMptj_BIzKBVhL9dZ8J7qG684mQwT06tB6dj3hsL-mATKNFEUyjJWX0M_S_MkP0cXy4SIL8JttjIPfx0FsZnZlKqI8FHdKHRu9LfjoL9n/s640/IMG_6376.JPG", "description": "Wild grapes are small, tart, and can be eaten fresh or used in jams and wines." },

# { 
#  "name": "Chickweed", "type": "edible", "img": "https://media.greg.app/cGxhbnQtZGItcGhvdG9zL2NvbW1vbl9jaGlja3dlZWQuanBn?format=pjpeg&optimize=high&auto=webp&precrop=1000:1000,smart&fit=crop&width=1000&height=1000", "description": "The leaves, stems, and flowers of this plant are edible and are often used in salads or cooked."

# },
#           {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
# { "name": "Sassafras", "type": "medicinal", "img": "https://www.thespruce.com/thmb/uABgqC7IwKzBBotVZ_87FgGMa0Y=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/sassafras-tree-plant-profile-5199214-hero-47efb45305de42398241eaeb9a0561d5.JPG", "description": "The roots and bark were traditionally used to treat colds, fevers, and as a blood purifier." },


# { "name": "Black Cohosh", "type": "medicinal", "img": "https://assets.americanmeadows.com/media/catalog/product/b/l/black-cohosh-white-blooms.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Used traditionally to treat menstrual issues, menopause symptoms, and as a pain reliever." },

# { "name": "Bloodroot", "type": "medicinal", "img": "https://hort.extension.wisc.edu/files/2015/12/Sang_canad-habitat.jpg", "description": "Historically used to treat respiratory conditions and as a topical antiseptic." },

# { 
# "name": "Chickweed", "type": "edible", "img": "https://media.greg.app/cGxhbnQtZGItcGhvdG9zL2NvbW1vbl9jaGlja3dlZWQuanBn?format=pjpeg&optimize=high&auto=webp&precrop=1000:1000,smart&fit=crop&width=1000&height=1000", "description": "The leaves, stems, and flowers of this plant are edible and are often used in salads or cooked."

# },

#                {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },

# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
            

# { "name": "Wild Plum", "type": "edible", "img": "https://magazine.outdoornebraska.gov/wp-content/uploads/2024/08/Wild-plum-at-Peterson-WMA-rgb.jpg", "description": "Small, sweet to tart plums that can be eaten fresh or used to make preserves, jellies, and syrups." },

# { "name": "Buffaloberry", "type": "edible", "img": "https://cdn11.bigcommerce.com/s-qttyo32dlj/images/stencil/550x400/products/916/2897/buffaloberry__47766.1632092586.jpg?c=2", "description": "Small, red or orange berries that are tart but edible. They can be eaten fresh or used in jams and jellies." },

#                 {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
# { "name": "Echinacea (Purple Coneflower)", "type": "medicinal", "img": "https://ujamaaseeds.com/cdn/shop/products/ECHINACEAHERB_720x.jpg?v=1641132561", "description": "Known for boosting the immune system and fighting colds and infections." },


#                                                                      {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
#     {
#         "name": "Blueberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14798/content_c1-Image-by-Tim-Rains_-of-Denali-National-Park-and-Preserve.-Droplets-of-Ice--Blueberry.-Denali-National-Park-and-Preserve.jpg",
#         "description": "Starting in July through August, diverse and delectable species of wild Maine blueberries are ripening. Acadia National park, with its ledges and naturally acidic soils are prime places to see these wild plants."},
    
#   {
#         "name": "Raspberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
#         "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
#     },
#   {
#         "name": "Serviceberries",
#         "type": "edible",
#         "img": "https://www.gardenista.com/wp-content/uploads/2023/06/serviceberries-june-marie-viljoen.jpg",
#         "description": "Many people make the mistake of harvesting Amelanchier fruit while it’s still red. Red berries are certainly edible, but they are not fully ripe. Berries are at their best when they ripen to a dark, purple-blue. At this stage they are sweet, plump, and juicy. The fruit ripens gradually, over a period of weeks, so this will be a graduated harvest. "
#     },
#   {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },
#                 {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#     {
#         "name": "Wild Mint",
#         "type": "medicinal",
#         "img": "https://eattheplanet.org/wp-content/uploads/2020/05/Mentha_canadensis_2.jpg",
#         "description": "Wild mint found in the park can be used to make a refreshing tea that helps in digestion and can relieve symptoms of colds and flu."
#     },

# { "name": "Labrador Tea", "type": "medicinal", "img": "https://cdn.britannica.com/66/1966-004-44359187/Labrador-tea.jpg?w=400&h=300&c=crop", "description": "The leaves are brewed into a tea used to treat colds, sore throats, and respiratory issues." },

# { "name": "Echinacea (Purple Coneflower)", "type": "medicinal", "img": "https://ujamaaseeds.com/cdn/shop/products/ECHINACEAHERB_720x.jpg?v=1641132561", "description": "Known for boosting the immune system and fighting colds and infections." },

#                                                               {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
#                                       {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
# { "name": "Sotol", "type": "edible", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Dasylirion_wheeleri_1.jpg/220px-Dasylirion_wheeleri_1.jpg", "description": "The base of the plant is traditionally roasted and eaten. The stems can also be used to make a beverage." },

# { "name": "Agave", "type": "edible", "img": "https://www.penick.net/digging/images/2010_02_05_Wildflower%20Center/Agave_&_grasses_2.JPG", "description": "The heart of the agave can be roasted and eaten, while the sap is used to make sweeteners and beverages." },


#                      {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#             {
#         "name": "Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },
#   {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
#    {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
# {
#  "name": "Yerba Santa", "type": "medicinal", "img": "https://followingdeercreek.com/wp-content/uploads/2018/09/20180626_112948-600x600.jpg", "description": "Used to treat respiratory issues such as colds, bronchitis, and asthma. Often brewed as a tea." },
#  {
#     "name": "Mormon Tea",
#     "type": "medicinal",
#     "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#     "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant."
# },


# { "name": "Wild Plum", "type": "edible", "img": "https://magazine.outdoornebraska.gov/wp-content/uploads/2024/08/Wild-plum-at-Peterson-WMA-rgb.jpg", "description": "Small, sweet to tart plums that can be eaten fresh or used to make preserves, jellies, and syrups." },

# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
   
# { "name": "Buffaloberry", "type": "edible", "img": "https://cdn11.bigcommerce.com/s-qttyo32dlj/images/stencil/550x400/products/916/2897/buffaloberry__47766.1632092586.jpg?c=2", "description": "Small, red or orange berries that are tart but edible. They can be eaten fresh or used in jams and jellies." },

#           {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#   {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
# { "name": "Echinacea (Purple Coneflower)", "type": "medicinal", "img": "https://ujamaaseeds.com/cdn/shop/products/ECHINACEAHERB_720x.jpg?v=1641132561", "description": "Known for boosting the immune system and fighting colds and infections." },


# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
     
  
    
#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
#            {
#         "name": "Huckleberry",
#         "type": "edible",
#         "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
#         "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
#     },
#  {
#         "name": "Raspberries",
#         "type": "edible",
#         "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
#         "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
#     },
#     {
#         "name": "Serviceberries",
#         "type": "edible",
#         "img": "https://www.gardenista.com/wp-content/uploads/2023/06/serviceberries-june-marie-viljoen.jpg",
#         "description": "Many people make the mistake of harvesting Amelanchier fruit while it’s still red. Red berries are certainly edible, but they are not fully ripe. Berries are at their best when they ripen to a dark, purple-blue. At this stage they are sweet, plump, and juicy. The fruit ripens gradually, over a period of weeks, so this will be a graduated harvest. "
#     },

# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
  

    
# { "name": "Arnica", "type": "medicinal", "img": "https://bcinvasives.ca/wp-content/uploads/2021/05/Heart-leaved-arnica-002_Arnica-cordifolia_ME-Harte_Bugwood.org_-600x400.jpg.webp", "description": "Commonly used externally for bruises, sprains, and muscle pain." },
     
#      {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
#  {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
#              {
#         "name": "Juniper Berries",
#         "type": "medicinal",
#         "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
#         "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
#     },
#               {
#         "name": "Greenleaf Manzanita",
#         "type": "edible",
#         "img": "https://bloomcalifornia.org/wp-content/uploads/2021/09/arctostaphylos-glauca_big-berry-manzanita_inat-800.jpg",
#         "description":"It features simple, green leaves and reddish-brown bark. The plant produces pink, urn-shaped flowers in small clusters during spring, followed by green berries that turn rusty red when ripe. The seeds can be roasted or ground into flour, and the young shoots and leaves are also edible."
#     },
#                    {
#         "name": "Yarrow",
#         "type": "medicinal",
#         "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
#         "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
#     },
#   {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },

#          {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
    
# { "name": "Chokecherry", "type": "edible", "img": "https://assets.highcountrygardens.com/media/catalog/product/c/h/chokeberry-aronia-melanocarpa-viking-cropped_2.jpg?quality=85&fit=bounds&height=&width=1080&auto=webp&format=pjpg", "description": "Tart berries best used for syrups or jams." },
   
#    {
#         "name": "Wild Strawberry",
#         "type": "edible",
#         "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
#         "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
#     },

#  { "name": "California Bay Laurel", "type": "medicinal", "img": "https://www.fs.usda.gov/database/feis/plants/tree/umbcal/FlowerBuds.jpg", "description": "The leaves are used to treat headaches, sinus infections, and for pain relief. They can be brewed into tea or used in a steam bath." },

#  {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },

#   {
#         "name": "Mullein",
#         "type": "medicinal",
#         "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
#         "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
#     },
#              {
#         "name": "Prickly Pear",
#         "type": "edible",
#         "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
#         "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
#     },
#         {
#         "name": "Pinyon nut",
#         "type": "edible",
#         "img": "https://treenm.org/wp-content/uploads/2022/08/Pinyon-Pine-UNM02.jpeg",
#         "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
#     },
#            {
#         "name": "Mesquite",
#         "type": "edible",
#         "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
#         "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
#     },
#    {
#         "name": "Cholla",
#         "type": "edible",
#         "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
#         "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
#     },
#                                                              {
#         "name": "Yucca",
#         "type": "medicinal",
#         "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
#         "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
#     },
#                                                                                              {
#         "name": "Mormon Tea",
#         "type": "medicinal",
#        "img": "https://cdn.britannica.com/89/123089-050-1C068220/Joint-pine.jpg?w=300",
#         "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
#     },

#   {
#         "name": "Creosote bush",
#         "type": "medicinal",   
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
#         "description":"It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
#     },
#     {
#         "name": "Sagebrush",
#         "type": "medicinal",
#         "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
#         "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
#     },
# { "name": "Yerba Santa", "type": "medicinal", "img": "https://followingdeercreek.com/wp-content/uploads/2018/09/20180626_112948-600x600.jpg", "description": "Used to treat respiratory issues such as colds, bronchitis, and asthma. Often brewed as a tea." },


# Run the seed script inside the application context
with app.app_context():
    # Optionally, clear the existing data if necessary
    db.session.query(Plant).delete()

    # Add plants to the database
    for plant in plants:
        try:
            new_plant = Plant(
                name=plant['name'],
                type=plant['type'],
                img=plant['img'],
                description=plant.get('description', 'No description provided')  # Use a default value if 'description' is missing
            )
            db.session.add(new_plant)
        except KeyError as e:
            print(f"Skipping plant due to missing key: {e},")
    
    # Commit changes to the database
    db.session.commit()
print("Plants have been added to the database.")

parks = [
    {"name": "Acadia", "state": "ME"},
    {"name": "Arches", "state": "UT"},
    {"name": "Badlands", "state": "SD"},
    {"name": "Big Bend", "state": "TX"},
    {"name": "Biscayne", "state": "FL"},
    {"name": "Black Canyon of the Gunnison", "state": "CO"},
    {"name": "Bryce Canyon", "state": "UT"},
    {"name": "Canyonlands", "state": "UT"},
    {"name": "Capitol Reef", "state": "UT"},
    {"name": "Carlsbad Caverns", "state": "NM"},
    {"name": "Channel Islands", "state": "CA"},
    {"name": "Congaree", "state": "SC"},
    {"name": "Crater Lake", "state": "OR"},
    {"name": "Cuyahoga Valley", "state": "OH"},
    {"name": "Death Valley", "state": "CA"},
    {"name": "Dry Tortugas", "state": "FL"},
    {"name": "Everglades", "state": "FL"},
    {"name": "Gateway Arch", "state": "MO"},
    {"name": "Glacier", "state": "MT"},
    {"name": "Grand Canyon", "state": "AZ"},
    {"name": "Grand Teton", "state": "WY"},
    {"name": "Great Basin", "state": "NV"},
    {"name": "Great Sand Dunes", "state": "CO"},
    {"name": "Great Smoky Mountains", "state": "NC"},
    {"name": "Guadalupe Mountains", "state": "TX"},
    {"name": "Hot Springs", "state": "AR"},
    {"name": "Indiana Dunes", "state": "IN"},
    {"name": "Isle Royale", "state": "MI"},
    {"name": "Joshua Tree", "state": "CA"},
    {"name": "Kings Canyon", "state": "CA"},
    {"name": "Lassen Volcanic", "state": "CA"},
    {"name": "Mammoth Cave", "state": "KY"},
    {"name": "Mesa Verde", "state": "CO"},
    {"name": "Mount Rainier", "state": "WA"},
    {"name": "New River Gorge", "state": "WV"},
    {"name": "North Cascades", "state": "WA"},
    {"name": "Olympic", "state": "WA"},
    {"name": "Petrified Forest", "state": "AZ"},
    {"name": "Pinnacles", "state": "CA"},
    {"name": "Redwood", "state": "CA"},
    {"name": "Rocky Mountain", "state": "CO"},
    {"name": "Saguaro", "state": "AZ"},
    {"name": "Sequoia", "state": "CA"},
    {"name": "Shenandoah", "state": "VA"},
    {"name": "Theodore Roosevelt", "state": "ND"},
    {"name": "White Sands", "state": "NM"},
    {"name": "Wind Cave", "state": "SD"},
    {"name": "Yellowstone", "state": "WY"},
    {"name": "Yosemite", "state": "CA"},
    {"name": "Zion", "state": "UT"},
    {"name": "Voyageurs", "state": "MN"}
]

# Move all database operations inside the app context
with app.app_context():
    # Optionally, clear the existing data if necessary
    print("Deleting data...")
    db.session.query(National_Park).delete()

    # Add parks to the database
    for park in parks:
        national_park = National_Park(name=park['name'], state=park['state'])
        db.session.add(national_park)

    # Commit changes to the database
    db.session.commit()
    print("National Parks have been added to the database.")

    

print("creating join table entries!")

plant_park_associations = [
    {'plant_id': 1, 'park_id': 1},
    {'plant_id': 2, 'park_id': 1},
    {'plant_id': 3, 'park_id': 1},
    {'plant_id': 4, 'park_id': 1},
    {'plant_id': 5, 'park_id': 1},
    {'plant_id': 6, 'park_id': 1},
    {'plant_id': 7, 'park_id': 2},
    {'plant_id': 8, 'park_id': 2},
    {'plant_id': 9, 'park_id': 2},
    {'plant_id': 10, 'park_id': 2},
    {'plant_id': 11, 'park_id': 2},
    {'plant_id': 12, 'park_id': 2},
    {'plant_id': 13, 'park_id': 3},
    {'plant_id': 14, 'park_id': 3},
    {'plant_id': 15, 'park_id': 3},
    {'plant_id': 16, 'park_id': 3},
    {'plant_id': 17, 'park_id': 3},
    {'plant_id': 18, 'park_id': 3},
    {'plant_id': 19, 'park_id': 4},
    {'plant_id': 20, 'park_id': 4},
    {'plant_id': 21, 'park_id': 4},
    {'plant_id': 22, 'park_id': 4},
    {'plant_id': 23, 'park_id': 4},
    {'plant_id': 24, 'park_id': 4},
    {'plant_id': 25, 'park_id': 4},
    {'plant_id': 26, 'park_id': 5},
    {'plant_id': 27, 'park_id': 5},
    {'plant_id': 28, 'park_id': 5},
    {'plant_id': 29, 'park_id': 5},
    {'plant_id': 30, 'park_id': 5},
    {'plant_id': 31, 'park_id': 5},
    {'plant_id': 32, 'park_id': 5},
    {'plant_id': 33, 'park_id': 6},
    {'plant_id': 34, 'park_id': 6},
    {'plant_id': 35, 'park_id': 6},
    {'plant_id': 36, 'park_id': 6},
    {'plant_id': 37, 'park_id': 6},
    {'plant_id': 38, 'park_id': 6},
    {'plant_id': 39, 'park_id': 7},
    {'plant_id': 40, 'park_id': 7},
    {'plant_id': 41, 'park_id': 7},
    {'plant_id': 42, 'park_id': 7},
    {'plant_id': 43, 'park_id': 7},
    {'plant_id': 44, 'park_id': 7},
    {'plant_id': 45, 'park_id': 8},
    {'plant_id': 46, 'park_id': 8},
    {'plant_id': 47, 'park_id': 8},
    {'plant_id': 48, 'park_id': 8},
    {'plant_id': 49, 'park_id': 8},
    {'plant_id': 50, 'park_id': 8},
    {'plant_id': 51, 'park_id': 9},
    {'plant_id': 52, 'park_id': 9},
    {'plant_id': 53, 'park_id': 9},
    {'plant_id': 54, 'park_id': 9},
    {'plant_id': 55, 'park_id': 9},
    {'plant_id': 56, 'park_id': 9},
    {'plant_id': 57, 'park_id': 10},
    {'plant_id': 58, 'park_id': 10},
    {'plant_id': 59, 'park_id': 10},
    {'plant_id': 60, 'park_id': 10},
    {'plant_id': 61, 'park_id': 10},
    {'plant_id': 62, 'park_id': 10},
    {'plant_id': 63, 'park_id': 11},
    {'plant_id': 64, 'park_id': 11},
    {'plant_id': 65, 'park_id': 11},
    {'plant_id': 66, 'park_id': 11},
    {'plant_id': 67, 'park_id': 11},
    {'plant_id': 68, 'park_id': 11},
    {'plant_id': 69, 'park_id': 12},
    {'plant_id': 70, 'park_id': 12},
    {'plant_id': 71, 'park_id': 12},
    {'plant_id': 72, 'park_id': 12},
    {'plant_id': 73, 'park_id': 12},
    {'plant_id': 74, 'park_id': 12},
    {'plant_id': 75, 'park_id': 13},
    {'plant_id': 76, 'park_id': 13},
    {'plant_id': 77, 'park_id': 13},
    {'plant_id': 78, 'park_id': 13},
    {'plant_id': 79, 'park_id': 13},
    {'plant_id': 80, 'park_id': 13},
    {'plant_id': 81, 'park_id': 14},
    {'plant_id': 82, 'park_id': 14},
    {'plant_id': 83, 'park_id': 14},
    {'plant_id': 84, 'park_id': 14},
    {'plant_id': 85, 'park_id': 14},
    {'plant_id': 86, 'park_id': 14},
    {'plant_id': 87, 'park_id': 15},
    {'plant_id': 88, 'park_id': 15},
    {'plant_id': 89, 'park_id': 15},
    {'plant_id': 90, 'park_id': 15},
    {'plant_id': 91, 'park_id': 15},
    {'plant_id': 92, 'park_id': 15},
    {'plant_id': 93, 'park_id': 16},
    {'plant_id': 94, 'park_id': 16},
    {'plant_id': 95, 'park_id': 16},
    {'plant_id': 96, 'park_id': 16},
    {'plant_id': 97, 'park_id': 16},
    {'plant_id': 98, 'park_id': 16},
    {'plant_id': 99, 'park_id': 17},
    {'plant_id': 100, 'park_id': 17},
    {'plant_id': 101, 'park_id': 17},
    {'plant_id': 102, 'park_id': 17},
    {'plant_id': 103, 'park_id': 17},
    {'plant_id': 104, 'park_id': 17},
    {'plant_id': 105, 'park_id': 17},
    {'plant_id': 106, 'park_id': 18},
    {'plant_id': 107, 'park_id': 18},
    {'plant_id': 108, 'park_id': 18},
    {'plant_id': 109, 'park_id': 18},
    {'plant_id': 110, 'park_id': 18},
    {'plant_id': 111, 'park_id': 18},
    {'plant_id': 112, 'park_id': 19},
    {'plant_id': 113, 'park_id': 19},
    {'plant_id': 114, 'park_id': 19},
    {'plant_id': 115, 'park_id': 19},
    {'plant_id': 116, 'park_id': 19},
    {'plant_id': 117, 'park_id': 19},
    {'plant_id': 118, 'park_id': 20},
    {'plant_id': 119, 'park_id': 20},
    {'plant_id': 120, 'park_id': 20},
    {'plant_id': 121, 'park_id': 20},
    {'plant_id': 122, 'park_id': 20},
    {'plant_id': 123, 'park_id': 20},
    {'plant_id': 124, 'park_id': 21},
    {'plant_id': 125, 'park_id': 21},
    {'plant_id': 126, 'park_id': 21},
    {'plant_id': 127, 'park_id': 21},
    {'plant_id': 128, 'park_id': 21},
    {'plant_id': 129, 'park_id': 21},
    {'plant_id': 130, 'park_id': 22},
    {'plant_id': 131, 'park_id': 22},
    {'plant_id': 132, 'park_id': 22},
    {'plant_id': 133, 'park_id': 22},
    {'plant_id': 134, 'park_id': 22},
    {'plant_id': 135, 'park_id': 22},
    {'plant_id': 136, 'park_id': 23},
    {'plant_id': 137, 'park_id': 23},
    {'plant_id': 138, 'park_id': 23},
    {'plant_id': 139, 'park_id': 23},
    {'plant_id': 140, 'park_id': 23},
    {'plant_id': 141, 'park_id': 23},
    {'plant_id': 142, 'park_id': 24},
    {'plant_id': 143, 'park_id': 24},
    {'plant_id': 144, 'park_id': 24},
    {'plant_id': 145, 'park_id': 24},
    {'plant_id': 146, 'park_id': 24},
    {'plant_id': 147, 'park_id': 24},
    {'plant_id': 148, 'park_id': 24},
    {'plant_id': 149, 'park_id': 25},
    {'plant_id': 150, 'park_id': 25},
    {'plant_id': 151, 'park_id': 25},
    {'plant_id': 152, 'park_id': 25},
    {'plant_id': 153, 'park_id': 25},
    {'plant_id': 154, 'park_id': 25},
    {'plant_id': 155, 'park_id': 25},
    {'plant_id': 156, 'park_id': 26},
    {'plant_id': 157, 'park_id': 26},
    {'plant_id': 158, 'park_id': 26},
    {'plant_id': 159, 'park_id': 26},
    {'plant_id': 160, 'park_id': 26},
    {'plant_id': 161, 'park_id': 26},
    {'plant_id': 162, 'park_id': 27},
    {'plant_id': 163, 'park_id': 27},
    {'plant_id': 164, 'park_id': 27},
    {'plant_id': 165, 'park_id': 27},
    {'plant_id': 166, 'park_id': 27},
    {'plant_id': 167, 'park_id': 27},
    {'plant_id': 168, 'park_id': 28},
    {'plant_id': 169, 'park_id': 28},
    {'plant_id': 170, 'park_id': 28},
    {'plant_id': 171, 'park_id': 28},
    {'plant_id': 172, 'park_id': 28},
    {'plant_id': 173, 'park_id': 28},
    {'plant_id': 174, 'park_id': 29},
    {'plant_id': 175, 'park_id': 29},
    {'plant_id': 176, 'park_id': 29},
    {'plant_id': 177, 'park_id': 29},
    {'plant_id': 178, 'park_id': 29},
    {'plant_id': 179, 'park_id': 29},
    {'plant_id': 180, 'park_id': 29},
    {'plant_id': 181, 'park_id': 30},
    {'plant_id': 182, 'park_id': 30},
    {'plant_id': 183, 'park_id': 30},
    {'plant_id': 184, 'park_id': 30},
    {'plant_id': 185, 'park_id': 30},
    {'plant_id': 186, 'park_id': 30},
    {'plant_id': 187, 'park_id': 30},
    {'plant_id': 188, 'park_id': 31},
    {'plant_id': 189, 'park_id': 31},
    {'plant_id': 190, 'park_id': 31},
    {'plant_id': 191, 'park_id': 31},
    {'plant_id': 192, 'park_id': 31},
    {'plant_id': 193, 'park_id': 31},
    {'plant_id': 194, 'park_id': 32},
    {'plant_id': 195, 'park_id': 32},
    {'plant_id': 196, 'park_id': 32},
    {'plant_id': 197, 'park_id': 32},
    {'plant_id': 198, 'park_id': 32},
    {'plant_id': 199, 'park_id': 32},
    {'plant_id': 200, 'park_id': 32},
    {'plant_id': 201, 'park_id': 33},
    {'plant_id': 202, 'park_id': 33},
    {'plant_id': 203, 'park_id': 33},
    {'plant_id': 204, 'park_id': 33},
    {'plant_id': 205, 'park_id': 33},
    {'plant_id': 206, 'park_id': 33},
    {'plant_id': 207, 'park_id': 34},
    {'plant_id': 208, 'park_id': 34},
    {'plant_id': 209, 'park_id': 34},
    {'plant_id': 210, 'park_id': 34},
    {'plant_id': 211, 'park_id': 34},
    {'plant_id': 212, 'park_id': 34},
    {'plant_id': 213, 'park_id': 34},
    {'plant_id': 214, 'park_id': 35},
    {'plant_id': 215, 'park_id': 35},
    {'plant_id': 216, 'park_id': 35},
    {'plant_id': 217, 'park_id': 35},
    {'plant_id': 218, 'park_id': 35},
    {'plant_id': 219, 'park_id': 35},
    {'plant_id': 220, 'park_id': 36},
    {'plant_id': 221, 'park_id': 36},
    {'plant_id': 222, 'park_id': 36},
    {'plant_id': 223, 'park_id': 36},
    {'plant_id': 224, 'park_id': 36},
    {'plant_id': 225, 'park_id': 36},
    {'plant_id': 226, 'park_id': 37},
    {'plant_id': 227, 'park_id': 37},
    {'plant_id': 228, 'park_id': 37},
    {'plant_id': 229, 'park_id': 37},
    {'plant_id': 230, 'park_id': 37},
    {'plant_id': 231, 'park_id': 37},
    {'plant_id': 232, 'park_id': 38},
    {'plant_id': 233, 'park_id': 38},
    {'plant_id': 234, 'park_id': 38},
    {'plant_id': 235, 'park_id': 38},
    {'plant_id': 236, 'park_id': 38},
    {'plant_id': 237, 'park_id': 38},
    {'plant_id': 238, 'park_id': 39},
    {'plant_id': 239, 'park_id': 39},
    {'plant_id': 240, 'park_id': 39},
    {'plant_id': 241, 'park_id': 39},
    {'plant_id': 242, 'park_id': 39},
    {'plant_id': 243, 'park_id': 39},
    {'plant_id': 244, 'park_id': 40},
    {'plant_id': 245, 'park_id': 40},
    {'plant_id': 246, 'park_id': 40},
    {'plant_id': 247, 'park_id': 40},
    {'plant_id': 248, 'park_id': 40},
    {'plant_id': 249, 'park_id': 40},
    {'plant_id': 250, 'park_id': 41},
    {'plant_id': 251, 'park_id': 41},
    {'plant_id': 252, 'park_id': 41},
    {'plant_id': 253, 'park_id': 41},
    {'plant_id': 254, 'park_id': 41},
    {'plant_id': 255, 'park_id': 41},
    {'plant_id': 256, 'park_id': 41},
    {'plant_id': 257, 'park_id': 42},
    {'plant_id': 258, 'park_id': 42},
    {'plant_id': 259, 'park_id': 42},
    {'plant_id': 260, 'park_id': 42},
    {'plant_id': 261, 'park_id': 42},
    {'plant_id': 262, 'park_id': 42},
    {'plant_id': 263, 'park_id': 42},
    {'plant_id': 264, 'park_id': 43},
    {'plant_id': 265, 'park_id': 43},
    {'plant_id': 266, 'park_id': 43},
    {'plant_id': 267, 'park_id': 43},
    {'plant_id': 268, 'park_id': 43},
    {'plant_id': 269, 'park_id': 43},
    {'plant_id': 270, 'park_id': 43},
    {'plant_id': 271, 'park_id': 44},
    {'plant_id': 272, 'park_id': 44},
    {'plant_id': 273, 'park_id': 44},
    {'plant_id': 274, 'park_id': 44},
    {'plant_id': 275, 'park_id': 44},
    {'plant_id': 276, 'park_id': 44},
    {'plant_id': 277, 'park_id': 44},
    {'plant_id': 278, 'park_id': 45},
    {'plant_id': 279, 'park_id': 45},
    {'plant_id': 280, 'park_id': 45},
    {'plant_id': 281, 'park_id': 45},
    {'plant_id': 282, 'park_id': 45},
    {'plant_id': 283, 'park_id': 45},
    {'plant_id': 284, 'park_id': 46},
    {'plant_id': 285, 'park_id': 46},
    {'plant_id': 286, 'park_id': 46},
    {'plant_id': 287, 'park_id': 46},
    {'plant_id': 288, 'park_id': 46},
    {'plant_id': 289, 'park_id': 46},
    {'plant_id': 290, 'park_id': 47},
    {'plant_id': 291, 'park_id': 47},
    {'plant_id': 292, 'park_id': 47},
    {'plant_id': 293, 'park_id': 47},
    {'plant_id': 294, 'park_id': 47},
    {'plant_id': 295, 'park_id': 47},
    {'plant_id': 296, 'park_id': 48},
    {'plant_id': 297, 'park_id': 48},
    {'plant_id': 298, 'park_id': 48},
    {'plant_id': 299, 'park_id': 48},
    {'plant_id': 300, 'park_id': 48},
    {'plant_id': 301, 'park_id': 48},
    {'plant_id': 302, 'park_id': 49},
    {'plant_id': 303, 'park_id': 49},
    {'plant_id': 304, 'park_id': 49},
    {'plant_id': 305, 'park_id': 49},
    {'plant_id': 306, 'park_id': 49},
    {'plant_id': 307, 'park_id': 49},
    {'plant_id': 308, 'park_id': 49},
    {'plant_id': 309, 'park_id': 50},
    {'plant_id': 310, 'park_id': 50},
    {'plant_id': 311, 'park_id': 50},
    {'plant_id': 312, 'park_id': 50},
    {'plant_id': 313, 'park_id': 50},
    {'plant_id': 314, 'park_id': 50},
    {'plant_id': 315, 'park_id': 50},
    {'plant_id': 316, 'park_id': 51},
    {'plant_id': 317, 'park_id': 51},
    {'plant_id': 318, 'park_id': 51},
    {'plant_id': 319, 'park_id': 51},
    {'plant_id': 320, 'park_id': 51},
    {'plant_id': 321, 'park_id': 51}
]

with app.app_context():
    # Iterate over each plant-park association and add to the database
    for association in plant_park_associations:
        plant_np_join = Plant_NP_Join(plant_id=association['plant_id'], national_park_id=association['park_id'])
        db.session.add(plant_np_join)

    # Commit the join table entries
    db.session.commit()
    print("Plant-National Park associations have been added.")

