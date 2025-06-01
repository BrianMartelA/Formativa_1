function esconder(input,icon) {
  var contra = document.getElementById(input);
  var eyeid=  document.getElementById(icon)

  if (contra.type === "password") {
    contra.type="text"
    eyeid.src = "/static/img/icons8-visible-16.png";
    


  }
  else {
    contra.type="password"

    eyeid.src = "/static/img/icons8-ojo-cerrado-16.png";
  }
}

function empty(input) {
  var borrar =document.getElementById(input)
  borrar.value = "";
}
