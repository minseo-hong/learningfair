$(document).ready(function() {
    isPost = $('.start-btn').data('ispost');
    if (isPost !== 'True') {
        $('.start-btn').attr('disabled', 'disabled');
    }

    $('.article-input').on('input', function() {
        if ($(this).val() !== '') {
            $('.start-btn').removeAttr("disabled");
        } else {
            $('.start-btn').attr('disabled', 'disabled');
        }
    });
});