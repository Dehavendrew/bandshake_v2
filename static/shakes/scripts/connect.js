

function test(e){
    console.log(e)
}

eventname = ""
function invoke(){
    let band = event.target.getAttribute('bandID')
    eventname= event.target.getAttribute('event_name')
    band = 'BandShake_000' + band
    var list = con(band, eventname)
}

function con(band, eventObj) {
    band_service = '19B10000-E8F2-537E-4F6C-D104768A1214'
    band_char = '19B10001-E8F2-537E-4F6C-D104768A1214'
    connected = true
    navigator.bluetooth.requestDevice({
        filters: [{name: [band]}],
        optionalServices: [band_service.toLowerCase()]
    })
        .then(device => device.gatt.connect())
        .then(server => server.getPrimaryService(band_service.toLowerCase()))
        .then(service =>service.getCharacteristic(band_char.toLowerCase()))
        .then(characteristic => characteristic.startNotifications())
        .then(characteristic => {
                characteristic.addEventListener('characteristicvaluechanged',
                    handleCharacteristicValueChanged);

                console.log('Notifications have been started.');
        })
        .catch(error => {
            console.log(error.message);
        });
}

function handleCharacteristicValueChanged(event) {
    var value = event.target.value;
    console.log("sending data")
    $.ajax({
        url: "\\makeshake\\",
        type: "POST",
        data: { message : value.getUint8(0),
                event : eventname
        },
        success: function(json) {
            addToPage("Shake Detected!")
            addNewShakeToPage()
        }
    })
}

function addNewShakeToPage(){
        $.ajax({
        url: "\\makeshake\\",
        type: "GET",
        success: function(res) {
            addShake(res)
        }
    })
}

function addToPage(text){
    var element = document.createElement("div")
    element.innerHTML = text
    var bar = document.getElementById("live-box")
    bar.appendChild(element)
}

function addShake(data){
    var data_arr = data.split(',')
    var new_shake = document.createElement("article")
    new_shake.className = "media content-section"
    new_shake.id = data[0]
    new_shake.innerHTML = " <img class=\"rounded-circle article-img\" src=" + data_arr[3] + ">\n" +
        "              <div class=\"media-body\">\n" +
        "                <div class=\"article-metadata\">\n" +
        "                  First Impression &#x1F91D\n" +
        "                </div>\n" +
        "                <h2>\n" +
        "                    <a class=\"mr-2\" href=\"http://127.0.0.1:8000/user/"+ data_arr[2] + "/\">" + data_arr[2] + "</a>shook hands with\n" +
        "                    <a class=\"mr-2\" href=\"http://127.0.0.1:8000/user/"+ data_arr[4] + "/\">" + data_arr[4] + "</a>\n" +
        "                </h2>\n" +
        "                <p class=\"article-content\"> At the <a class=\"article-title\" " +
        "                     href=\"http://127.0.0.1:8000/events/" + data_arr[1] + "\">" + data_arr[1] + "</a>\n" +
        "                    <small class=\"text-muted\">" + data_arr[6] + "</small>\n" +
        "                </p>\n" +
        "              </div>\n" +
        "            <img class=\"rounded-circle article-img\" src=" + data_arr[5] + ">"
    document.getElementById("feed").insertBefore(new_shake, document.getElementById("feed").firstChild);
}