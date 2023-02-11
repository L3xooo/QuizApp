$('.choice').on("click",function(){

    var checkbox = $(this).children("input[type = 'checkbox']");
    var siblings = $(this).siblings()
    siblings.removeClass("active")    //Remove other active class
    console.log(siblings)

    checkbox.prop("checked",!checkbox.prop("checked"))                      //Will check the checbox with clicking on div "choice"
    $('input[id="' + (this.id) + '"]').not(checkbox).prop("checked",false); //No other inputs checked

    $(this).addClass("active")      //Add active class to div "Choice" where is input checked

});