window.onload = function test(){
  drawGraph()
}

data1 = []
data2 = []

function makePrediction(){
  editedData = ""
  for(var i = 0; i < 50; ++i){
    editedData += (parseInt(data1[i]["y"]) - parseInt(data2[i]["y"])).toString()
    if(i != 49){
      editedData += ","
    }
  }
  console.log(editedData)
  $.ajax({
      url: "\\getPrediction\\",
      type: "POST",
      data: {
        shakes : editedData
      },
      success: function(json) {
          console.log(json)
          if(json == "Handshake")
            document.getElementById("Shake").innerHTML = "HandShake Detected"
          else
            document.getElementById("Shake").innerHTML = "No HandShake Detected"
      }

  })
}

function con(bandnum) {
    band_service = '19B10000-E8F2-537E-4F6C-D104768A1214'
    band_char = '19B10001-E8F2-537E-4F6C-D104768A1214'

    navigator.bluetooth.requestDevice({
        //filters: [{name: "BandShake_0001"}],
        filters: [{ services: [band_service.toLowerCase()] }]
    })
        .then(device => device.gatt.connect())
        .then(server => server.getPrimaryService(band_service.toLowerCase()))
        .then(service =>service.getCharacteristic(band_char.toLowerCase()))
        .then(characteristic => characteristic.startNotifications())
        .then(characteristic => {
              if(bandnum == 1){
                characteristic.addEventListener('characteristicvaluechanged',
                    handleCharacteristicValueChanged1);
              document.getElementById("band1btn").innerHTML = "Connected"
              document.getElementById("band1btn").className = "btn btn-success ml-3"
              }
              if(bandnum == 2){
                characteristic.addEventListener('characteristicvaluechanged',
                    handleCharacteristicValueChanged2);
                document.getElementById("band2btn").innerHTML = "Connected"
                document.getElementById("band2btn").className = "btn btn-success ml-3"
              }

                console.log(bandnum + " connected");
        })
        .catch(error => {
            console.log(error.message);
        });
}

function handleCharacteristicValueChanged1(event) {
  addToArray(event.target.value.getUint8(0), 1)
}

function handleCharacteristicValueChanged2(event) {
  addToArray(event.target.value.getUint8(0), 2)
}

function clr(){
  console.log("clearing")
  document.getElementById("Shake").innerHTML = "Awaiting Data"
  data1 = []
  data2 = []
  d3.selectAll("path.line").remove();
  d3.selectAll("path.line2").remove();
  d3.selectAll("circle.dot").remove();
  d3.selectAll("circle.dot2").remove();
  plotData()
}

function addToArray(text, band){
    if(data2.length >= 50 && data1.length >= 50)
      return

    if(band == 1){
      var new_row = {"y": text}
      data1.push(new_row)
      plotData()
    }
    if(band == 2){
      var new_row = {"y": text}
      data2.push(new_row)
      plotData()
    }
    if(data2.length == 50 && data1.length == 50){
      makePrediction()
    }
  }

var svg
var line
var line2
var xScale
var yScale

function drawGraph(){
  var margin = {top: 50, right: 50, bottom: 50, left: 50}
  , width = document.getElementById("graph").offsetWidth - margin.left - margin.right
  , height = document.getElementById("graph").offsetHeight - margin.top - margin.bottom;

  var n = 50;

  xScale = d3.scaleLinear()
    .domain([0, n-1]) // input
    .range([0, width]); // output

  yScale = d3.scaleLinear()
    .domain([0, 300]) // input
    .range([height, 0]); // output

  line = d3.line()
    .x(function(d, i) { return xScale(i); }) // set the x values for the line generator
    .y(function(d) { return yScale(d.y); }) // set the y values for the line generator
    .curve(d3.curveMonotoneX) // apply smoothing to the line

  line2 = d3.line()
    .x(function(d, i) { return xScale(i); }) // set the x values for the line generator
    .y(function(d) { return yScale(d.y); }) // set the y values for the line generator
    .curve(d3.curveMonotoneX) // apply smoothing to the line


  svg = d3.select("#graph").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// 3. Call the x axis in a group tag
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

// 4. Call the y axis in a group tag
svg.append("g")
    .attr("class", "y axis")
    .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

// 9. Append the path, bind the data, and call the line generator
}

function plotData(){
  svg.append("path")
      .datum(data1) // 10. Binds data to the line
      .attr("class", "line") // Assign a class for styling
      .attr("d", line); // 11. Calls the line generator

  svg.append("path")
      .datum(data2) // 10. Binds data to the line
      .attr("class", "line2") // Assign a class for styling
      .attr("d", line2); // 11. Calls the line generator

  // 12. Appends a circle for each datapoint
  svg.selectAll(".dot")
      .data(data1)
    .enter().append("circle") // Uses the enter().append() method
      .attr("class", "dot") // Assign a class for styling
      .attr("cx", function(d, i) { return xScale(i) })
      .attr("cy", function(d) { return yScale(d.y) })
      .attr("r", 5)
        .on("mouseover", function(a, b, c) {
    			console.log(a)
  		})

    svg.selectAll(".dot2")
        .data(data2)
        .enter().append("circle") // Uses the enter().append() method
        .attr("class", "dot2") // Assign a class for styling
        .attr("cx", function(d, i) { return xScale(i) })
        .attr("cy", function(d) { return yScale(d.y) })
        .attr("r", 5)
          .on("mouseover", function(a, b, c) {
        		console.log(a)
      		})
}
