from config import app
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
plants = [
    {
        "name": "Japanese Knotweed",
        "type": "edible",
        "img": "https://cdn.britannica.com/45/246545-050-677C999F/Japanese-knotweed-plant.jpg",
        "description": "Once established, this perennial herbaceous plant can grow up to 10 feet in one growing season. Its young shoots are the most consumed part, as they are tender and have a tart flavor reminiscent of rhubarb."}
    {
        "name": "Garlic Mustard",
        "type": "edible",
        "img": "data:image/jpeg;base64,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",}
        "description": "Garlic mustard is a biennial, which means it produces seed on its second year that spreads by seed dispersal and can grow up to six feet tall. It’s best to harvest when the plant is younger and only eat the leaves."
    {
        "name": "Blueberries",
        "type": "edible",
        "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14798/content_c1-Image-by-Tim-Rains_-of-Denali-National-Park-and-Preserve.-Droplets-of-Ice--Blueberry.-Denali-National-Park-and-Preserve.jpg",
        "description": "Starting in July through August, diverse and delectable species of wild Maine blueberries are ripening. Acadia National park, with its ledges and naturally acidic soils are prime places to see these wild plants."}
    {
        "name": "Serviceberries",
        "type": "edible",
        "img": "https://www.gardenista.com/wp-content/uploads/2023/06/serviceberries-june-marie-viljoen.jpg",
        "description": "Many people make the mistake of harvesting Amelanchier fruit while it’s still red. Red berries are certainly edible, but they are not fully ripe. Berries are at their best when they ripen to a dark, purple-blue. At this stage they are sweet, plump, and juicy. The fruit ripens gradually, over a period of weeks, so this will be a graduated harvest. "
    }

       {
        "name": "Thimbleberries",
        "type": "edible",
        "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
        "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."}
    {
        "name": "Raspberries",
        "type": "edible",
        "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
        "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
    }
     {
        "name": "Red Currants",
        "type": "medicinal",
        "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14800/content_c3-Image-by-Emilie-Barbier.-Wild-Red-Currant.jpg",
        "description": "Red currants are small, round, and almost spherical, with a translucent skin that can sometimes show the pips inside. They have ribs that resemble lines of longitude on a globe. Red currants have a tart flavor due to their high content of organic acids and polyphenols."
    }
       {
        "name": "Elderberries",
        "type": "medicinal",
        "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14801/content_c4-Image-by-Mark-Robinson.-Elderberries.jpg",
        "description": "Berries and flowers are used in traditional remedies for immune support and to treat colds and flu. Berries must be cooked before consumption to avoid toxicity."}
    {
        "name": "Hickory Nuts",
        "type": "edible",
        "img": "https://www.mossyoak.com/sites/default/files/inline-images/green-hickory-nuts.jpg",
        "description": "Hickory nuts can taste sweet, dense, and rich, and some say they taste better than pecans or walnuts. However, the taste varies by species, with some being bitter. For example, bitternut hickory nuts are so bitter that many squirrels avoid them."
    }
       {
        "name": "Chestnuts",
        "type": "edible",
        "img": "https://cdn.britannica.com/92/182092-050-114F4DA5/European-chestnut.jpg?w=400&h=300&c=crop",
        "description": "Chestnuts grow inside a spiky husk that splits open when the nuts are mature. The number of nuts in a husk depends on the species, but it's usually one to seven. The nuts are edible and have been a vital food source for rural populations, especially in the winter"}
    {
        "name": "Beechnuts",
        "type": "edible",
        "img": "https://naturallycuriouswithmaryholland.wordpress.com/wp-content/uploads/2019/08/8-7-19-beechnuts-0u1a0160.jpg",
        "description": "Beech nuts can taste bitter, astringent, or mild and nut-like. Some say they taste like a cross between a pine nut and a hazelnut."
    }
    
      {
        "name": "Fiddlehead",
        "type": "edible",
        "img": "https://www.recordonline.com/gcdn/authoring/2017/03/18/NTHR/ghows-TH-4acb951e-3b2d-42d3-e053-0100007f6645-c481c407.jpeg",
        "description": "Do not eat this plant raw, if you can make a fire, you should cook for at least 5 minutes. The spring plant peaks in May and the sprouts are generally foraged or picked from late April to early June before the plant grows into a fiddlehead fern."
    }
        {
        "name": "Sweetgrass",   
        "type": "medicinal",
        "img": "https://i.etsystatic.com/20994514/r/il/6ab59d/3248729537/il_fullxfull.3248729537_dprx.jpg",
        "description": "You can make tea from this plant to treat coughs and sore throats. Windburn and chapping were treated through an infusion of sweetgrass stems soaked in water or a salve of sweetgrass water and grease. The sweetgrass water was also used as an eyewash."
    }
          {
        "name": "Mormon Tea",
        "type": "medicinal",
        "img": "hhttps://www.nps.gov/arch/learn/nature/images/Ephedraceae_Ephedra_viridis_5.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
    }
            {
        "name": "Pinyon nut",
        "type": "edible",
        "img": "https://www.nps.gov/arch/learn/nature/images/Pinaceae_Pinus_edulis_1.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
    }
         {
        "name": "Garlic Mustard",
        "type": "edible",
        "img": "data:image/jpeg;base64,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",}
        "description": "Garlic mustard is a biennial, which means it produces seed on its second year that spreads by seed dispersal and can grow up to six feet tall. It’s best to harvest when the plant is younger and only eat the leaves."
    
    {
        "name": "Wild Spinach",
        "type": "edible",
        "img": "https://loganspader.com/wp-content/uploads/2022/08/wild-spinach-sd-wild-edible-plant-sss.jpg?strip=info&w=528",
        "description":"Also known as lambs quarters this wild plant is best eaten raw as a snack while hiking but also works great in salads or sandwiches. Starts growing in South Dakota in the early summer."
    }
      {
        "name": "Purlsane",
        "type": "edible",
        "img": "https://loganspader.com/wp-content/uploads/2022/08/purslane-close-up-sioux-falls-lawn-weed-edible-sss.jpg?strip=info&w=800",
        "description":"This starts growing midsummer in SD and should be eaten raw"
    }
        {
        "name": "Stinging nettle",
        "type": "edible",
        "img": "https://loganspader.com/wp-content/uploads/2022/08/stinging-nettle-plant-wild-edible-food-22-sss.jpg?strip=info&w=800",
       "description": "Can be eaten raw, just watch out for the pricks."
    }
          {
        "name": "Cattail",
        "type": "edible",
        "img": "https://www.fs.usda.gov/Internet/FSE_MEDIA/stelprdb5070148.jpg",
        "description":"Pluck out of the water and slice the lower end open (just above the roots) like a banana until you get to the crisp core. Be sure to look for young shoots."
          }
            {
        "name": "Wood Sorrel",
        "type": "edible",
        "img": "https://loganspader.com/wp-content/uploads/2022/08/wood-sorel-great-bear-sd-22-sss.jpg?strip=info&w=800",
        "description":"Can be eaten raw."
    }
              {
        "name": "Mulberries",
        "type": "edible",
        "img": "https://loganspader.com/wp-content/uploads/2022/08/mulberry-leaves-sd-s.jpg?strip=info&w=1080",
        "description":"Dark berry that can be eaten raw, and July is the best time to forage them."
    }
          {
        "name": "Wild Licorice",
        "type": "medicinal",
        "img": "https://www.prairiemoon.com/mm5/graphics/00000001/glycyrrhiza-lepidota-wild-licorice_main_548x730.jpg",
        "description":"Native Americans used the root extensively as an herbal remedy for common things like fever, stomach ache, toothache, ear infection and sore throat. The Dakota's steeped the licorice leaves in boiling water to make a topical medicine for earache. The root was also chewed and held in the mouth to relieve toothache. The Blackfeet made a tea from bitter tasting root to relieve coughs, chest pain and sore throat."
    }
     
                        {
        "name": "Prickly Pear",
        "type": "edible",
        "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
        "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
    }
                               {
        "name": "Lechuguilla",
        "type": "edible",
        "img": "https://coldhardycactus.com/cdn/shop/products/YuccalechuguillaGuadalupes1.jpg?v=1607876162",
        "description":"Although primarily known for its fibrous leaves used in traditional crafts, the base and young flower stalks can be cooked and eaten in survival situations."
    }
                                      {
        "name": "Ocotillo",
        "type": "medicinal",
        "img": "https://m.media-amazon.com/images/I/811+ITLQT3L.jpg",
        "description":"This plant is known for its ability to sprout leaves rapidly after rain. It has traditional medicinal uses, such as creating a soothing tea from its flowers to treat symptoms like coughs and chest congestion."
    }
                                             {
        "name": "Yucca",
        "type": "medicinal",
        "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
        "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
    }
                                                    {
        "name": "Honey Mesquite",
        "type": "edible",
        "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
        "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
    }
                   {
        "name": "Creosote bush",
        "type": "medicinal",   ",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
        "It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
    }
           {
        "name": "Mormon Tea",
        "type": "medicinal",
        "img": "hhttps://www.nps.gov/arch/learn/nature/images/Ephedraceae_Ephedra_viridis_5.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
    }
                                         {
        "name": "Beautyberry",
        "type": "edible",
        "img": "https://gardeningsolutions.ifas.ufl.edu/images/plants/shrubs/beautyberry2021.jpg",
        "description":"Native Americans used the beautyberry for a variety of medicinal purposes, including treating malaria, rheumatism, dizziness, stomachaches, and dysentery. Leaves and other parts of the plant were boiled for use in sweat baths to treat malarial fevers and rheumatism. "
    }
                                                    {
        "name": "Dandelion",
        "type": "edible",
        "img": "data:image/jpeg;base64,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",
        "description":"Leafs and flowers can be eaten raw."
    }
                              
                                                                          {
        "name": "Orache",
        "type": "edible",
        "img": "https://thumbs.dreamstime.com/z/atriplex-hortensis-orache-used-as-leaf-vegetable-salads-spring-edible-plant-orach-grows-garden-closeup-also-known-248814192.jpg",
        "description":"Can be eaten raw."
    }
                   {
        "name": "Musk Mustard",
        "type": "edible",
        "img": "data:image/jpeg;base64,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",
        "description":"Like all mustards, the entire plant can be eaten! Musk mustard is one of the mustards that tastes pretty good and lacks a lot of the bitter or hot flavors that can be common in these plants."
    }
                              {
        "name": "Curly Dock",
        "type": "edible",
        "img": "https://images.squarespace-cdn.com/content/v1/61fc74eb0ad5900c8e413b64/f2afb1bc-0d1e-4d8f-b12d-8b2f5292bc9d/Dock3.jpeg?format=1500w",
        "description":"Harvest curly dock in the spring before the plant flowers. Once the plant flowers, the stems become tough and fibrous and are no longer edible."
    }
                                         {
        "name": "Salsify",
        "type": "edible",
        "img": "https://nurturenaturecenter.org/wp-content/uploads/2022/06/DSCF2489-382x509.jpg",
        "description":"Young roots can be eaten raw, otherwise you can boil the leaves and roots."
    }
                       {
        "name": "Prickly Lettuce",
        "type": "edible",
        "img": "https://crops.extension.iastate.edu/files/resize/article/prklyletplant-600x896.jpg",
        "description":"Leaves can be eaten raw, or you can boil the shoots. Prickly lettuce has a distinctive line of reddish bristles on the underside of the leaf midrib. When you cut the plant, a milky juice will come out of the leaves and stem."
    }
                            {
        "name": "Fireweed",
        "type": "edible",
        "img": "https://i0.wp.com/practicalselfreliance.com/wp-content/uploads/2021/05/Fireweed-Plant1-.jpg?resize=1200%2C1800&ssl=1",
        "description":"Can eat seeds and flowers raw, and can cook the roots. It's best to eat leaves raw when they are young. The seeds can also be a firestarter!"
    }
                            {
        "name": "Arrowleaf Balsamroot ",
        "type": "medicinal",
        "img": "https://www.fs.usda.gov/wildflowers/plant-of-the-week/images/arrowleafbalsamroot/balsamorhiza_sagittata.jpg",
        "description":"Medicinally, Native Americans used the large coarse balsamroot leaves as a poultice for burns. Some tribes boiled the roots for a medicinal tea for tuberculosis and whooping cough, rheumatism, headaches, insect bites. Other tribes made an infusion to use as a poultice for wounds, cuts and bruises."
    }
                            {
        "name": "Fern-leaf Desert Parsley",
        "type": "edible",
        "img": "https://gardenshop.symbiop.com/cdn/shop/products/lom_dispsd_1200x1200.jpg?v=1638219109",
        "description":"The roots are edible and can be eaten roasted, steamed, or boiled, or ground into flour. The young leaves and shoots can be eaten raw or cooked."
    }
                            {
        "name": "Fern-leaf Desert Parsley",
        "type": "medicinal",
        "img": "https://gardenshop.symbiop.com/cdn/shop/products/lom_dispsd_1200x1200.jpg?v=1638219109",
        "description":"The roots are used to make medicine for a variety of conditions, including asthma, colds, flu, lung injuries, pneumonia, tuberculosis, and viral infections. It can also be applied as a dressing to treat sores, cuts, boils, bruises, sprains, broken bones, burns, and other skin wounds"
    }
                            {
        "name": "Greenleaf Manzanita",
        "type": "edible",
        "img": "https://bloomcalifornia.org/wp-content/uploads/2021/09/arctostaphylos-glauca_big-berry-manzanita_inat-800.jpg",
        "description":"It features simple, green leaves and reddish-brown bark. The plant produces pink, urn-shaped flowers in small clusters during spring, followed by green berries that turn rusty red when ripe. The seeds can be roasted or ground into flour, and the young shoots and leaves are also edible."
    }
                            {
        "name": "Yarrow",
        "type": "medicinal",
        "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
        "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
    }
        {
        "name": "Pinyon nut",
        "type": "edible",
        "img": "https://www.nps.gov/arch/learn/nature/images/Pinaceae_Pinus_edulis_1.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
    }
    
                            {
        "name": "Evening Primrose",
        "type": "edible",
        "img": "https://commonsensehome.com/wp-content/uploads/2023/09/common-evening-primrose-flower.jpg",
        "description":"You can eat the leaves from a young plant, or boil the shoots."
    }
    
                            {
        "name": "Four O'Clock",
        "type": "medicinal",
        "img": "https://www.kitchengardenseeds.com/media/catalog/product/cache/b8afbc9b375ff88a260fed7bdf351322/4/o/4oclocks1-w.jpg",
        "description":"This plant has a long history of use by Native American tribes such as the Navajo and Hopi. It is primarily used for its roots, which are made into poultices to treat skin conditions and infections. The plant features trumpet-shaped flowers that bloom in the evening."
    }
         {
        "name": "Prickly Pear",
        "type": "edible",
        "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
        "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
    }
    
        {
        "name": "Pinyon nut",
        "type": "edible",
        "img": "https://www.nps.gov/arch/learn/nature/images/Pinaceae_Pinus_edulis_1.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
    }
    
                            {
        "name": "Juniper Berries",
        "type": "medicinal",
        "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
        "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
    }
    
                            {
        "name": "Fourwing saltbush",
        "type": "edible",
        "img": "https://cdn11.bigcommerce.com/s-9ht3qzdye/images/stencil/960w/products/357/2923/fourwingsaltbush_Atriplex_canescens_var_canescens_3__93515.1657035474.jpg?c=1",
        "description":"The seeds of this shrub are a valuable food source for wildlife and birds. Native Americans also ate the seeds and ground them into flour, and boiled the leaves to make a yellow dye. "
    }
    
       {
        "name": "Pinyon nut",
        "type": "edible",
        "img": "https://www.nps.gov/arch/learn/nature/images/Pinaceae_Pinus_edulis_1.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
    }
    
                            {
        "name": "Juniper Berries",
        "type": "medicinal",
        "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
        "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
    }
       {
        "name": "Pinyon nut",
        "type": "edible",
        "img": "https://www.nps.gov/arch/learn/nature/images/Pinaceae_Pinus_edulis_1.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
    }
    
                            {
        "name": "Juniper Berries",
        "type": "medicinal",
        "img": "https://backyardforager.com/wp-content/uploads/2017/02/IMG_4720-768x1024.jpg",
        "description":" Native American tribes also used the juniper for its medicinal qualities to treat coughs, headaches, and stomach aches. You can use the berries as a tea."
    }
                             {
        "name": "Yucca",
        "type": "medicinal",
        "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
        "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
    }
       {
        "name": "Yucca",
        "type": "medicinal",
        "img": "https://images.almostedenplants.com/images/full/Yucca%20cernua%20(16).jpg",
        "description":"The roots of yucca plants are sometimes used to make soaps due to their saponin content, and the leaves can be used to alleviate pain through topical applications."
    }
     {
        "name": "Pinyon nut",
        "type": "edible",
        "img": "https://www.nps.gov/arch/learn/nature/images/Pinaceae_Pinus_edulis_1.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
    }
      {
        "name": "Prickly Pear",
        "type": "edible",
        "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
        "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
    }
                            
                
                                                    {
        "name": "Honey Mesquite",
        "type": "edible",
        "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
        "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
                                                    }
    {
        "name": "Cholla",
        "type": "edible",
        "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
        "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
    }
      {
        "name": "Catalina Cherry",
        "type": "edible",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Prunus_ilicifolia_ne1.jpg/440px-Prunus_ilicifolia_ne1.jpg",
        "description":"This plant can grow as a shrub or a tree, and its fruit is edible. The fruit is dark purple to black when ripe, and has a large seed and pulpy flesh. The pits can be boiled to remove toxic chemicals, then mashed and eaten"
    }
      {
        "name": "Prickly Pear",
        "type": "edible",
        "img": "https://cdn.britannica.com/31/100631-050-F219B9CB/Prickly-pear-cactus-Arizona.jpg?w=400&h=300&c=crop",
        "description":"Known for its edible pads and fruits, the prickly pear is a common sight in arid areas. The pads can be cooked and eaten, and the fruits are often used to make syrups and jellies."
    }
      {
        "name": "Manzanita",
        "type": "edible",
        "img": "https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153664648468496389.jpeg?x-oss-process=image/format,webp/resize,s_600&v=1.0",
        "description":" The berries are edible and can be eaten raw or used to make cider. The leaves have been used in traditional remedies for treating stomach ailments."
    }
      {
        "name": "Deer Grass",
        "type": "edible",
        "img": "https://www.cpp.edu/biotrek/img/ethnobotany/Ethnobotany%20Images/muhlenbergia_rigens_1.jpeg",
        "description":" The foundation of the plant materials were used for coiled baskets. The seeds are edible and were often eaten by natives."
    }
      {
        "name": "Lemonade Berry ",
        "type": "medicinal",
        "img": "The berries of this plant can be soaked in water to make a lemonade-like drink. The plant also has medicinal uses, including as a treatment for respiratory issues",
        "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
    }
        {
        "name": "Pawpaw",
        "type": "edible",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Asimina_triloba3.jpg/440px-Asimina_triloba3.jpg",
        "description": "Produces a large, yellowish-green fruit that is edible and has a custard-like taste. It is rich in nutrients and can be eaten raw or used in various recipes."
    }
    {
        "name": "Spicebush",
        "type": "medicinal",
        "img": "https://www.joyfulbutterfly.com/wp-content/uploads/2015/02/Lindera_benzoin.jpg",
        "description": "The berries and leaves are used to make tea, traditionally used to treat fevers, colds, and gastrointestinal issues."
    }
    {
        "name": "Jewelweed",
        "type": "medicinal",
        "img": "https://www.adirondackalmanack.com/wp-content/uploads/2015/07/Jewelweed-540x702.jpg",
        "description": "Known for treating skin irritations, such as poison ivy rashes. The leaves and juice from the stem are applied directly to the skin."
    }
    {
        "name": "Wild Ginger",
        "type": "edible",
        "img": "https://www.eattheweeds.com/wp-content/uploads/2017/09/Asarum_canadense.jpg",
        "description": "The roots can be used as a spice or brewed into a tea. It has been used to aid digestion and treat intestinal ailments."
    }
    {
        "name": "Greenbrier",
        "type": "edible",
        "img": "https://www.carolinanature.com/trees/smro6025.jpg",
        "description": "The young shoots and leaves are edible raw or cooked, similar to asparagus. The roots can be used to make a starchy paste."
    }
    {
        "name": "Nettle",
        "type": "medicinal",
        "img": "https://www.wildedible.com/sites/default/files/styles/1200wide/public/stinging-nettles-p.jpg.webp?itok=DBoqFtXF",
        "description": "Once cooked, the leaves are safe to eat and very nutritious. Nettle has been used medicinally for its anti-inflammatory properties and as a diuretic."
    }
     {
        "name": "Oregon Grape",
        "type": "medicinal",
        "img": "https://www.nps.gov/articles/000/images/B_aquifolium_Bruce_Newhouse_ORFloraProject_permission.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The roots contain berberine, used as an antimicrobial agent. The berries are tart but edible and can be made into jellies or fermented into wine."
    }
                    {
        "name": "Yarrow",
        "type": "medicinal",
        "img": "https://ginosnursery.com/wp-content/uploads/2022/03/IMG_6026.jpeg",
        "description":"Leaves and flowers can be steeped in boiling water for 5-10 minutes to make yarrow tea. Use about 1-2 teaspoons of yarrow in each cup of water for fever. For skin injuries, you can apply the leaves or juices directly on wound."
    }
    {
        "name": "Wild Strawberry",
        "type": "edible",
        "img": "https://strawberryplants.org/wp-content/uploads/growing-wild-alpine-strawberries.jpg",
        "description": "The small, red fruits are edible and flavorful, perfect for fresh eating or making jam. The leaves can also be used to make tea."
    }
    {
        "name": "Thimbleberries",
        "type": "edible",
        "img": "https://www.nps.gov/common/uploads/cropped_image/primary/50D9D92F-A4A6-F924-2D093E1751A63015.jpg?width=1600&quality=90&mode=crop",
        "description": "The velvety-textured of the thimbleberries feels strange on the tongue of the uninitiated, but the Huna Tlingit relish the flavor of this thimble-shaped berry when it ripens in August."
    }
    {
        "name": "Sagebrush",
        "type": "medicinal",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Sagebrushsjc.jpg/440px-Sagebrushsjc.jpg",
        "description": "Used by Native American tribes for various remedies, including treating colds and headaches by making a tea from the leaves. Can also be used to make a wash to treat wounds."
    }
     {
        "name": "Jewelweed",
        "type": "medicinal",
        "img": "https://www.adirondackalmanack.com/wp-content/uploads/2015/07/Jewelweed-540x702.jpg",
        "description": "Known for treating skin irritations, such as poison ivy rashes. The leaves and juice from the stem are applied directly to the skin."
    }
    {
        "name": "Wild Ginger",
        "type": "edible",
        "img": "https://www.eattheweeds.com/wp-content/uploads/2017/09/Asarum_canadense.jpg",
        "description": "The roots can be used as a spice or brewed into a tea. It has been used to aid digestion and treat intestinal ailments."
    }
     {
        "name": "Elderberries",
        "type": "medicinal",
        "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14801/content_c4-Image-by-Mark-Robinson.-Elderberries.jpg",
        "description": "Berries and flowers are used in traditional remedies for immune support and to treat colds and flu. Berries must be cooked before consumption to avoid toxicity."}
  {
        "name": "Raspberries",
        "type": "edible",
        "img": "https://s3.amazonaws.com/beautifulnow_production/uploads/ckeditor_assets/pictures/14799/content_c2-Image-by-Eric.-Wild-Raspberries..jpg",
        "description": "Raspberries are a small, sweet, and spongy fruit that can be red, purple, black, or golden in color. They are part of the rose family and are a great source of fiber, vitamins C and K, and manganese."
    }
      {
        "name": "Nettle",
        "type": "medicinal",
        "img": "https://www.wildedible.com/sites/default/files/styles/1200wide/public/stinging-nettles-p.jpg.webp?itok=DBoqFtXF",
        "description": "Once cooked, the leaves are safe to eat and very nutritious. Nettle has been used medicinally for its anti-inflammatory properties and as a diuretic."
    }
           {
        "name": "Creosote bush",
        "type": "medicinal",   ",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhskbo1EwcW8rL_rdVUmmjBukVM4pKJYS2Ow&s",
        "It is known to repel pests. Stems crushed in water helped reduce the pain of rheumatism. Creosote tea, a foul-tasting liquid, was used to treat tuberculosis, and its vapor inhaled for other respiratory ailments."
    }
    
      {
        "name": "Cholla",
        "type": "edible",
        "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
        "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
    }
         {
        "name": "Mormon Tea",
        "type": "medicinal",
        "img": "hhttps://www.nps.gov/arch/learn/nature/images/Ephedraceae_Ephedra_viridis_5.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "Blooms from March-July. The boiled stems have been used to make a tea which can work as a decongestant.  "
    }
     {
        "name": "Desert Holly",
        "type": "edible",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/California_Death_Valley_Ubehebe_plant.jpg/440px-California_Death_Valley_Ubehebe_plant.jpg",
        "description": "The leaves of Desert Holly can be eaten raw or cooked. They have a salty flavor and are often used as a seasoning."
    }
                   {
        "name": "Mesquite",
        "type": "edible",
        "img": "https://www.theherbcottage.com/wp-content/uploads/2016/10/Prosopis-glandulosa-seed-pods.jpg",
        "description":"The seed, or bean, pods were eaten raw, or collected, ground, mixed with water, and eaten as is or dried into cakes."
    }
                     {
        "name": "Sea Grape",
        "type": "edible",
        "img": "https://www.tcpalm.com/gcdn/presto/2019/11/05/PTCN/4e32f5d7-4f63-4006-95c5-ec15f405ad57-Coccoloba_uvifera_Nov_17.JPG?width=600&height=636&fit=crop&format=pjpg&auto=webp",
        "description": "Sea Grape fruits can be eaten fresh or made into jellies and wines. The large leaves can also be used for relief from sunburn."
    },
    {
        "name": "Scaevola Taccada",
        "type": "medicinal",
        "img": "https://toptropicals.com/pics/garden/m2/2014/8/20140830_115553Scaevola_taccada_TA.jpg",
        "description": "Also known as sea lettuce, the leaves of this plant are used in traditional medicine to treat eye infections and as a general antiseptic."
    },
    {
        "name": "Buttonwood",
        "type": "medicinal",
        "img": "https://tinezfarms.com/cdn/shop/files/buttonwood-standard-green-conocarpus-erectus-plantologyusa-3-gallon-148229_jpg_1024x.webp?v=1720462168",
        "description": "The bark of Buttonwood is used in traditional remedies for headaches and muscle pain."
    }
    {
        "name": "Saw Palmetto",
        "type": "medicinal",
        "img": "https://www.meadowbeautynursery.com/wp-content/uploads/2017/01/Charleston-067.jpg",
        "description": "Saw Palmetto berries are used in traditional medicine for their benefits to prostate health and hormone regulation."
    }
   {
        "name": "Cattail",
        "type": "edible",
        "img": "https://www.fs.usda.gov/Internet/FSE_MEDIA/stelprdb5070148.jpg",
        "description":"Pluck out of the water and slice the lower end open (just above the roots) like a banana until you get to the crisp core. Be sure to look for young shoots."
          }
    {
        "name": "Cocoplum",
        "type": "edible",
        "img": "https://images.squarespace-cdn.com/content/v1/58458123ff7c506672298481/1538408730987-1Y3IFQ3TYP5PVRX17P2P/Plant+Creations+Nursery+Cocoplum+Chrysobalanus+icaco?format=750w",
        "description": "Cocoplum fruit can be eaten fresh or made into jams and jellies. The stone inside can also be cracked open to extract an edible kernel."
    }
    {
        "name": "Mangrove",
        "type": "medicinal",
        "img": "https://npr.brightspotcdn.com/dims4/default/9ec1db0/2147483647/strip/true/crop/5725x3822+0+0/resize/840x560!/format/webp/quality/90/?url=https%3A%2F%2Fnpr.brightspotcdn.com%2Fd9%2Faa%2Fa8bbc4cb4394a52629701f0d82d1%2F42394815810-08191c1c4b-o.jpg",
        "description": "Mangrove bark is used in traditional medicine to treat skin conditions and wounds due to its antiseptic properties."
    }
                                          {
        "name": "Dandelion",
        "type": "edible",
        "img": "data:image/jpeg;base64,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",
        "description":"Leafs and flowers can be eaten raw."
    }
                                           {
        "name": "Plantain",
        "type": "medicinal",
        "img": "https://weedid.missouri.edu/images/images_optimized/2455optimized.jpg",
        "description": "Plantain leaves are known for their medicinal properties, particularly for treating skin irritations and wounds. They can be crushed and applied as a poultice directly to the skin to soothe inflammation."
    },
    {
        "name": "White Clover",
        "type": "edible",
        "img": "https://www.thespruce.com/thmb/ojIM2rHV6W2v4UdsLdhFFbRDp58=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/growing-white-clover-trifolium-repens-5101230-hero-e134e5d705eb48309508c55110bff91d.jpg",
        "description": "White clover flowers and leaves are edible, often used in teas and salads. The flowers can also be dried and added to baked goods for a sweet, vanilla-like flavor."
    },
    {
        "name": "Mullein",
        "type": "medicinal",
        "img": "https://virginiawildflowers.org/wp-content/uploads/2015/06/img_8839.jpg",
        "description": "Mullein is used medicinally, particularly for its effectiveness in treating respiratory problems. The leaves and flowers can be used to make a tea that soothes coughs and congestion."
    }
       {
        "name": "Fireweed",
        "type": "edible",
        "img": "https://i0.wp.com/practicalselfreliance.com/wp-content/uploads/2021/05/Fireweed-Plant1-.jpg?resize=1200%2C1800&ssl=1",
        "description":"Can eat seeds and flowers raw, and can cook the roots. It's best to eat leaves raw when they are young. The seeds can also be a firestarter!"
    }
          {
        "name": "Pinyon nut",
        "type": "edible",
        "img": "https://www.nps.gov/arch/learn/nature/images/Pinaceae_Pinus_edulis_1.jpg?maxwidth=650&autorotate=false&quality=78&format=webp",
        "description": "The trees yield edible nuts, which are a staple food of Native Americans, and widely eaten as a snack and as an ingredient in New Mexican cuisine. "
    }
            {
        "name": "Huckleberry",
        "type": "edible",
        "img": "https://www.southernexposure.com/media/products/width-1200/garden-huckleberry-5c2187bf821f4161c5ec8f6e2ecd2df0.jpg",
        "description": "Huckleberries are highly prized in Glacier National Park. These berries are sweet and flavorful, commonly used in pies, jams, and preserves."
    }
    {
        "name": "Beargrass",
        "type": "medicinal",
        "img": "https://www.fs.usda.gov/wildflowers/plant-of-the-week/images/beargrass/Xerophyllum_tenax1_Barbara_Mumblo.jpg",
        "description": "While not edible, beargrass has traditional medicinal uses, such as poultices made from its roots to treat burns and insect bites."
    }
    {
        "name": "Wild Mint",
        "type": "medicinal",
        "img": "https://eattheplanet.org/wp-content/uploads/2020/05/Mentha_canadensis_2.jpg",
        "description": "Wild mint found in the park can be used to make a refreshing tea that helps in digestion and can relieve symptoms of colds and flu."
    }
      {
        "name": "Cholla",
        "type": "edible",
        "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
        "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
    }
      {
        "name": "Cholla",
        "type": "edible",
        "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
        "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
    }
      {
        "name": "Cholla",
        "type": "edible",
        "img": "https://media.azpm.org/master/image/2017/6/16/hero/cholla-2.jpg",
        "description":"The buds of this cactus are edible and are traditionally eaten in the Southwest."
    }
]

