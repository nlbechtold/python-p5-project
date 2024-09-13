import { useState, useEffect } from 'react'
import Guide from './Guide.jsx'
import Userpage from './Userpage.jsx'
import Login from './Login.jsx'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import 'semantic-ui-css/semantic.min.css'

function App(){
  
  // States
  const [user, setUser] = useState(null);
  const [guideId, setGuideId] = useState("");

  
  // Check if user is logged in
  useEffect(() => {
    fetch(`/checksessions`)  
      .then((r) => {
        if (r.ok) {
          return r.json();
        } else {
          throw new Error();
        }
      })
      .then((data) => {
        setUser(data);
      })
      .catch(() => {
        console.log("Error in session check");
      });
  }, []);
// below are the routes
  return (
    <div className="body2">
      <BrowserRouter>
        <Routes>
          {user ? (
            <>
              <Route path="/user" element={<Userpage user={user} setUser={setUser} setGuideId={setGuideId}/>} />
              <Route path="/user/guide" element={<Guide guideId={guideId} user={user}/>} />
              <Route path="*" element={<Navigate to="/user" />} /> 
            </>
          ) : (
            <>
              <Route path="/" element={<Login user={user} setUser={setUser} />} />
              <Route path="*" element={<Navigate to="/" />} /> 
            </>
          )}
        </Routes>
      </BrowserRouter>
    </div>
  );
}
export default App