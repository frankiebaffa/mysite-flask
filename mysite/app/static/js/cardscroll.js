$(function() {
    var sum = 0;
    var grandwidth = $("body").width();
    $(".projectcontainer .listcontainer .cardlist .card").each(function(){sum += $(this).width()});
    $(".projectcontainer .listcontainer .cardlist").css('width', sum*1.25);
    $(".listcontainer").css('width', grandwidth);
});

$(function() {
    var sum = 0;
    var grandwidth = $("body").width();
    $(".blogcontainer .listcontainer .cardlist .card").each(function(){sum += $(this).width()});
    $(".blogcontainer .listcontainer .cardlist").css('width', sum*1.25);
    $(".listcontainer").css('width', grandwidth);
});

$(function() {
    var sum = 0;
    var grandwidth = $("body").width();
    $(".articlecontainer .listcontainer .cardlist .card").each(function(){sum += $(this).width()});
    $(".articlecontainer .listcontainer .cardlist").css('width', sum*1.25);
    $(".listcontainer").css('width', grandwidth);
});

$(window).resize(function() {
    var sum = 0;
    var grandwidth = $("body").width();
    $(".projectcontainer .listcontainer .cardlist .card").each(function(){sum += $(this).width()});
    $(".projectcontainer .listcontainer .cardlist").css('width', sum*1.25);
    $(".listcontainer").css('width', grandwidth);
});

$(window).resize(function() {
    var sum = 0;
    var grandwidth = $("body").width();
    $(".blogcontainer .listcontainer .cardlist .card").each(function(){sum += $(this).width()});
    $(".blogcontainer .listcontainer .cardlist").css('width', sum*1.25);
    $(".listcontainer").css('width', grandwidth);
});

$(window).resize(function() {
    var sum = 0;
    var grandwidth = $("body").width();
    $(".articlecontainer .listcontainer .cardlist .card").each(function(){sum += $(this).width()});
    $(".articlecontainer .listcontainer .cardlist").css('width', sum*1.25);
    $(".listcontainer").css('width', grandwidth);
});
