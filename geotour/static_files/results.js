var listTypes = ["poiList", "foodList", "shopList"];

var toggleList = function(type) {
    $("#"+type).show();

    for (var i = 0; i < listTypes.length; i++) {
        if (listTypes[i] != type) {
            $("#"+listTypes[i]).hide();
            console.log(listTypes[i] + " is hidden!");
        }
    }

};

var openGoogleMaps = function() {
    alert("Need to make maps pop up!");
};

var resizePage = function() {
    var H = 600;
    var sidebarH = $("nav").height();
    var articleH = $("article").height();

    if ((sidebarH < H) && (articleH < H)){
        // nothing to do, H is already default size
    }
    else{
        if (sidebarH < articleH){
            H = articleH;
        } else{
            H = sidebarH;
        }
    }
    $("article").css({'height': H});
    $("nav").css({'height': H});
};

$(window).load(function() {
    resizePage();
    document.getElementById("gMapIcon").addEventListener("click", openGoogleMaps);
});

