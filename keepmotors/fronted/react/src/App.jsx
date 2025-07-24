import React from 'react'
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


function App() {
  const [count, setCount] = useState(0)
  return (
    <>
    <login></login>
      <div>
        <a href="https://vite.dev" target="_blank">
        
        </a>
        <a href="https://react.dev" target="_blank">
       
        </a>
      </div>

      <h1>Keep Motors</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          registrar {count}
        </button>
        <p>
          
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
