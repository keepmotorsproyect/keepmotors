import React from "react";
import './login.css'
function Login() {
  return (
    <div className="login-form">
      <br />
      <h1>KeepMotors</h1>
      <br /><br />
      <h6>email:</h6>
      <input
        type="email"
        className="form-control"
        id="correo"
        placeholder="Ingrese su correo"
      />
      <br /> <br />

      <h5>Contraseña</h5>
      <input
        type="password"
        className="form-control"
        id="password"
        placeholder="Introduzca su contraseña"
      />
<br /> <br /> <br />
      <button type="button">Registrar</button>
    </div>
  );
}

export default Login;