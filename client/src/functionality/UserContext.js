import { createContext, useState, useEffect } from "react";

export const UserContext = createContext(null);

export function UserProvider({ children }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    login()
  }, [])

  // Function to handle login
  const login = () => {
     // Checks if user session exists if not in dev mode
     fetch('/api/authorized')
     .then(res => {
       if (res.ok) {
         return res.json()
       } else {
         setUser(null)
       }
     })
     .then((data) => {
       setUser(data) 
     })
     .catch(error => {
       console.error("Error fetching user:", error)
       setUser(null)
     })
  }

  // Function to handle logout
  const logout = () => {
    setUser(null); 
  };

  useEffect(() => {
    
  }, []);

  return (
    <UserContext.Provider value={{ user, setUser, logout, login}}>
      {children}
    </UserContext.Provider>
  );
}
