import { useState } from 'react';
import { CardMeta, CardHeader, CardContent, Card, Image, Button, Form, Input } from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';

function GuideCard({ guide, setGuideId, guides, setGuides }) {
    const [isEditing, setIsEditing] = useState(false);
    const [title, setTitle] = useState(guide ? guide.title : '');
    const [description, setDescription] = useState(guide ? guide.description : '');
    const navigate = useNavigate();

    // Function to edit guide and takes you to guide page
    function editGuide() {
        setGuideId(guide.id);
        navigate(`/user/guide`);
    }

    // Function to delete guide
    function deleteGuide() {
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
                const notRemoved = guides.filter((gu) => gu.id !== guide.id);
                setGuides(notRemoved);
            })
            .catch((error) => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }

    // Function to handle the patch request to update guide details
    function handleEditSubmit() {
        fetch(`/guide/${guide.id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title,
                description,
            }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Failed to update guide');
                }
                return response.json();
            })
            .then((updatedGuide) => {
                // Update the guide in the guides state
                const updatedGuides = guides.map((gu) => (gu.id === updatedGuide.id ? updatedGuide : gu));
                setGuides(updatedGuides);
                setIsEditing(false);
            })
            .catch((error) => {
                console.error('There was a problem with the update operation:', error);
            });
    }

    // Ensure guide is defined before rendering
    if (!guide) {
        return <div>Loading...</div>;
    }

    return (
        <Card>
            <CardContent>
                {isEditing ? (
                    <Form>
                        <Form.Field>
                            <label>Title</label>
                            <Input value={title} onChange={(e) => setTitle(e.target.value)} />
                        </Form.Field>
                        <Form.Field>
                            <label>Description</label>
                            <Input value={description} onChange={(e) => setDescription(e.target.value)} />
                        </Form.Field>
                        <Button color="green" onClick={handleEditSubmit}>
                            Save
                        </Button>
                        <Button color="grey" onClick={() => setIsEditing(false)}>
                            Cancel
                        </Button>
                    </Form>
                ) : (
                    <>
                        <CardHeader>{guide.title}</CardHeader>
                        <CardMeta>{guide.description}</CardMeta>
                        {guide.plants && guide.plants.length > 0 && (
                            <div>
                                <h4>Plants:</h4>
                                {guide.plants.map((plant) => (
                                    <div key={plant.id}>
                                        <Image src={plant.img} size="small" />
                                        <p><strong>Name:</strong> {plant.name}</p>
                                        <p><strong>Description:</strong> {plant.description}</p>
                                        <p><strong>Type:</strong> {plant.type}</p>
                                    </div>
                                ))}
                            </div>
                        )}
                        <Button color="green" onClick={editGuide}>Add Plants</Button>
                        <Button color="red" onClick={deleteGuide}>Delete Guide</Button>
                        <Button color="blue" onClick={() => setIsEditing(true)}>Edit Guide</Button>
                    </>
                )}
            </CardContent>
        </Card>
    );
}

export default GuideCard;
