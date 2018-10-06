var prog = 0;

$(document).ready(function() {
  $("#progressbar").css("width", 0 + "%");
  $(".left").hide();
});

function progress(dir)
{
  if(dir == 'left' && prog > 0)
  {
    prog--;
    if (prog == 0){
      $(".left").hide();
    }
    else {
      $(".left").show();
    }
    if (prog == 4){
      $(".right").hide();
    }
    else {
      $(".right").show();
    }
  }
  if(dir == 'right' && prog < 4)
  {
    prog++;
    if (prog == 0){
      $(".left").hide();
    }
    else {
      $(".left").show();
    }
    if (prog == 4){
      $(".right").hide();
    }
    else {
      $(".right").show();
    }
  }
  console.log(prog);
  $("#progressbar").css("width", prog*25 + "%");




}
