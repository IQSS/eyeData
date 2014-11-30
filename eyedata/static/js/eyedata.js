/* Project specific Javascript goes here. Nothing yet */
 // width and height
 
// On document load
$(document).ready(function(){
  $("#flip").click(function(){
    $("#panel").slideToggle("slow");
  });
});

// Create SVG element
function visualize() { var svg = d3.select(".cover-container")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

  svg.selectAll("rect")
      .data(dataset)
      .enter()
      .append("rect")
      .attr("x", function(d, i) {
          return i * (w / dataset.length);
      })
      .attr("y", function(d) {
          return h - 2.5*d;
      })
      .attr("width", w / dataset.length - padding)
      .attr("height", function(d) {
          return 2.5*d;
      })
      .attr("fill", function(d) {
          return "rgb(0, 0, " + (d / 2.5) + ")";
      });

 svg.selectAll("text")
      .data(dataset)
      .enter()
      .append("text")
      .text(function(d) {
          return d;
      })
      .attr("x", function(d, i) {
          return i * (w / dataset.length) + (w / dataset.length - padding) / 2;
      })
      .attr("y", function(d) {
          return h - (2.5* d) + 14;
      })
      .attr("font-family", "sans-serif")
      .attr("font-size", "11px")
      .attr("fill", "white")
      .attr("text-anchor", "middle");
}
