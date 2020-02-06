$(document).ready(function () {

    $('#load').click(function () {
        $.get('/ajax/data/', {}, function (data) {
            $('#my_test_div').html(data);
        });
    });

});