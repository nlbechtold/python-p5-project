import { React, useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import { Form, Button, FormField, Card, FormSelect } from 'semantic-ui-react';
import Plant from './Plant';
import '../style.css';
import SelectedPlant from './SelectedPlant';

function Guide({ guideId, user }) {

    // All states for guide pages
    const [selectedPlant, setSelectedPlant] = useState([]);
    const [filteredPlant, setFilteredPlant] = useState([]);
    const [filterType, setFilterType] = useState("");
    const [filterName, setFilterName] = useState("");
    const [filterState, setFilterState] = useState("");
    const navigate = useNavigate();

    // Fetch all plant data and set selected plant based on guide
    useEffect(() => {
        fetch('/plants')
            .then(r => r.json())
            .then(data => {
                setFilteredPlant(data);
            });

        if (user && user.guides) {
            const selectedGuide = user.guides.find(guide => guide.id === guideId);
            if (selectedGuide && selectedGuide.plant) {
                setSelectedPlant(selectedGuide.plant);
            } else {
                setSelectedPlant([]);  // Ensure selectedPlant is set to an empty array
            }
        }
    }, [guideId, user]);

    // Function to add plants to guide
    function addToGuide(newPlant) {
        fetch(`/add_plants_to_guide`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                guide_id: guideId,  
                plant_ids: [newPlant.id], 
            }),
        })
        .then(response => response.json())
        .then(() => {
            setSelectedPlant([...selectedPlant, newPlant]);
        })
        .catch(error => console.error('Error adding plant:', error));
    }

    // Function to filter plants based on national park name, state, and type
    function handleSearch(e) {
        e.preventDefault();

        fetch(`/plants`)
            .then(r => r.json())
            .then(data => {
                // Apply case-insensitive filtering for national park name, state, and plant type
                const filtered = data.filter(plant => {
                    const parkName = plant.national_parks[0]?.name.toLowerCase() || '';
                    const parkState = plant.national_parks[0]?.state.toLowerCase() || '';
                    const plantType = plant.type.toLowerCase();
                    
                    return (
                        (!filterName || parkName.includes(filterName.toLowerCase())) &&
                        (!filterState || parkState.includes(filterState.toLowerCase())) &&
                        (!filterType || plantType === filterType.toLowerCase())
                    );
                });
                setFilteredPlant(filtered);
            });
    }

    // Renders plants based on filter
    const plantRender = filteredPlant.map((plant) => {
        return <Plant key={plant.id} plant={plant} addToGuide={addToGuide} />;
    });

    const selectedPlantRender = selectedPlant.map((plant) => {
        return <SelectedPlant key={plant.id} plant={plant} guideId={guideId} selectedPlant={selectedPlant} setSelectedPlant={setSelectedPlant} />;
    });

    const options = [
        { key: 'a', text: '--Select--', value: '' },
        { key: 't', text: 'Edible', value: 'edible' },
        { key: 'c1', text: 'Medicinal', value: 'medicinal' },
    ];

    return (
        <div className="container">
            <div className="Header">
                <h1>Guide Page</h1>
                <Button color='black' onClick={() => navigate('/user')}>Back to Home</Button>

                <Form onSubmit={handleSearch}>
                    <h2>Filter Search</h2>

                    <FormSelect
                        fluid
                        label="Select Type"
                        options={options}
                        placeholder="--Select--"
                        onChange={(e, { value }) => setFilterType(value)}
                    />

                    <FormField>
                        <label>National Park Name</label>
                        <input
                            placeholder="Search by park name"
                            value={filterName}
                            onChange={(e) => setFilterName(e.target.value)}
                        />
                    </FormField>

                    <FormField>
                        <label>State</label>
                        <input
                            placeholder="Search by state"
                            value={filterState}
                            onChange={(e) => setFilterState(e.target.value)}
                        />
                    </FormField>

                    <Button color='black' type="submit">Search</Button>
                </Form>

                <div className="Content2">
                    <div className="plants2" itemsperrow={2}>
                        <Card.Group>
                            {selectedPlantRender}
                        </Card.Group>
                    </div>
                    <div className="plants">
                        <Card.Group>
                            {plantRender}
                        </Card.Group>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Guide;
