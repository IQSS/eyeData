/* Project specific Javascript goes here. Nothing yet */
 // width and height
 
// On document load
$(document).ready(function(){
  // allow sorting of results on 
  $("#datasets-table").tablesorter({
    sortList: [[0,0], [1,0]]
  });

  // make table scrollable
  console.log("loaded");
});

