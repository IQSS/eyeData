/* Project specific Javascript goes here. Nothing yet */
 // width and height

/* VISUALIZATION FUNCTIONS */

// globals for formatting
// want to create dynamically sized graphs?
var w = 500;
var h = 800;
var padding = 1;

function visualize(data_id, variable) {

  // load the data
  // call to grab the JSON using the id of the desired data
  // currently assuming univariate, need to create condition to handle multiple variables
  // var data_json = fun(data_id, variable);
  $.getJSON("/variable-detail/" + data_id + "/" + variable + "/", function(dataset) {
  // var dataset = JSON.parse(data_json);

    // to scale the data to fit the screen
    var yScale = d3.scale.linear()
             .domain([0, d3.max(dataset.data)])
             .range([h - padding, padding]);

    switch (dataset.type) {
        case "bar":
      visualize_bar(dataset, yScale);
      break;

        case "density":
      visualize_density(dataset, yScale);
      break;

//            case "table":
//                visualize_table(dataset);
//                break;

//          case "scatter":
//              visualize_scatter(dataset);
//              label(dataset);
//              break;
  }

    label(dataset, yScale);
  });
}

// where does this put the graph?
// can I make the graph a d3 object and return it?
function visualize_bar(dataset, yScale) {

  var svg = d3.select(".cover-container")
    .append("svg")
    .attr("width", w)
    .attr("height", h);

  svg.selectAll("rect")                             // creates rectangles for every datapoint
    .data(dataset.data)                           // binds data
    .enter()
    .append("rect")
    .attr("x", function(d, i) {                   // where the element is located horizontally
      return i * (w / dataset.length);
    })
    .attr("y", function(d) {                      // location vertically
//                return h - 2.5*d;
      return h - yScale(d);
    })
    .attr("width", w / dataset.length - padding)  // width
    .attr("height", function(d) {                 // height
//                return 2.5*d;
      return yScale(d);
    })
    .attr("fill", function(d) {                   // color, currently correlates with height
      return "rgb(0, 0, " + (d / 2.5) + ")";    // add controls for color?
    });

  svg.selectAll("text")                             // add y values on the corresponding bars
    .data(dataset.data)                           
    .enter()
    .append("text")
    .text(function(d) {
      return d;
  });
}

// set up title, axes, etc.
function label(dataset, yScale) {                     // adds axes, titles, scales

  svg.append("text")                                // title
    .attr("x", (w / 2))             
    .attr("y", 0 - (margin.top / 2))
    .attr("text-anchor", "middle")  
    .style("font-size", "16px") 
    .text(dataset.title);

 var yAxis = d3.svg.axis()                          // function to create y-axis
  .scale(yScale)
  .orient("left")
  .ticks(10);                      // roughly ten tick marks

svg.append("g")
  .attr("class", "axis")
  .attr("transform", "translate(0, " + padding + ")")
  .call(yAxis);

         // x axis

}