# Add plants to the database
for plant in plants:
    new_plant = Plant(
        name=plant['name'],
        type=plant['type'],
        img=plant['img'],
        description=plant['description']
    )
    db.session.add(new_plant)

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
    {"name": "Theodore Roosevelt", "state": "ND"},s
    {"name": "Voyageurs", "state": "MN"},
    {"name": "White Sands", "state": "NM"},
    {"name": "Wind Cave", "state": "SD"},
    {"name": "Yellowstone", "state": "WY"},
    {"name": "Yosemite", "state": "CA"},
    {"name": "Zion", "state": "UT"}
]

# Add parks to the database
for park in parks:
    national_park = National_Park(name=park['name'], state=park['state'])
    db.session.add(national_park)

# Commit changes to the database
db.session.commit()
print("National Parks have been added to the database.")
    
    # print("creating users!")
    # user1 = User(email='nancyleebechtold@gmail.com', password_hash='meow123')
    # user2 = User(email='annbechtold0883@gmail.com', password_hash='woof123')

    # Add users to the session and commit to generate IDs
    # users = [user1, user2]
    # db.session.add_all(users)
    # db.session.commit()

    print("creating guides!")
    # guide1 = Guide(title='trip to yosemite', description='I love yosemite!', user_id=user1.id)
    # guide2 = Guide(title='trip to rocky mountain', description='I love rocky mountain!', user_id=user2.id)
    
    # Add other records
    plants = [plant1, plant2]
    parks = [nationalpark1, nationalpark2]
    guides = [guide1, guide2]
    
    db.session.add_all(plants)
    db.session.add_all(parks)
    db.session.add_all(guides)
    db.session.commit()
    
    print("creating join table entries!")
    # Create join table entries after the primary records have been committed
    # plant_guide_join1 = Plant_Guide_Join(plant_id=plant1.id, guide_id=guide1.id)
    # plant_guide_join2 = Plant_Guide_Join(plant_id=plant2.id, guide_id=guide2.id)

    plant_np_join1 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id)
    plant_np_join3 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join4 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id)
    plant_np_join4 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id)
    plant_np_join6 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id) 
    plant_np_join1 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id)
    plant_np_join1 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id)
    plant_np_join1 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id)
    plant_np_join1 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark1.id)
    plant_np_join1 = Plant_NP_Join(plant_id=plant1.id, national_park_id=nationalpark1.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark2.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark2.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark2.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark2.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark2.id)
    plant_np_join2 = Plant_NP_Join(plant_id=plant2.id, national_park_id=nationalpark2.id)

    join_entries = [plant_guide_join1, plant_guide_join2, plant_np_join1, plant_np_join2]
    
    db.session.add_all(join_entries)
    db.session.commit()
