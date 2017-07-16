$(document).ready(function () {
    //get language from session and change the page lang if necessary
    var lang = sessionStorage.getItem('lang');
    var h = window.location.href;
    var changeLang = false;
    if (lang == 'en') {
        $('#en_lang').addClass('active');
        $('#fa_lang').removeClass('active');
        // check if the url and lang are same or not
        if (h.indexOf('fa') != -1 && h.indexOf('fa') < 20) {
            h = h.replace('/fa/', '/en/');
            changeLang = true;
        }

    } else if (lang == 'fa') {
        $('#fa_lang').addClass('active');
        $('#en_lang').removeClass('active');
        if (h.indexOf('en') != -1 && h.indexOf('en') < 20) {
            h = h.replace('/en/', '/fa/');
            changeLang = true;
        }
    }
    if (changeLang) {
        window.location.href = h;
        changeLang = false;
    }

    //handle clicks on change lang buttons
    $('.change_lang').click(function () {
        var chosen_lang;
        if ($(this).attr('id') == 'en_lang') chosen_lang = 'en'; else chosen_lang = 'fa';
        if (chosen_lang == 'fa') {
            h = h.replace('/en/', '/fa/');
            sessionStorage.setItem('lang', 'fa');
            $('#fa_lang').addClass('active');
            $('#en_lang').removeClass('active');
        }
        else if (chosen_lang == 'en') {
            h = h.replace('/fa/', '/en/');
            sessionStorage.setItem('lang', 'en');
            $('#en_lang').addClass('active');
            $('#fa_lang').removeClass('active');
        }
        window.location.href = h;
    });
});