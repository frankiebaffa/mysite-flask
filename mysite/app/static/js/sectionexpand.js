$(function() {
    var height1 = $('.subhead').height();
    var height2 = $('.contentcontainer').height();
    var height3 = $('.pagecard').height();
    var height4 = height1 + height2 + height3;
    $('.gencontainer').css('height', height4*1.1);
    //if (heightdoc > grandheight) {
    //    $('.gencontainer').css('height', heightdoc);
    //} else {
    //    $('.gencontainer').css('height', grandheight);
    //}
});

$(window).resize(function() {
    var height1 = $('.subhead').height();
    var height2 = $('.contentcontainer').height();
    var height3 = $('.pagecard').height();
    var height4 = height1 + height2 + height3;
    $('.gencontainer').css('height', height4*1.1);
    //if (heightdoc > grandheight) {
    //    $('.gencontainer').css('height', heightdoc);
    //} else {
    //    $('.gencontainer').css('height', grandheight);
    //}
});
