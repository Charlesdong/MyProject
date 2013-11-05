$(document).ready(function() {
    $("#page_login").click(function(){
       $('#modal_login').modal();
    })

    $("#id_modal_login").click(function(){
        var email = $("#modal_email").val();
        var password = $("#modal_password").val();

        if (email && password){
            $.ajax({
                type: "POST",
                data: $('#modal_login_form form').serialize(),
                url: "http://127.0.0.1:8000/accounts/login-ajax/",
                cache: false,
                dataType: "json",
                success: function(data, textStatus){
                    window.location.reload();
                },
                error: function () {
                   $("#modal_login_error").show();
                }
            });
        }else{
            $("#modal_login_error").show();
        }
    });

});