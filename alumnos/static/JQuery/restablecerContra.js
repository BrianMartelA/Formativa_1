$(document).ready(function(){
    $("#recuperar").click(function(){
        var Pass = $("#id_new_password1").val();
        var conPass = $("#id_new_password2").val();
        var passRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$/;
        var isValid = true;
        event.preventDefault(); 




        if( Pass== '' ){
            $("#errorPass1").fadeIn();
            isValid = false;


        }
        else{
            $("#errorPass1").fadeOut();
            if(!passRegex.test(Pass)){
                $("#errorPassFormato").fadeIn();
                isValid = false;
    
            }

            else{
                $("#errorPassFormato").fadeOut()
                if(Pass != conPass){
                    $("#errorContra").fadeIn();
                    isValid = false;
                }

            }
            

        }
        if(isValid){
            $("#restablecerContra").submit();
        }

    } 
  
   
   )});



