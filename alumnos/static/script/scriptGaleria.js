$(document).ready(function(){
    $("#registrar").click(function(){
        var nombre = $("#user").val();
        var correo = $("#correo").val();
        var confirmarCorreo = $("#confirmar_correo").val();
        var pass =$("#contrasena").val();
        var conPass = $("#confirmarContrasena").val();
        var emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        var passRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$/;

        if(!emailRegex.test(correo)){
            $("#errorCorreo").fadeIn();
            return false;
            
        }
        else{
            $("#errorCorreo").fadeOut();  
            if(confirmarCorreo !== correo){
                $("#errorConfirmarCorreo").fadeIn();
                return false;
            }
            else{
                $("#errorConfirmarCorreo").fadeOut();
                if (nombre > 20 || nombre < 5 || nombre==null){
                    $("#errorUser").fadeIn();
                    return false;

                }
                else{
                    $("#errorUser").fadeOut();
                    if(!passRegex.test(pass)){
                        $("#errorPass").fadeIn();
                        return false;

                    }
                    else{
                        $("#errorPass").fadeOut();
                        if(pass !== conPass){
                            $("#errorConfirmarPass").fadeIn();
                            return false;
                        }
                        else{
                            $("#errorConfirmarPass").fadeOut();
                            alert("Datos guardados")

                        }
                    }


                }
            }
        }
    
    
    })
   



})