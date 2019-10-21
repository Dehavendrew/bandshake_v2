function test(nodes){
    var tags = JSON.parse(document.getElementById('tags-data').textContent)
        console.log(tags)

}

function setNodes(){
    var tags = JSON.parse(document.getElementById('tags-data').textContent)
//     names = []
//     for(i = 0; i < tags.length; ++i){
//         if(!names.includes(tags[i].personA)){
//             names.push(tags[i].personA)
//             var temp = {
//                 "id":tags[i].personA
//             }
//             nodes.push(temp)
//         }
//         if(!names.includes(tags[i].personB)){
//             names.push(tags[i].personB)
//             var temp = {
//                 "id":tags[i].personB
//             }
//             nodes.push(temp)
//         }
//         var connection = {
//             "source": tags[i].personA,
//             "target": tags[i].personB,
//             "value":1
//         }
//         links.push(connection)
//     }
    names = []
    people["name"] = tags[0].personA
    people["hero"] = tags[0].personA
    people["img"] = tags[0].personALink
    names.push(tags[0].personA)
    for(i = 0; i < tags.length; ++i){
         if(!names.includes(tags[i].personA)){
            names.push(tags[i].personA)
            var temp = {
                "hero":tags[i].personA,
                "name":tags[i].personA,
                "link":"",
                "img":tags[i].personALink,
                "size": 40000
            }
            people["children"].push(temp)
        }
        if(!names.includes(tags[i].personB)){
            names.push(tags[i].personB)
            var temp = {
                "hero":tags[i].personB,
                "name":tags[i].personB,
                "link":"",
                "img":tags[i].personBLink,
                "size": 40000
            }
            people["children"].push(temp)
        }
    }
 }
//
// var nodes = []
//
// var links = []

var people = {
    "name":"",
    "img":"",
    "hero":"",
    "children":[]
}
//
// function createGraph(){
//
//     var svg = d3.select("svg"),
//         width = +svg.attr("width"),
//         height = +svg.attr("height");
//
//     var simulation = d3.forceSimulation()
//         .force("link", d3.forceLink().id(function(d) { return d.id; }))
//             .force('charge', d3.forceManyBody()
//           .strength(-200)
//           .theta(100)
//           .distanceMax(1)
//         )
//         .force("center", d3.forceCenter(width / 2, height / 2));
//
//
//     const graph = {
//       "nodes": nodes,
//       "links": links,
//     }
//
//
//     function run(graph) {
//
//       graph.links.forEach(function(d){
//       });
//
//       var link = svg.append("g")
//                     .style("stroke", "#aaa")
//                     .selectAll("line")
//                     .data(graph.links)
//                     .enter().append("line");
//
//       var node = svg.append("g")
//                 .attr("class", "nodes")
//       .selectAll("circle")
//                 .data(graph.nodes)
//       .enter().append("circle")
//               .attr("r", 2)
//               .call(d3.drag()
//                   .on("start", dragstarted)
//                   .on("drag", dragged)
//                   .on("end", dragended));
//
//       var label = svg.append("g")
//           .attr("class", "labels")
//           .selectAll("text")
//           .data(graph.nodes)
//           .enter().append("text")
//             .attr("class", "label")
//             .text(function(d) { return d.id; });
//
//       simulation
//           .nodes(graph.nodes)
//           .on("tick", ticked);
//
//       simulation.force("link")
//           .links(graph.links);
//
//       function ticked() {
//         link
//             .attr("x1", function(d) { return d.source.x; })
//             .attr("y1", function(d) { return d.source.y; })
//             .attr("x2", function(d) { return d.target.x; })
//             .attr("y2", function(d) { return d.target.y; });
//
//         node
//              .attr("r", 32)
//              .style("fill", "#efefef")
//              .style("stroke", "#424242")
//              .style("stroke-width", "1px")
//              .attr("cx", function (d) { return d.x+5; })
//              .attr("cy", function(d) { return d.y-3; });
//
//
//         label
//                 .attr("x", function(d) { return d.x - 50; })
//                 .attr("y", function (d) { return d.y + 50; })
//                 .style("font-size", "20px").style("fill", "#333");
//       }
//     }
//
//     function dragstarted(d) {
//       if (!d3.event.active) simulation.alphaTarget(0.3).restart()
//       d.fx = d.x
//       d.fy = d.y
//     //  simulation.fix(d);
//     }
//
//     function dragged(d) {
//       d.fx = d3.event.x
//       d.fy = d3.event.y
//     //  simulation.fix(d, d3.event.x, d3.event.y);
//     }
//
//     function dragended(d) {
//       d.fx = d3.event.x
//       d.fy = d3.event.y
//       if (!d3.event.active) simulation.alphaTarget(0);
//       //simulation.unfix(d);
//     }
//
//     run(graph)
//     }

