/**
 * Created by dermersean on 26/11/2015.
 */

var foods = [['Black and White Affogato', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/05/Black-and-White-Affogato1-410x546.jpg'],
    ['Marvelous Meatballs!', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/04/Meatballs1-410x307.jpg'],
    ["Lia's Dark Chocolate Truffles", 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2010/12/5240497441_3188a021b4_o-420x280.jpg'],
    ['Spice Rubbed Flank Steak', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2014/10/Coffee-7-410x273.jpg'],
    ['Mile High Caramel Bars', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/05/0061-410x361.jpg'],
    ['Lentil Vegetable Soup with Whipped Feta', 'https://s-media-cache-ak0.pinimg.com/736x/24/87/2a/24872a474b46b4b821d788d560369cb4.jpg'],
    ['Lentil, Rice, and Raisin Pilaf', 'http://1.bp.blogspot.com/-3zKMEryxu1c/UnaoXYCkbyI/AAAAAAAAgN4/g5LVy6QBD7E/s1600/Persian-rice-pilaf-and-lentil.jpg'],
    ['Roasted Garlic Dungeness Crab', 'http://media-cache-ak0.pinimg.com/736x/e8/6b/0e/e86b0e4fb7caff9666526fccd9f416ee.jpg'],
    ['Whole Wheat Peanut Butter Chocolate Bread', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/03/DSCN5435-410x307.jpg'],
    ['Spicy Chipotle Shrimp Skewers', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/05/spicy-chipotle-shrimp-skewers-cropped-410x307.jpg'],
    ['Szechwan Green Beans', 'http://julievr.wpengine.netdna-cdn.com/wp-content/uploads/2012/05/Szechuan-green-beans-2.jpg'],
    ['Roasted Brussels Sprouts with Winter Squash', 'http://www.ihavenet.com/images/Roasted-Brussels-Sprouts-and-Winter-Squash-Recipe_DRW_12031.jpg'],
    ['Spinach and Mushroom Lasagna', 'http://www.jewelosco.com/wp-content/uploads/2014/10/spinach-mushroom-lasagna.png'],
    ['Sweet and Savoury Stir Fried Pork and Cashews', 'http://media-cache-ak0.pinimg.com/736x/64/da/75/64da751276ee12b7ca026593e3f9fb05.jpg'],
    ['Lentil, Walnut and Raisin Salad with Red Peppers','http://media-cache-ak0.pinimg.com/736x/c5/c2/84/c5c284de5cef2668ec155b13dcb008da.jpg'],
    ['Taco Flavored Ground Turkey', 'http://consumerrecipe.conagrafoods.com/uploadedImages/img_7417_7275.jpg'],
    ['Light BBQ Chicken Pizza', 'http://media-cache-ec0.pinimg.com/736x/a7/3c/92/a73c921920b09594507db1b4e31b80aa.jpg'],
    ['Pecan Pie Caramel Cheesecake', 'http://media-cache-ak0.pinimg.com/736x/fa/39/27/fa3927cc7f3bb009f00a893727c7beab.jpg'],
    ['Quick and Easy Cinnamon Walnut Bread', 'http://media-cache-ak0.pinimg.com/736x/5b/1f/32/5b1f3294830e0c2fdcbbdc491b247417.jpg'],
    ["Mom's Famous BBQ Pulled Chicken", 'http://www.eatingwell.com/sites/default/files/imagecache/standard/recipes/MP5102A_Scrivani.JPG']]

suggestions();

var lastScrollTop = 0;
$(window).scroll(function(event){
    var st = $(this).scrollTop();
    if (st > lastScrollTop){
        $("#fork").animate({right:"-=20"});
    } else {
        $("#fork").animate({right:"+=20"});
    }
    lastScrollTop = st;
});

$('#suggestions').click(function(){
    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 1500);
    return false;
});

$('#submitSearch').click(function()
{
    var searchWord = $('#searchFood').val();
    var json = {query:searchWord};
    alert("holly");
    $.post('/commitSearch',json,function(data) {
        alert("gi");
        data = $.parseJSON(data);
        alert(data);
    }).done(function(data){alert(data);}).fail(function(){alert("2");}).always(function(){alert("4");}).ontimeout(function(){alert("ARGGGGGGG");});
});

function suggestions()
{
    var inner = "<div class='row'>";
    $.each(foods,function(index, value)
    {
            inner += "<div id='img" + index +"' class='col-lg-3'><img class='img-circle floater' src='" + value[1] + "' width='180' height='160' alt=''/><h4>" + value[0] + "</h4></div>";
            if(index % 4 == 3)
            {
                inner+="</div><div class='row'>";
            }
    });
    inner += "</div>";
    document.getElementById("foodContainer").innerHTML=inner;
}


