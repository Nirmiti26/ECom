var height = $('#greenesto_header').innerHeight();
console.log(height);
window.onscroll = function () {
    hideHeader();
    console.log("YEs called");
};

////////////////////////  Saving Form Validating Functions /////////////////////////

function validBill() {
        var bill = document.forms['form']['bill'].value;
        if (isNaN(bill) || bill == null){
            $('#bill').css('border-color','#d50000');
            $('#bill').css('box-shadow', '0 1px 1px rgba(0, 0, 0, 0.075) inset, 0 0 8px #d50000');
        }
        else{
            $('#bill').css('border-color','transparent');
            $('#bill').css('box-shadow', 'none');
        }
    }
    function validPincode() {
        var pincode = document.forms['form']['pincode'].value;
        if (isNaN(pincode)){
            $('#pincode').css('border-color','#d50000');
            $('#pincode').css('box-shadow', '0 1px 1px rgba(0, 0, 0, 0.075) inset, 0 0 8px #d50000');
        }
        else{
            $('#pincode').css('border-color','transparent');
            $('#pincode').css('box-shadow', 'none');
        }
    }
    function validConnectionLoad() {
        var connection_load = document.forms['form']['connection_load'].value;
        if (isNaN(connection_load)){
            $('#connection_load').css('border-color','#d50000');
            $('#connection_load').css('box-shadow', '0 1px 1px rgba(0, 0, 0, 0.075) inset, 0 0 8px #d50000');
            return -1;
        }
        else{
            $('#connection_load').css('border-color','transparent');
            $('#connection_load').css('box-shadow', 'none');
            return connection_load
        }
    }
    function validArea() {
        var roof_area = document.forms['form']['roof_area'].value;
        if (isNaN(roof_area)){
            $('#roof_area').css('border-color','#d50000');
            $('#roof_area').css('box-shadow', '0 1px 1px rgba(0, 0, 0, 0.075) inset, 0 0 8px #d50000');
        }
        else{
            $('#roof_area').css('border-color','transparent');
            $('#roof_area').css('box-shadow', 'none');
        }
    }

////////////////////////////// Charts ////////////////////////////////////////

function get_25year_data(connection_load) {
    var yearly_bill = document.forms['form']['bill'].value*12;
    var yearly_saving_units;
    if ((yearly_bill) < connection_load*1535*8)
    {
        yearly_saving_units = yearly_bill/8;
    }
    else
    {
        yearly_saving_units = 1535*connection_load;
    }
    var yearly_saving = yearly_saving_units*8;
    var yearly_remaining = yearly_bill - yearly_saving;

    var ret=[];
    for (var i=1;i<=5;i++){

        ret.push({
            x: i,
            a: yearly_bill*i,
            b: (yearly_remaining).toFixed(2)*i
        });
    }
    return ret;
}

function getSystemCost(connection_load) {
    var cost=0;
    if(connection_load >=2 && connection_load <=10){
        cost = connection_load * 90000 * 0.889
    }
    else if ( connection_load >=11 && connection_load <=29){
        cost = connection_load * 90000 * 0.87
    }
    else if ( connection_load >=30 && connection_load <=39){
        cost = connection_load * 90000 * 0.86
    }
    else if ( connection_load >=40 && connection_load <=79){
        cost = connection_load * 90000 * 0.85
    }
    else if ( connection_load >=80 && connection_load <=100){
        cost = connection_load * 90000 * 0.845
    }
    else{
        alert("Please enter connection load between 1 to 100");
    }
    return cost;
}

function drawSystemCost(cost) {
    var data1 = "<h1 style=\"color: white; font-size: 20px; font-family: 'Wellfleet'; text-align: center\">System Cost</h1><h1 style=\"color: white; font-size: 60px; font-family: 'Wellfleet';text-align: center\"><span class=\"fa fa-rupee\"></span> ";
    var data2 = "</h1>";
    document.getElementById('card2Chart').innerHTML = data1 + cost.toString() + data2;
}


