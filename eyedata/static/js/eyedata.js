/* Project specific Javascript goes here. Nothing yet */
 // width and height

// On document load
$(document).ready(function(){
  // allow sorting of results on 
  $("#datasets-table").dataTable({
    "scrollY" : "100px",
    "scrollCollapse": true,
    "paging": false,
    "stateSave": true  
  });

  // change the color of the search field to black
  $(".dataTables_filter > label > input").css("color", "black");
  $(".dataTables_scrollBody").css("height","50%");
  
  // add hover ability to table rows
  $("#datasets-table tr").hover(function(){
    $(this).addClass("hover");
  }, function(){
    $(this).removeClass("hover");
  });

  // attach on click handler to rows in table 
  $("#datasets-table tbody").on("click", "tr", function(event){
    var row = $(this);
    if (row.hasClass("selected") && deselect(row.attr('dataset_id'))) {
      row.removeClass("selected");
    }
    else if (select(row)) {
      row.addClass("selected");
    }
    else {
      console.log("Error transforming variable workspace.");
    }

  });

});


// Adds the variables corresponding to the selected dataset to the
//  workspace
function select(dataset) {
  // get variable names and populate options
  var id = dataset.attr("dataset_id");
  var ret = true;
  $.getJSON("get-vars/" + id + "/", function(data, textStatus, jqXHR){
    console.log(data);
    var html = construct_workspace_html(id, data);
    $("#variables").append(html);
    activate_workspace(id);
  })
  .done(function() {
      console.log("Successful retrieval of data.");
  })
  .fail(function() {
    console.log("Failed retrieval of data.");
    ret = false;
  });

  return ret;
}

// Removes the variables from the selected dataset from the workspace
function deselect(id){
  if(!isNaN(id)){
    return false;
  }

  // remove the div
  $("#variables-" + id).remove();
  return true;
}

// given dataset id and JSON data, constructs html to be added to the variables workspace
function construct_workspace_html(id, data){
  // construct outer div for dataset
  var html = "<div id='variables-" + id + "'>";
  $.each(data, function(key, variables) {
    console.log("Received field " + key);

    // construct children divs per field
    html += "<div id='" + key + "-" + id + "'>";
    $.each(variables, function(index, variable){
      html += "<button dataset-id='" + id + "' variable-name='" + variable + "' class='btn btn-info'>";
      html += "<span class='glyphicon glyphicon-wrench' aria-hidden='true'></span>";
      html += variable; 
      html += "</button>";
    });
    html += "</div>"
  
  });
  html += "</div>"

  return html;
}

// given a dataset id, activates variables belonging to that dataset
function activate_workspace(id){
  $("#variables-" + id).find("div[id$='-" + id + "']").draggable({
    scroll: true,
    containment: "parent", 
    cursor: "move",
    revert: true,  
    opacity: 0.7
  });
}
