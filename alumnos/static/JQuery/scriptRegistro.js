$(document).ready(function(){
    $("#registrar").click(function(e){
        var nombre = $("#id_username").val();
        var correo = $("#id_email").val();
        var confirmarCorreo = $("#id_confirmarcorreo").val();
        var pass =$("#id_password1").val();
        var conPass = $("#id_password2").val();
        var passRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$/;
        var isValid = true;
        var validacionCorreo=/^[a-zA-Z0-9._%+-]+@(gmail|hotmail)\.(com|cl)$/;
        e.preventDefault();

        

        if(nombre == "" || nombre== null || nombre.length>20|| nombre.length<10){
            $("#errorNombre").fadeIn();
            isValid = false;
        } 
        else{
            $("#errorNombre").fadeOut();
            if(!passRegex.test(pass)){
                $("#errorpassword").fadeIn();
                isValid = false;
            }
            else{
                $("#errorpassword").fadeOut();

                if(conPass != pass || conPass == null || conPass == ""){
                    $("#errorConf").fadeIn();
                    isValid = false;
                }
                else{
                    $("#errorConf").fadeOut();

                    if (correo === "" || correo === null) {
                        $("#errorCorreo").fadeIn();
                        isValid = false;
                    } else {
                        $("#errorCorreo").fadeOut();
                        if (!validacionCorreo.test(correo)) {
                            $("#errorCorreoFormato").fadeIn();
                            isValid = false;
                        } else {
                            $("#errorCorreoFormato").fadeOut();
                            if (correo !== confirmarCorreo) {
                                $("#errorConfCorreo").fadeIn();
                                isValid = false;
                            } else {
                                $("#errorConfCorreo").fadeOut();
                            }
                        }
                    }
                           
            }
            
    }
        }
        if(isValid){
            $("#formulario").submit();
        }
    } 
  
   
   )});



