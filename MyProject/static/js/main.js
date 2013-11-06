$(document).ready(function() {
// 登录
    $("#page_login").click(function(){
       $('#modal_login').modal();
    })
    $("#page_register").click(function(){
       $('#modal_register').modal();
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

// 注册
    $("#id_modal_register").click(function() {
        var name = $("#modal_name_register").val();
        var email = $("#modal_email_register").val();
        var password = $("#modal_password_register").val();
        var repassword = $("#modal_repassword_register").val();
        if (name && email && password && repassword){
            if (password != repassword){

                return false
            }
           $.ajax({
                type: "post",
                data: $('#modal_register_form form').serialize(),
                url: "http://127.0.0.1:8000/accounts/register-ajax/",
                cache: false,
                dataType: "json",
                success: function(data, textStatus){
                    window.location.reload();
                },
                error: function () {
                   $("#modal_login_error").show();
                }
           });
        }
    });

});