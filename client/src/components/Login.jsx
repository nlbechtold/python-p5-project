/* 
Child file of App.jsx
Holds code for login page, and login form
*/
import {Form, Button, FormField} from 'semantic-ui-react'
import { useNavigate } from 'react-router-dom'  
import React, { useState } from 'react';

function Login({setUser}) {

  // All needed states for login
  const navigate = useNavigate()

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [nEmail, setNEmail] = useState("");
  const [nPassword, setNPassword] = useState("");
  const [cPassword, setCPassword] = useState("");
  const [sLI, setSLI] = useState(false)

  // Handles login and navigates to user page
  function handleLogin(e) {
    e.preventDefault();
    fetch("/api/login",{
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({email:email, stayLoggedIn: sLI,password:password}),
      }
    )
    .then(r=>{
      console.log(r.ok)
      if (r.ok) { return r.json()}
      else {throw new Error}
    })
    .then(data=>{
      console.log(data)
      setUser(data)
      navigate('/user')
    })
    .catch(data=>{
      alert("Not valid emaail/password")
    })
  }

  // Handles creating new user and adding to database
  function handleCreate(newUser){
    fetch("/api/users",{
      method:"POST",
      headers:{
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newUser)
    })
    .then(r=>r.json())
    .then(data=>{
      alert('User Added! Please Login')
    })
    .catch(data=>{
      alert("Not valid email/password")
    })
  }

  // Handles adding new user and calls handleCreate
  function addUser(e){
    e.preventDefault()
    if (cPassword === nPassword) {
      const newUser = {
          email: nEmail,
          password: nPassword
      };
      handleCreate(newUser);
    }
    else {
      alert("Passwords do not match");
    }
  }

  return (
    <div>
      <h1>InteriYOUR Design</h1>
        <h2>Have an Account</h2>
          <Form onSubmit={handleLogin}>
              <h2>Login</h2> 
              <FormField>
                  <label>Email</label>
                  <input type="text" value={email} onChange={(e)=>setEmail(e.target.value)} placeholder="Email" ></input>
              </FormField>
              <FormField>
                  <label>Password</label>
                  <input type="text" value={password} onChange={(e) =>setPassword(e.target.value)} placeholder="Password" ></input>
              </FormField>
              <input type="checkbox" onChange={(e)=>setSLI(!sLI)}/>
              <Button color='black' type='submit'>Submit</Button>
          </Form>
        <h2>Don't Have an Account? Create an account here!</h2>  
          <Form onSubmit={addUser}>
              <h2>Create an Account</h2> 
              <FormField>
                  <label>Email</label>
                  <input type="text" value={nEmail} onChange={(e)=>setNEmail(e.target.value)} placeholder="Email" />
              </FormField>
              <FormField>
                  <label>Password</label>
                  <input type="text" value={nPassword} onChange={(e) =>setNPassword(e.target.value)} placeholder="Password" />
              </FormField>
              <FormField>
                  <label>Confirm Password</label>
                  <input type="text" value={cPassword} onChange={(e) =>setCPassword(e.target.value)} placeholder="Confirm Password" />
              </FormField>
              <Button color='black' >Submit</Button>
          </Form>          
    </div>
  )
}

export default Login;