import React from "react";
import './login.css'
function Login() {
  return (
    <div className="login-form">
      <h6>email:</h6>
      <input
        type="email"
        className="form-control"
        id="correo"
        placeholder="Ingrese su correo"
      />
      <br /> <br />
      <input
        type="password"
        className="form-control"
        id="password"
        placeholder="Introduzca su contraseña"
      />
    </div>
  );
}

export default Login;