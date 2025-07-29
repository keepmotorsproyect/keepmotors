import { useState, useEffect, useCallback } from 'react';
import './App.css';
import axios from 'axios';
import Login from './login.jsx'


function App() {
  const [count, setCount] = useState(0)
  return (
    <>

      <Login />

      <div>
        <a href="https://vite.dev" target="_blank">
        
        </a>
        <a href="https://react.dev" target="_blank">
       
        </a>
      </div>

    </>
  )
}

export default App
