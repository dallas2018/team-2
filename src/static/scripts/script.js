var prog = 0;
localStorage.clear();

$(document).ready(function() {
  $("#progressbar").css("width", 0 + "%");
  $(".left").hide();
});

function progress(dir)
{
  if(dir == 'left' && prog > 0)
  {
    prog--;
    if (prog <= 0){
      $(".left").hide();
    }
    else {
      $(".left").show();
    }
    if (prog == 5){
      $(".right").hide();
    }
    else {
      $(".right").show();
    }
  }
  if(dir == 'right' && prog < 8)
  {
    sendtest(prog);
    prog++;
    if (prog == 0){
      $(".left").hide();
    }
    else {
      $(".left").show();
    }
    if (prog == 7){
      $(".right").hide();
    }
    else {
      $(".right").show();
    }

  }
  console.log(prog);
  $("#progressbar").css("width", prog*15 + "%");
}

function sendtest(prog)
{
  var url = "http://localhost:5000/submit"
  if(prog == 0)
  {
    var firstParam = document.getElementById("first").value;
    var secondParam = document.getElementById("second").value;
    var thirdParam = document.getElementById("third").value;
    if(firstParam == "" || secondParam == "" || thirdParam == "")
    {
      window.alert("You have not filled in the last form completely, go back and please fill it out!")
      return false;
    }
    var dataNew = {
      "user_id" : "new_user",
      "data" : {
        "user_first_name" : firstParam,
        "user_last_name" : thirdParam
        // "user_middle_name" : thirdParam
      }
    }
  }
  else if(prog == 2) //change this to be take user id from here
  {
    var firstParam = document.getElementById("fourth").value;
    var secondParam = document.getElementById("fifth").value;
    var thirdParam = document.getElementById("sixth").value;
    var id = localStorage.getItem("user_id");
    if(firstParam == "" || secondParam == "" || thirdParam == "")
    {
      window.alert("You have not filled in the last form completely, go back and please fill it out!")
      return false;
    }
    var dataNew = {
      "user_id" : id,  //actual id
      "data" : {
        "user_location": firstParam + " " + secondParam + " " + thirdParam
      }
    }
  }
  else if(prog == 3)
  {
    var secondParam = document.getElementById("eigth").value;
    var thirdParam = document.getElementById("ninth").value;
    var fourthParam = document.getElementById("tenth").value;
    var id = localStorage.getItem("user_id");

    if(secondParam == "" || thirdParam == "")
    {
      window.alert("You have not filled in the last form completely, go back and please fill it out!");
      return false;
    }
    var dataNew = {
      "user_id" : id,  //actual id
      "data" : {
        "user_dob" : secondParam,
        "user_email" : thirdParam,
        "user_phone" : fourthParam
      }
    }
  }


  console.log(dataNew);

  console.log("Beginning ajax call")

  $.ajax({
  type: "POST",
  url: url,
  data: JSON.stringify(dataNew),
  contentType: "application/json",
  success: function(data){
    var returnedId = data['result']['user_id']
    localStorage.setItem("user_id" , returnedId);
    console.log("storing returned id: " + returnedId);
  }
});

}
