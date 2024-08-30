import { CardMeta, CardHeader, CardContent, Card, Button, Image } from 'semantic-ui-react'

function Plant({plant, addToGuide}){

    // Function to add  plant to guide
    function addPlant(e){
        e.preventDefault()
        const id = plant.id
        addToGuide(plant, id);
    }
    
    return (
        <div>
            <Card>
                <Image alt="uh oh" src={plant.img}/>
                <CardContent>
                    <CardHeader>{plant.name}</CardHeader>
                    <CardMeta>
                        {plant.type}
                    </CardMeta>
                    <CardMeta>
                        {plant.description}
                    </CardMeta>
                    <Button color='green' onClick={(e)=>addPlant(e)}>Add to Guide</Button>
                </CardContent>
            </Card>    
        </div>
    )
}

export default Plant