function plot(){
         var tcBlack = "#130C0E";

    // rest of vars
    var w = 960,
        h = 800,
        maxNodeSize = 200,
        x_browser = 20,
        y_browser = 25,
        root;

    var vis;
    var force = d3.layout.force();

    vis = d3.select("#vis").append("svg").attr("width", w).attr("height", h);

    d3.json("", function(json) {

      root = people;
      root.fixed = true;
      root.x = w / 2;
      root.y = h / 4;


            // Build the path
      var defs = vis.insert("svg:defs")
          .data(["end"]);


      defs.enter().append("svg:path")
          .attr("d", "M0,-5L10,0L0,5");

         update();
    });


    /**
     *
     */


    function update() {
      var nodes = flatten(root),
          links = d3.layout.tree().links(nodes);

      // Restart the force layout.
      force.nodes(nodes)
            .links(links)
            .gravity(0)
        .charge(-1500)
        .linkDistance(200)
        .friction(0.5)
        .linkStrength(function(l, i) {return 1; })
        .size([w, h])
        .on("tick", tick)
            .start();

       var path = vis.selectAll("path.link")
          .data(links, function(d) { return d.target.id; });

        path.enter().insert("svg:path")
          .attr("class", "link")
          // .attr("marker-end", "url(#end)")
          .style("stroke", "#eee");


      // Exit any old paths.
      path.exit().remove();



      // Update the nodes…
      var node = vis.selectAll("g.node")
          .data(nodes, function(d) { return d.id; });


      // Enter any new nodes.
      var nodeEnter = node.enter().append("svg:g")
          .attr("class", "node")
          .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
          .on("click", click)
          .call(force.drag);

      // Append a circle
      nodeEnter.append("svg:circle")
          .attr("r", function(d) { return Math.sqrt(d.size) / 5 || 4.5; })
          .style("fill", "#eee");


      // Append images
      var images = nodeEnter.append("svg:image")
            .attr("xlink:href",  function(d) { return d.img;})
            .attr("x", function(d) { return -25;})
            .attr("y", function(d) { return -25;})
            .attr("height", 50)
            .attr("width", 50);

      // make the image grow a little on mouse over and add the text details on click
      var setEvents = images

              .on( 'click', function (d) {
                  window.location.href = "http://127.0.0.1:8000/user/" +  d.hero
               })

              // .on( 'mouseenter', function() {
              //   // select element in current context
              //   d3.select( this )
              //     .transition()
              //     .attr("x", function(d) { return -60;})
              //     .attr("y", function(d) { return -60;})
              //     .attr("height", 100)
              //     .attr("width", 100);
              // })
              // // set back
              // .on( 'mouseleave', function() {
              //   d3.select( this )
              //     .transition()
              //     .attr("x", function(d) { return -25;})
              //     .attr("y", function(d) { return -25;})
              //     .attr("height", 50)
              //     .attr("width", 50);
              // });

      // Append hero name on roll over next to the node as well
      nodeEnter.append("text")
          .attr("class", "nodetext")
          .attr("x", x_browser)
          .attr("y", y_browser +15)
          .attr("fill", tcBlack)
          .text(function(d) { return d.hero; });


      // Exit any old nodes.
      node.exit().remove();


      // Re-select for update.
      path = vis.selectAll("path.link");
      node = vis.selectAll("g.node");

    function tick() {


        path.attr("d", function(d) {

         var dx = d.target.x - d.source.x,
               dy = d.target.y - d.source.y,
               dr = Math.sqrt(dx * dx + dy * dy);
               return   "M" + d.source.x + ","
                + d.source.y
                + "A" + dr + ","
                + dr + " 0 0,1 "
                + d.target.x + ","
                + d.target.y;
      });
        node.attr("transform", nodeTransform);
      }
    }


    /**
     * Gives the coordinates of the border for keeping the nodes inside a frame
     * http://bl.ocks.org/mbostock/1129492
     */
    function nodeTransform(d) {
      d.x =  Math.max(maxNodeSize, Math.min(w - (d.imgwidth/2 || 16), d.x));
        d.y =  Math.max(maxNodeSize, Math.min(h - (d.imgheight/2 || 16), d.y));
        return "translate(" + d.x + "," + d.y + ")";
       }

    /**
     * Toggle children on click.
     */
    function click(d) {
      if (d.children) {
      //  d._children = d.children;
      //  d.children = null;
      } else {
        d.children = d._children;
        d._children = null;
      }

      update();
    }


    /**
     * Returns a list of all nodes under the root.
     */
    function flatten(root) {
      var nodes = [];
      var i = 0;

      function recurse(node) {
        if (node.children)
          node.children.forEach(recurse);
        if (!node.id)
          node.id = ++i;
        nodes.push(node);
      }

      recurse(root);
      return nodes;
    }
}