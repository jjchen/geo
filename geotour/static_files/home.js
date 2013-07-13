

var addEndField = function() {
    $("#endField").show();
    $("#showEndFieldText").hide();
    $("#showEndField").css("padding-top", "10px");
};


$(document).ready(function() {
    $("#dateInput").datepicker();
    $(".timeInput").timepicker();
});
