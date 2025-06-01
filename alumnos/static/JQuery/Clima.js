$(document).ready(function () {
    console.log('Documento listo');
    $.get("https://api.weatherapi.com/v1/forecast.json?key=d827b6f0df87409b9b7222808240205&q=Santiago&aqi=yes  &days=10", function (data) {
        console.log('datos recibidos : ', data);


        $.each(data.forecast.forecastday, function (i, item) {
            $("#day").append(`<tr><td style="border: 1px solid" > ${item.date}</td>
                <td style="border: 1px solid">${item.day.avgtemp_c}°C</td><td style="border: 1px solid"> ${item.day.condition.text}</td></tr>`);

        });

    });




});