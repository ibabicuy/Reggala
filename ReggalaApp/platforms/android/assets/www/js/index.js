/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

var toastHTML;

// Custom toast object. Used to show messages. Uses a custom toast messsage if the cordova-plugin-toast is not installed.
var toast;

document.addEventListener("deviceready", function () {	//evento cordova ready
    toast={
        toast: function(text) {

            if ("plugins" in window && "toast" in window.plugins){
                window.plugins.toast.showLongBottom(text); //toast plugin
            }else{
                // Custom Toast Message Logic
                if(toastHTML != null){
                    toastHTML.fadeOut(300)
                }
                toastHTML=$("<div class='toastMsg' style='display: none'>" + text + "</div>")
                $('#mui-viewport').append(toastHTML)
                toastHTML.fadeIn(400,function(){setTimeout(function(){toastHTML.fadeOut(300)},3000)}); //fade out after 3 seconds
                toastWidth = (-toastHTML.outerWidth())/2;
                toastHTML.css({"margin-left":toastWidth + "px"})
            }
        }
    }

    function getHumidity(){

        $.ajax({
            url:"http://192.168.4.107:3080/getCurrentHumidityValue",
            type:"GET",
            success: function(data){
                toast.toast("Humidity is " + data)
                $("#humidityInput").val(data)
            },
            error: function(xhr, status, error){

                toast.toast(JSON.stringify(xhr))
            }
        })
    }


    $("#humidityInput").on("change",function(){
        if($(this).val() > 100){
            $(this).val(100)
        }else if($(this).val() < 0){
            $(this).val(0)
        }
    })

    $('.submitBtn').click(function(){
        var hVal = $("#humidityInput").val();
        if(hVal == "") hVal=0;
        $.ajax({
            url: 'http://192.168.4.107:3080/changeHumidity',
            type: 'POST',
            data: JSON.stringify({ action: "changeHumidity", value : hVal ,plant_id:1}) ,
            success: function (data) {
                //toast.toast("New value saved: " + data);
                getHumidity()

            },
            error: function (xhr, status, error){
                toast.toast(JSON.stringify(xhr))
            }
        });
    })

    getHumidity();



})