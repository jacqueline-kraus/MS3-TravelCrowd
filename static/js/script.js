$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('input.autocomplete').autocomplete({
      data: {
        "USA": null,
        "Germany": null,
        "Italy": null,
        "Greece": null,
        "Spain": null,
        "England": null,
        "Russia": null,
        "Austria": null,
      },
    });
    $('.datepicker').datepicker();
  });