/*
Card for all the furiture for each project.
Child file of Project.jsx
*/
import { CardMeta, CardHeader, CardContent, Card, Button, Image } from 'semantic-ui-react'

function SelectedPlant({plant, guideId, selectedPlant, setSelectedPlant}){


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
                  
                </CardContent>
            </Card>    
        </div>
    )
}

export default SelectedPlant