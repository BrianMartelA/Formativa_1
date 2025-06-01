function validarFormulario(){
    //removemos el div con la clase alert
    $('.alert').remove();

    //declaracion de variables
    var nombre=$('#nombre').val(),
        correo=$('#correo').val(),
        asunto=$('#asunto').val(),
        mensaje=$('#mensaje').val();

    //validacion nombre
    if(nombre=="" || nombre==null){
        cambiarColor("nombre");
        //mostrar mensaje de alerta
        mostrarAlerta("Campo obligatorio.");
        return false;
    }else{
        var expresion= /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(nombre)){
            //mostrara el mensaje que debe ingresar un nombre valido
            cambiarColor( "nombre" );
            mostrarAlerta("No se permiten caracteres especiales o numericos");
            return false;
        }
    }

    //validacion correo
    if(correo=="" || correo==null){
        cambiarColor("correo");
        //mostrar mensaje de alerta
        mostrarAlerta("Campo obligatorio.");
        return false;
    }else{
        var expresion= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if(!expresion.test(correo)){
            //mostrara el mensaje que debe ingresar un nombre valido
            cambiarColor( "correo" );
            mostrarAlerta("Por favor ingresar un correo válido");
            return false;
        }
    }

    //validacion asunto
    if(asunto=="" || asunto==null){
        cambiarColor("asunto");
        //mostrar mensaje de alerta
        mostrarAlerta("Campo obligatorio.");
        return false;
    }else{
        var expresion= /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(asunto)){
            //mostrara el mensaje que debe ingresar un nombre valido
            cambiarColor( "asunto" );
            mostrarAlerta("No se permiten caracteres especiales o numericos");
            return false;
        }
    }

    //validacion mensaje
    if(mensaje=="" || mensaje==null){
        cambiarColor("mensaje");
        //mostrar mensaje de alerta
        mostrarAlerta("Campo obligatorio.");
        return false;
    }else{
        var expresion= /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(mensaje)){
            //mostrara el mensaje que debe ingresar un nombre valido
            cambiarColor( "mensaje" );
            mostrarAlerta("No se permiten caracteres especiales o numericos");
            return false;
        }
    }

    $('form').submit();
    return true;
    
}

$('input').focus(function(){
    $('.alert').remove();
    colorDefault('nombre');
    colorDefault('correo');
    colorDefault('asunto');
});

$('textarea').focus(function(){
    $('.alert').remove();
    colorDefault('mensaje');
});

//funcion color por defecto de los bordes de los inputs
function colorDefault(dato){
    $('#' + dato).css({
        border: '1px solid #999'
    });
}
//funcion para cambiar de color al borde del input cuando este detecte un error
function cambiarColor(dato){
    $('#' + dato).css({
        border: '1px solid #dd5144'
    });
}

//funcion para mostrar la alerta
function mostrarAlerta(texto){
    $('#nombre').before('<div class="alert">Error: '+ texto +'</div>');
}