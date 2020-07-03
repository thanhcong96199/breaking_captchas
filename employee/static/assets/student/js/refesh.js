

$("#btn_refesh").on("click", function () {

    $.ajax({
        url: '/api/get-image',
        method: 'GET',
        success: (data) => {
             $("#img_captcha_gender_refesh").attr('src', data.url)
            $('0')
        },
        error: (error)=>{

        }
    })

})

$(".form__login").submit(function (event) {

    event.preventDefault();
        var $form = $(this),
        email = $form.find("input[name='email']").val(),
        password = $form.find("input[name='password']").val(),
        textcaptcha = $form.find("input[name='textcaptcha']").val(),
        image = $form.find("img[id='img_captcha_gender_refesh']").attr('src'),
        url = $form.attr("action"),
        csrfmiddlewaretoken =  $form.find('input[name=csrfmiddlewaretoken').val();
    $.ajax({
        url: url,
        method: 'POST',
        data: {
            'email': email,
            'password': password,
            'textcaptcha': textcaptcha,
            'image': image,
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
        },
        success: (data)=>{
            debugger;
            console.log(data)
         if (data.error_email_password){
             $("#email_passwor_error").addClass('error_class');
             $("#email_passwor_error").html('Email or Password is wrong');

         } else {
            $("#email_passwor_error").removeClass('error_class');
         }
         if(data.error_captcha){
             $("#captcha_error").addClass('error_class');
             $("#captcha_error").html('Text of Captcha is wrong');

         }
         else{
             $("#captcha_error").removeClass('error_class');
         }
         if(data.success){
             window.location.href='/done'
         }

        }
    })


    // var posting = $.post(url, {'email': email, 'password': password, 'textcaptcha': textcaptcha, 'image': image, 'csrfmiddlewaretoken': csrfmiddlewaretoken})

    // posting.done(function (data) {
    //     console.log('dầdsf', data)
    //
    // })

})
