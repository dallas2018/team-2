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
    if(prog == 1)
    {
      sendtest();
    }
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

function sendtest()
{
  console.log("Running");
  var senderName = document.getElementById("name").value;
  var senderEmail = document.getElementById("email").value;
  var url = "http://129.114.104.6:5000/submit"
  var data = {
    "user_id" : "new_user",
    "data" : {
      "user_first_name" : senderName,
      "user_last_name" : "Khan"
    }
  }
  $.ajax({
  type: "POST",
  url: url,
  data: JSON.stringify(data),
  success: function(data){
    console.log(data);
  },
  contentType: "application/json"
});

}
