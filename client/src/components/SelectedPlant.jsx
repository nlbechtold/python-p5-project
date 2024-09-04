/*
Card for all the furiture for each project.
Child file of Project.jsx
*/
import { CardMeta, CardHeader, CardContent, Card, Button, Image } from 'semantic-ui-react'

function SelectedFurniture({plant, guideId, selectedPlant, setSelectedPlant}){

    // Function to remove furniture from project
    // function handleClick() {
    //     console.log(plant)
    //     fetch(`/api/project/${guideId}/remove_furniture`, {
    //         method: 'DELETE',
    //         headers: {
    //             'Content-Type': 'application/json',
    //         },
    //         body: JSON.stringify({
    //             project_id: projectId,
    //             furniture_id: furniture.id,
    //         }),
    //     })
    //     .then(response => response.json())        
    //     .catch(error => {
    //         console.error('There was a problem with the fetch operation:', error);
    //     });
    //     const notRemoved = selectedFurniture.filter(furn=>{
    //         if(furn.id == furniture.id){
    //             return false
    //         }
    //         return true    
    //     })
    //     setSelectedFurniture(notRemoved)
    // }

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

export default SelectedFurniture