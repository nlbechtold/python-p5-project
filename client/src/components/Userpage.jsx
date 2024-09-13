
// Child File of App.jsx
// Holds code for user home page, guide Cards will be a child file holding code 
// for each guide card displayed on homepage
// Components in here, Guide List, Sign Out button, New Guide Form

import { useNavigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import {Form, Button, FormField} from 'semantic-ui-react'
import GuideCard from './GuideCard'

function Userpage ({user, setUser, setGuideId}) {

    // States for userpage
    const [guides, setGuides] = useState([]);
    const [title, setTitle] = useState("");  
    const [description, setDescription] = useState("");
    const navigate = useNavigate()

    // Function to log user out
    function handleLogout(){
        fetch('/logout',{method:"DELETE"})
        .then(r=>r.json())
        .then(() => setUser(undefined))
        .then(()=>navigate('/'))
    }

    // Fetch all guide data
    useEffect(() => {
        if (user) {
            console.log(user)
            fetch(`/user/${user.id}/guides`, {  // Full URL to backend
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Failed to fetch guides');
                }
            })
            .then(data => setGuides(data))
            .catch(err => {
                console.log(err);
            })
        }
    }, [user]);

    // Function to add new guide
    function handleSubmit(newGuide) {
        fetch(`/user/${user.id}/guides`, {
          method: "POST",
          headers: {
            "Content-Type": "Application/json"
          },
          body: JSON.stringify(newGuide)
        })
        .then(r => {
          if (r.ok) {
            return r.json(); // Parse the JSON from the response
          } else {
            throw new Error('Failed to create guide');
          }
        })
        .then(data => {
          const newArr = [...guides, data]; // Add the new guide to the existing guides array
          setGuides(newArr);
          setTitle(''); // Clear form fields after submission
          setDescription('');
        })
        .catch(err => {
          console.error(err);
        });
      }

    // Function to add new guide
    function addGuide(e) {
        e.preventDefault();
        if (user) {
          const newGuide = {
            title: title,
            description: description,
            user_id: user.id
          };
          handleSubmit(newGuide);
        } else {
          alert("User not found");
        }
      }

    // Render guide cards
    const guideRender = guides.map((guide)=>{
        return <GuideCard key={guide.id} guide={guide}  setGuideId={setGuideId}  guides={guides} setGuides={setGuides} user={user}/>
    })

    return (
        <div>
           
            <h2>Welcome  to Foraging Friends</h2>
            <Button color='black' onClick={(e)=>handleLogout(e)}>Sign Out</Button>
            {guideRender}
            <Form onSubmit={addGuide}>
                <h2>Create a New Guide</h2>
                    <FormField>
                        <label>Title</label>
                        <input type="text" value={title} onChange={(e)=>setTitle(e.target.value)} placeholder="Title" required />
                    </FormField>
                    <FormField>
                        <label>Description</label>
                        <input type="text" value={description} onChange={(e)=>setDescription(e.target.value)} placeholder="Description" required />
                    </FormField>
                    <Button color='black' type='submit'>Create</Button>
            </Form>
        </div>
    )
}

export default Userpage 