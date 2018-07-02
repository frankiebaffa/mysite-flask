$(document).ready(function() {
    var modalabout = $('#modalabout');
    var btnabout = $("a[title|='About']");
    var navcollapse = $("select[class='navbar-toggle collapsed']");

    btnabout.removeAttr('href');
    btnabout.click(function() {
        $('#modalabout').css('display', 'block');
        navcollapse.click();
    });
    modalabout.click(function() {
        modalabout.css('display', 'none');
    });

});
    
