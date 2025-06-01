$(document).ready(function(){
    $("#Cambiar").click(function(){
       var pass = $("#id_password1").val();
       var correo = $("#id_email").val();
       var passRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$/;
       var isValid = true;
       var validacionCorreo=/^[a-zA-Z0-9._%+-]+@(gmail|hotmail)\.(com|cl)$/;
       event.preventDefault(); 

        if(correo === "" ){
            $("#errorCorreo").fadeIn();
            isValid=false

        }
        else{
            $("#errorCorreo").fadeOut();
            if(!validacionCorreo.test(correo)){
                $("#errorCorreoFormato").fadeIn();
                isValid=false;
            }
            else{
                $("#errorCorreoFormato").fadeOut();
                if(!passRegex.test(pass) || pass ===""){
                    $("#errorpassword").fadeIn();
                    isValid=false;
                }
            }
        }

     
        if(isValid){
            $("#formularioCambio").submit();
        }
    
    
    })
   });



