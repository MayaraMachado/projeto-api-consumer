<?php include("includes/a_config.php");?>
<!DOCTYPE html>
<html>
<head>
	<?php include("includes/head-tag-contents.php");?>
	<meta charset="utf-8">
    <style>
    @import url(https://fonts.googleapis.com/css?family=Roboto:300);

.login-page {
  width: 360px;
  padding: 3% 0 0;
  margin: auto;
}
.form {
  position: relative;
  z-index: 1;
  background: #FFFFFF;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #007bff;
  width: 100%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}

.botao{
    font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #007bff!important; 
  width: 100%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,.form button:active,.form button:focus {
  background: #43A047;
}
.form .message {
  margin: 15px 0 0;
  color: #b3b3b3;
  font-size: 12px;
}
.form .message a {
  color: #4CAF50;
  text-decoration: none;
}
.form .register-form {
  display: none;
}
.container {
  position: relative;
  z-index: 1;
  max-width: 300px;
  margin: 0 auto;
}
.container:before, .container:after {
  content: "";
  display: block;
  clear: both;
}
.container .info {
  margin: 50px auto;
  text-align: center;
}
.container .info h1 {
  margin: 0 0 15px;
  padding: 0;
  font-size: 36px;
  font-weight: 300;
  color: #1a1a1a;
}
.container .info span {
  color: #4d4d4d;
  font-size: 12px;
}
.container .info span a {
  color: #000000;
  text-decoration: none;
}
.container .info span .fa {
  color: #EF3B3A;
}
body {
  /* background: #007bff; fallback for old browsers */
  /* background: -webkit-linear-gradient(right, #76b852, #8DC26F); */
  /* background: -moz-linear-gradient(right, #76b852, #8DC26F); */
  /* background: -o-linear-gradient(right, #76b852, #8DC26F); */
  /* background: linear-gradient(to left, #76b852, #8DC26F); */
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;      
}
    </style>
</head>
<body>
<?php include("includes/design-top.php");?>

<SCRIPT LANGUAGE="JavaScript">

function Login() {
  var done=0;
  var usuario = document.getElementsByName('usuario')[0].value;
  usuario=usuario.toLowerCase();
  var senha= document.getElementsByName('senha')[0].value;
  seha=senha.toLowerCase();
  if (usuario=="admin" && senha=="admin") {
    window.location="/projeto-api-consumer/php-proj/index.php";
    done=1;
  }
  if (done==0) { alert("Dados incorretos, tente novamente"); }
}

</SCRIPT>

<body>

<div class="login-page">
  <div class="form">
    <!-- <form class="register-form">
      <input type="text" placeholder="name"/>
      <input type="password" placeholder="password"/>
      <input type="text" placeholder="email address"/>
      <button>create</button>
      <p class="message">Already registered? <a href="#">Sign In</a></p>
    </form> -->
    <form class="login-form">
      <input type="text" placeholder="username" name="usuario"/>
      <input type="password" placeholder="password" name="senha"/>
      <input type="button" onclick="Login()" class="botao" value="Login">
      <!-- <p class="message">Not registered? <a href="#">Create an account</a></p> -->
    </form>
  </div>
</div>

<!-- <div id="all">
  <div id="login-box">
    <div id="login-header">
      Faça login no sistema
    </div>
    <div id="login-inputs">
      <input type="text" placeholder="Nome de usuário" name="usuario">
      <br />
      <input type="password" placeholder="Senha" name="senha">
    </div>
    <div id="enviar">
      <input type="button" onclick="Login()" class="botao" value="Login">
      <a href="#">Esqueceu a sua senha?</a>
    </div>
  </div>
</div> -->

</body>
</html>

