$(document).ready(function(){
    $("#button").click(function(){
        changeHumidityValue();
    })
})
function changeHumidityValue(){
    console.log($("#value").val())
    $.ajax({
        url: 'http://10.252.252.119:3080/humidityData',
        type: 'POST',
        data: { action: "changeHumidity", value : $("#value").val() ,plant_id:1} ,
        success: function (response) {
            alert(response.status);
            window.location = "indice.html";
        },
        error: function () {
            alert("error");
            window.location = "indice.html";
        }
    });
}