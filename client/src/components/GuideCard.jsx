import { CardMeta, CardHeader, CardContent, Card, Button, Image } from 'semantic-ui-react'
import { useNavigate } from 'react-router-dom'

function GuideCard({guide, setGuideId, guideId, guides, setGuides}){

    const navigate = useNavigate()

    // Function to edit guide and takes you to guide page
    function editGuide(){
        setGuideId(guide.id)
        navigate('/user/guide')
    }

    // Function to delete guide
    function deleteGuide(){
        fetch(`/api/guide/${guide.id}`, {
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
                <CardMeta>
                    {guide.description}
                </CardMeta>
                <Button color='green' onClick={editGuide}>Edit Guide</Button>
                <Button color='red' onClick={deleteGuide}>Delete Guide</Button>
            </CardContent>
        </Card>
    )
}

export default GuideCard