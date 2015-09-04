function autoResize() {
      var el;
      try {
 el = window.getComputedStyle(document.getElementById('streamWindow'), null)
     .getPropertyValue('padding-left');
} catch(e) {
 el = document.getElementById('streamWindow').currentStyle.padding-left;
} 
    var x = document.getElementById("streamWindow").clientWidth;
    var y = parseInt(x) - 2*parseInt(el);
    var width = (y-100)/4;
    if(width < 155)
    {
      width = (y-70)/3;
    }
    if(width < 155)
    {
      width = (y-50)/2;
    }
    if(width < 155)
    {
      width = (y-20);
    }
    var stream = document.getElementsByClassName("stream");
    for(i=0 ; i<stream.length ; i++)
    {
      stream[i].style.width=width + "px";
    }
    
    }

function validateLogin() {

  var valid = true;

      //Check username
      var username = document.forms["loginForm"]["username"].value;
      if (username == null || username == "") {
        document.getElementById("logUserHint").innerHTML  = "! You must enter a login";
        valid = false;
      }else{
        document.getElementById("logUserHint").innerHTML  = "";
      }

      //Check username
      var password = document.forms["loginForm"]["password"].value;
      if (password == null || password == "") {
        document.getElementById("logPassHint").innerHTML  = "! You must enter a password";
        valid = false;
      }else{
        document.getElementById("logPassHint").innerHTML  = "";
      }

      if(valid){
        return true;
      }else{
        return false;
      }


    }

    function validateSignin() {
      var valid = true;

      //Check username
      var username = document.forms["signInForm"]["username"].value;
      if (username.length < 3) {
        document.getElementById("usernameHint").innerHTML  = "! Username must be minimum of 3 characters";
        valid = false;
      }else{
        document.getElementById("usernameHint").innerHTML  = "";
      }

      //check email
      var email = document.forms["signInForm"]["email"].value;
      if (email == null || email==""){
        document.getElementById("emailHint").innerHTML  = "! You must enter an email address";
        valid = false;
      }else{
        document.getElementById("emailHint").innerHTML  = "";
      }

      //check password1
      var pass = document.forms["signInForm"]["password1"].value;
      if (pass.length < 3 ) {
        document.getElementById("pass1Hint").innerHTML  = "! Password must be minimum of 3 characters";
        valid = false;
      }else{
        document.getElementById("pass1Hint").innerHTML  = "";
      }

      //check password2
      var pass2 = document.forms["signInForm"]["password2"].value;
      if (pass!=pass2) {
        document.getElementById("pass2Hint").innerHTML  = "! Passwords do not match";
        valid = false;
      }else{
        document.getElementById("pass2Hint").innerHTML  = "";
      }

      //check birthdate
      var birthdate = document.forms["signInForm"]["verifyAge"].value;
      var age = calcAge(birthdate);
      //check age min 18
      if(age<18){
        document.getElementById("ageHint").innerHTML  = "! You must be at least 18";
        valid = false;
      }else{
        document.getElementById("ageHint").innerHTML  = "";
      }

      //check age max 130
      if(age>130){
        document.getElementById("ageHint").innerHTML  = "! You are not "+age+" years old !";
        valid = false;
      }else{
        if(age>17){
          document.getElementById("ageHint").innerHTML  = "";
        }
      }

      //check birthdate entered
      if (birthdate == null || birthdate==""){
        document.getElementById("ageHint").innerHTML  = "! You must enter your date of birth";
        valid = false;
      }else{
        if(age>17 && age<131){
          document.getElementById("ageHint").innerHTML  = "";
        }
        
      }

      //check terms and services
      var check = document.forms["signInForm"]["terms"].checked;
      if(!check)
      {
        document.getElementById("termsHint").innerHTML  = "! You must agree with the term of uses";
        valid = false
      }else{
        document.getElementById("termsHint").innerHTML  = "";
      }
      

      

      if(valid){
        return true;
      }else{
        return false;
      }

    }

    function calcAge(dateString) {
      var birthday = +new Date(dateString);
      return~~ ((Date.now() - birthday) / (31557600000));
    }