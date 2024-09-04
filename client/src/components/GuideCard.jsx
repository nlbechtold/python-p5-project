
import { CardMeta, CardHeader, CardContent, Card, Image,Button } from 'semantic-ui-react'
import { useNavigate } from 'react-router-dom'
// import React from 'react';

function GuideCard({guide, setGuideId,  guides, setGuides}){




    const navigate = useNavigate()

    // Function to edit guide and takes you to guide page
    function editGuide(){
        setGuideId(guide.id)
        navigate(`/user/guide`)
    }

    // Function to delete guide
    function deleteGuide(){
        fetch(`/guide/${guide.id}`, {
            method: 'DELETE',
        })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Failed to delete guide');
            }
            return response.json();
        })
        .then(() => {
            const notRemoved = guides.filter(gu=>{
                if(gu.id == guide.id){
                    return false
                }
                return true    
            })
            setGuides(notRemoved)
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
        const notRemoved = guides.filter(gu=>{
            if(gu.id == guide.id){
                return false
            }
            return true    
        })
        setGuides(notRemoved)
    }

    return (
        <Card>
            <CardContent>
            <CardHeader>{guide.title}</CardHeader>
                <CardMeta>{guide.description}</CardMeta>
                {guide.plants && guide.plants.length > 0 && (
                    <div>
                        <h4>Plants:</h4>
                        {guide.plants.map(plant => (
                            <div key={plant.id}>
                                <Image src={plant.img} size="small" />
                                <p><strong>Name:</strong> {plant.name}</p>
                                <p><strong>Description:</strong> {plant.description}</p>
                                <p><strong>Type:</strong> {plant.type}</p>
                            </div>
                        ))}
                    </div>
                )}
                <Button color='green' onClick={editGuide}>Edit Guide</Button>
                <Button color='red' onClick={deleteGuide}>Delete Guide</Button>
            </CardContent>
        </Card>
    )
}
// GuideCard.propTypes = {
//     guide = PropTypes.something.isRequired,
//     guide.id = PropTypes.something.isRequired.
// }
export default GuideCard
