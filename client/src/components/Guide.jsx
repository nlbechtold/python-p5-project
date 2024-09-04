
import {React, useState, useEffect } from "react"
import { useNavigate } from 'react-router-dom'
import {Form, Button, FormField, Card, FormSelect} from 'semantic-ui-react'
// import SelectedFurniture from './SelectedFurniture'
import Plant from './Plant'
import  '../style.css'
import SelectedPlant from './SelectedPlant'

function Guide({guideId, user}) {

    // All states for guide pages
    const [plant, setPlant] = useState([]) 
    const [selectedPlant, setSelectedPlant] = useState([])
    const [filteredPlant, setFilteredPlant] = useState([])
    const [filter, setFilter] = useState("")
    // const [name, setName] = useState("")
    // const [price, setPrice] = useState("")
    // const [type, setType] = useState("")
    // const [img, setImg] = useState("")
    const navigate = useNavigate()


    // Fetch all plant data and sets selected plant based on guide
    useEffect(()=>{
        fetch('/plants')
        .then(r=>r.json())
        .then(data=>{
            setPlant(data)
            setFilteredPlant(data)
        })
        if (user && user.guides) {
            const selectedGuide = user.guides.find(guide => guide.id === guideId);
            
            if (selectedGuide) {
                console.log("guide found");
                setSelectedPlant(selectedGuide.plant);
            } else {
                console.log("guide not found");
            }
        }
    }
    ,[])
    // Function to add plans to guide
    function addToGuide(newPlant, id) {
        fetch(`/guide/${guideId}/add_plants_to_guide`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                guide_id: guideId,  
                plant_id: id,  
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response bad');
            }
            return response.json();
        })
        .then(data=>{
            const newArr = [...selectedPlant, newPlant]
            setSelectedPlant(newArr)
          })
        .catch(error => {
            console.error('There was a problem with the fetch:', error);
        });
    }

 
    // function to filter plant by type
    function handleSearch(e){
        e.preventDefault()
        setFilteredPlant(plant.filter(pl=>{
            if(filter === ''){
                return true
            }
            else if(filter == pl.type)
                return true
        }))
    }



    // renders furniture based on filter
    const plantRender = filteredPlant.map((plant)=>{
        return <Plant key={plant.id} plant={plant} addToGuide={addToGuide}/>
    })

  
    const selectedPlantRender = selectedPlant.map((plant)=>{
        return <SelectedPlant key={plant.id} plant={plant} guideId={guideId} selectedPlant={selectedPlant} setSelectedPlant={setSelectedPlant}/>
    })

    const options = [ 
        { key: 'a', text: '--Select--', value: '' },
        { key: 't', text: 'Edible', value: 'edible' },
        { key: 'c1', text: 'Medicinal', value: 'medicinal' },
     
    ]

    return (
     
        <div className="container">
            <div className="Header"> 
                <h1>Guide Page</h1>
                <Button color='black' onClick={(e)=>navigate('/user')}>Back to Home</Button>
        
                <Form onSubmit={(e)=>handleSearch(e)}>
                    <h2>Filter Search</h2> 
                    <Button color='black' type="submit">Search</Button>
                    <FormSelect onChange={(e, { value })=>setFilter(value)}
                        fluid
                        label='Select Type'
                        options={options}
                        placeholder='--Select--'    
                    />
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
    )

}


export default Guide