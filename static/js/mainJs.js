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

    $.get( "/search", { checkIn: checkIn, checkOut: checkOut } ,function(res){
        var listings = $.parseJSON(res);
        var jsonLen = listings.length;
        var inner = "";
        var price;
        var curRes;
        for (var i = 0; i < jsonLen; i++){
                curRes = listings[i];
                inner += "<div class='row'><div class='col-lg-12' align='center' style='margin-bottom: 20px'><h6>" + curRes['sdate'] + "</h6></div></div>";
                inner += "<div class='row'><div class='col-lg-5' align='right' style='margin-top: 45px'><div class='row'><h4>$" + curRes['price'] + "</h4></div></div><div class='col-lg-7' align='left' style='margin-bottom: 20px'><a href='"+curRes['href']+"' target='_blank'><img class='img-circle' src='" + curRes['imurl'] + "' width='180' height='160' alt=''/></a></div></div>"
        }
        inner += "<div class='row'><div class='col-lg-12' align='center'><h6>" + listings[jsonLen-1]['edate'] + "</h6></div></div>";
        document.getElementById("resultContainer").innerHTML=inner;
    });

});


$('#scrollDown').click(function(){
    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});



$body = $("body");

$(document).on({
    ajaxStart: function()
    {
        $body.addClass("loading");
    },
    ajaxStop: function() {
        $body.removeClass("loading");

        $('html, body').animate({scrollTop:950},1000);
    }
});
//result();
