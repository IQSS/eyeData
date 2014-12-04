/* Project specific Javascript goes here. Nothing yet */
 // width and height

/* VISUALIZATION FUNCTIONS */

// globals for formatting
// want to create dynamically sized graphs?
var w = 500;
var h = 400;
var padding = 1;
//var svg;

function visualize(data_id, variable) {

  // load the data
  // call to grab the JSON using the id of the desired data
  // currently assuming univariate, need to create condition to handle multiple variables
  // var data_json = fun(data_id, variable);
  $.getJSON("variable-detail/" + data_id + "/" + variable + "/", function(dataset) {
  // var dataset = JSON.parse(data_json);

      console.log(dataset);
      // to scale the data to fit the screen
      var yScale = d3.scale.linear()
                     .domain([0, d3.max(dataset.y)])
                     .range([h - padding, padding]);

      switch (dataset["graph type"]) {

          case "bar":
          visualize_bar(dataset, yScale);
          break;

          case "density":
          visualize_density(dataset, yScale);
          break;

      }

//      label(dataset, yScale);

      // show the modal
      $("#visualization").modal('show');
  });
}

function visualize_bar(dataset, yScale) {

    var svg = d3.select("#viz_space")
                .append("svg")
                .attr("width", w)
                .attr("height", h);

    svg.selectAll("rect")                            // creates rect for every datapoint
       .data(dataset.y)                              // binds data
       .enter()
       .append("rect")
       .attr("x", function(d, i) {                   // elements x location
           return i * (w / dataset.y.length);
       })
       .attr("y", function(d) {                      // location vertically
//                return h - 2.5*d;
           return h - yScale(d);
       })
       .attr("width", w / dataset.y.length - padding)// width
       .attr("height", function(d) {                 // height
//                return 2.5*d;
           return yScale(d);
       })
       .attr("fill", function(d) {                   // color correlates with height
//           return "rgb(0, 0, " + (d / 2.5) + ")";    // add controls for color?
           return "rgb(0, 0, 100)";
       });

    svg.selectAll("text")                            // print y value on bar
       .data(dataset.y)                           
       .enter()
       .append("text")
       .text(function(d) {
           return d;
       });
}

// set up title, axes, etc.
function label(dataset, yScale) {                    // adds axes, titles, scales

    var svg = d3.select("#viz_space");
    svg.append("text")                               // title
       .attr("x", (w / 2))             
       .attr("y", 0 - (margin.top / 2))
       .attr("text-anchor", "middle")  
       .style("font-size", "16px") 
       .text(dataset.graph_title);

    var yAxis = d3.svg.axis()                        // function to create y-axis
                  .scale(yScale)
                  .orient("left")
                  .ticks(10);                        // roughly ten tick marks

    svg.append("g")                                  // set up y-axis
       .attr("class", "axis")
       .attr("transform", "translate(0, " + padding + ")")
       .call(yAxis);

         // x axis

}
