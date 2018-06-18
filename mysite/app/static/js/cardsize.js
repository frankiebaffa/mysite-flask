$(function() {
    var width = $(".card").width()
    $(".card").css("height", (width*1.35));
});

$(window).resize(function() {
    var width = $(".card").width();
    $(".card").css("height", (width*1.35));
});
