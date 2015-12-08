/**
 * Created by dermersean on 26/11/2015.
 */

$('#submitSearch').click(function()
{
    var checkIn = document.getElementById("CheckIn").value;
    var checkOut = document.getElementById("CheckOut").value;
    checkIn = checkIn + ' 00:00:00';
    checkOut = checkOut + ' 00:00:00';
    checkIn = moment(checkIn).unix();
    checkOut = moment(checkOut).unix();
    checkIn += 86400;
    checkOut += 86400;

    document.getElementById("in").innerHTML = checkIn;
    document.getElementById("out").innerHTML = checkOut;

    $.get( "/search", { checkIn: checkIn, checkOut: checkOut } ,function(res){
        var inner = "";
        $.each(res["results"],function(i, value)
        {
            inner += "<div class='row'><div class='col-lg-12' align='center'><h4>" + value.sdate + "</h4></div></div>";
            inner += "<div class='row'><div class='col-lg-5' align='right'><div class='row'><h4>" + value.name + "</h4></div><div class='row'><h4>" + value.price + "</h4></div></div><div class='col-lg-7' align='left'><img src='" + value.imurl + "' width='180' height='160' alt=''/></div></div>"
        });
        document.getElementById("resultContainer").innerHTML=inner;
    });

});

//$('#arrow').bind('mouseenter', function(){
//    alert('hi');
//    $('#arrow').animate({up:"10"});
//});


$('#scrollDown').click(function(){
    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});


//function result()
//{
//    var inner = "";
//    $.each(res["results"],function(i, value)
//    {
//        inner += "<div class='row'><div class='col-lg-12' align='center'><h4>" + value.sdate + "</h4></div></div>";
//        inner += "<div class='row'><div class='col-lg-5' align='right'><div class='row'><h4>" + value.name + "</h4></div><div class='row'><h4>" + value.price + "</h4></div></div><div class='col-lg-7' align='left'><img src='" + value.imurl + "' width='180' height='160' alt=''/></div></div>"
//    });
//    document.getElementById("resultContainer").innerHTML=inner;
//}
//
$body = $("body");

$(document).on({
    ajaxStart: function()
    {
        $body.addClass("loading");
    },
    ajaxStop: function() {
        $body.removeClass("loading");
    }
});
//result();
