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
    if (row.hasClass("selected")){
      if (deselect(row.attr('dataset-id'))){
        row.removeClass("selected");
        row.find("td").first().find("span").remove();
      }
      else{
        console.log("Deselect operation failed!");
      }
    }
    else if (select(row)) {
      row.addClass("selected");
      // TODO -- add check mark to selected datasets
      row.find("td").first().append("<span class='glyphicon glyphicon-play></span> ");
    }
    else {
      console.log("Error transforming variable workspace.");
    }

  });

  // attach click handler to buttons
  $("#variables").on("click", "button", function(event){
    var variable = $(this).attr('variable-name')
      , id = $(this).parent().attr('dataset-id');

    // calling Alex's function, so we need to make sure it's loaded
     visualize(id, variable);
     console.log("Called Alex's visualize with" + id + " and " + variable);
  });

});


// Adds the variables corresponding to the selected dataset to the
//  workspace
function select(dataset) {
  // get variable names and populate options
  var id = dataset.attr("dataset-id");
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
  if(isNaN(id)){
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
    html += "<div id='" + key + "-" + id + "' dataset-id='" + id + "'";
    html += "' class='btn-group btn-group-justified variable-btn-set'";
    html += "role='group' aria-label='...' >";
    $.each(variables, function(index, variable){
      var btn = "<button " + "variable-name='" + variable;
      btn += "' class='btn btn-info btn-variable'>";
      btn += "<span class='glyphicon glyphicon-wrench' aria-hidden='true'></span> ";
      btn += variable; 
      btn += "</button>";
      html += btn;
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
    cursor: "move",  
    opacity: 0.8
  });
}
