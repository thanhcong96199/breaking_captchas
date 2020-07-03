

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

    var posting = $.post(url, {'email': email, 'password': password, 'textcaptcha': textcaptcha, 'image': image, 'csrfmiddlewaretoken': csrfmiddlewaretoken})

    posting.done(function (data) {


    })

})