function get_1year_saving_units(connection_load) {
    var bill = document.forms['form']['bill'].value;
    var saving;
    if ((bill*12)/8 < connection_load*1535)
    {
        saving = 100;
    }
    else
    {
        saving = ((1535*connection_load*8)/(bill*12))*100;
        saving = saving.toFixed(2);
    }
    var ret = [];
    ret.push({
        label: "Saving", value: saving
    });
    ret.push({
        label: 'Payable', value: 100-saving
    });
    return ret;
}

function updateDonut(connection_load) {
    donut.setData(get_1year_saving_units(connection_load));
}

function makeRoof(percentage) {
    $('td').css('background-color','transparent');
    var cells = Math.ceil(percentage/2);
    var rows = Math.floor(cells/10);
    var extra_cells = cells%10;
    $('#roofTopText').text(percentage+'%');
    for(var r=1;r<=rows;r++){
        for (c=1;c<=10;c++){
            var id = '#'+r.toString()+'-'+c.toString();
            $(id).css('background-color','white');
        }
    }
    rows++;
    for (var c=1;c<=extra_cells;c++){
        var id = '#'+rows.toString()+'-'+c.toString();
            $(id).css('background-color','white');
    }
}

function get_slider() {
    $("#ex6").slider();
    $("#ex6").on("slide", function(slideEvt) {
        $("#ex6SliderVal").text(slideEvt.value+'kW');
        makeRoof(get_roof(slideEvt.value));
        updateLine(get_25year_data(slideEvt.value));
        updateDonut(slideEvt.value);
        drawSystemCost(getSystemCost(slideEvt.value));


    });
}

function updateLine() {
    graph.setData(get_25year_data(document.forms['form']['connection_load'].value));
}

function get_roof(connection_load) {
    var roof_area = document.forms['form']['roof_area'].value;
    var panel_area = connection_load*120;
    return Math.ceil((panel_area/roof_area)*100);
}
//////////////////////////// Functions to be called when website is refreshed /////////////////////
//// function called at start
$(function () {
    get_slider();
    drawSystemCost(getSystemCost(document.forms['form']['connection_load'].value));
    makeRoof(get_roof(document.forms['form']['connection_load'].value));
});

//// code to make line chart ////
var graph = Morris.Line({
     element: 'card4Chart',
     data: get_25year_data(document.forms['form']['connection_load'].value),
     xkey: 'x',
     ykeys: ['a','b'],
     labels: ['Before', 'After'],
     lineColors: ['black','white'],
     parseTime: false,
 });

//// code to make donut chart ////
var donut = Morris.Donut({
    element: 'card5Chart',
    data: [
        {label: "Savings", value: 12},
        {label: "Payable", value: 30}
    ],
    colors: ['#e65100','#311b92']
});

//////////////////////////// Function to be called when saving button is pressed /////////////////

function generateCharts() {
    get_slider();
    drawSystemCost(getSystemCost(document.forms['form']['connection_load'].value));
    updateLine(get_25year_data(document.forms['form']['connection_load'].value));
    updateDonut();
    makeRoof(get_roof(document.forms['form']['connection_load'].value));

}

//////////////////////////// Function to be called when windows resizes /////////////////

$(window).resize(function () {
    updateLine(get_25year_data(document.forms['form']['connection_load'].value));
    updateDonut(document.forms['form']['connection_load'].value);
});

//////////////////////////// Function to be called when slider changes its values //////////////////


/******************************** /JS for Carousel height ***************************/

function setCarouselHeight(carousel, image){
    var img_id = image.attr('id');
    var carousel_id = carousel.attr('id');
    var img_height = document.getElementById(img_id).offsetHeight;
    document.getElementById(carousel_id).css('height', img_height);

}
/*****************************  /JS for Header Buttons /******************************/

function createStrip(button_Id) {
    $('#'+button_Id).css('background-color', '#FFC400');
    console.log("In");
}
function removeStrip(button_Id) {
    $('#'+button_Id).css('background-color', '#FFF');
    console.log("Out");
}
function print() {
    console.log("HELLO");
}

/**************************** /JS for Header Animations ******************************/


function hideHeader() {
    var scrollTop = $(window).scrollTop();
    if(scrollTop > height){
        $('.header-part2').css('transition-duration','1s');
        $('.header-part2').css('height','0');
        $('.header-part2').css('overflow','hidden');

    }
    else{
        $('.header-part2').css('height','auto');
    }
}