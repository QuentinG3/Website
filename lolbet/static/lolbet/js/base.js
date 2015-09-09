
function autoResizeFrame(id){
    var newheight;
    var newwidth;

    if(document.getElementById){
        newheight=document.getElementById(id).contentWindow.document .body.scrollHeight;
        newwidth=document.getElementById(id).contentWindow.document .body.scrollWidth;
    }

    document.getElementById(id).height= "0px";
    document.getElementById(id).width= (newwidth) + "px";
}


function updateLookup(JSON,lookup)
{
  //Premier header
              var header = document.createElement("h2");
              //TODO => name
              var headerText = document.createTextNode(JSON.summonerName);
              header.appendChild(headerText);
              lookup.appendChild(header);

              //Second header
              var header2 = document.createElement("h5");
              //TODO => Region
              var headerText2 = document.createTextNode("Ranked Solo | Summoner's Rift |"+JSON.region);
              header2.appendChild(headerText2);
              lookup.appendChild(header2);

              //hr
              var hr1 = document.createElement("hr");
              lookup.appendChild(hr1);

              //div table
              var tableR = document.createElement("div");
              tableR.className = "table-responsive table-bg";
              lookup.appendChild(tableR);

              //table
              var table = document.createElement("table");
              table.className = "table";
              tableR.appendChild(table);

              //table body
              var tbody = document.createElement("tbody");
              table.appendChild(tbody);

              var tr1 = document.createElement("tr");
              tbody.appendChild(tr1);

              //Boucle for pour les joueurs de la team 1
              for(var i = 0 ; i < JSON.team1.length ; i++){
                var player = JSON.team1[i];
                var td1 = document.createElement("td");
                tr1.appendChild(td1);

                var center1 = document.createElement("center");
                td1.appendChild(center1);

                //Player Name
                var h50 = document.createElement("h5");
                h50.className = "summoner-name-blue";
                var h50text = document.createTextNode(player.name);
                h50.appendChild(h50text);
                center1.appendChild(h50);

                var imageDiv = document.createElement("div");
                imageDiv.className = "image image-blue";
                td1.appendChild(imageDiv);

                //Champion name img x2
                var img = document.createElement("img");
                img.setAttribute("width", "145");
                img.setAttribute("src", "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"+player.champion+"_0.jpg");
                img.setAttribute("alt", player.champion);
                imageDiv.appendChild(img);

                //KDA
                var h51 = document.createElement("h5");
                h51.className = "kda";
                var h51text = document.createTextNode("-");
                h51.appendChild(h51text);
                imageDiv.appendChild(h51);

                //WL
                var h52 = document.createElement("h5");
                h52.className = "wl";
                var h52text = document.createTextNode("W:"+player.wins+" - L:"+player.losses);
                h52.appendChild(h52text);
                imageDiv.appendChild(h52);

                //bg
                var h53 = document.createElement("h5");
                h53.className = "bg";
                imageDiv.appendChild(h53);

                //Division image diamond*2 (tier)*2 (division) (leaguepoints)
                var tooltipDiv = document.createElement("a");
                tooltipDiv.className = "tooltip3";
                tooltipDiv.setAttribute("href","#");
                imageDiv.appendChild(tooltipDiv);

                var imgLeague = document.createElement("img");
                imgLeague.className = "league";
                imgLeague.setAttribute("src","https://boost-rankedboost.netdna-ssl.com/file/2014/09/"+player.tier+"-rewards-lol.png");
                tooltipDiv.appendChild(imgLeague);

                var spanTooltipDiv = document.createElement("span");
                tooltipDiv.appendChild(spanTooltipDiv);
                
                var spanCenter = document.createElement("center");
                spanTooltipDiv.appendChild(spanCenter);

                var spanBold = document.createElement("b");
                var spanBoldText = document.createTextNode(player.tier+" "+player.division+" - "+player.leaguePoints+" LP");
                spanBold.appendChild(spanBoldText);
                spanCenter.appendChild(spanBold);

                //League division
                var h6 = document.createElement("h6");
                h6.className = "leaguen";
                var h6Text = document.createTextNode(player.division);
                h6.appendChild(h6Text);
                imageDiv.appendChild(h6);

                //runes et masteries
                var tooltipRunes = document.createElement("a");
                tooltipRunes.className = "tooltip2";
                tooltipRunes.setAttribute("href","");
                imageDiv.appendChild(tooltipRunes);

                var imgRunes = document.createElement("img");
                imgRunes.className = "runes";
                imgRunes.setAttribute("src","http://vignette2.wikia.nocookie.net/leagueoflegends/images/9/90/7_Rune_pages.png/revision/latest/scale-to-width-down/99?cb=20150423134410&format=webp");
                tooltipRunes.appendChild(imgRunes);

                var spanTooltipRunes = document.createElement("span");
                tooltipRunes.appendChild(spanTooltipRunes);

                var spanBoldRunes = document.createElement("b");
                var runesHeader = document.createTextNode("Runes:");
                spanBoldRunes.appendChild(runesHeader);
                spanTooltipRunes.appendChild(spanBoldRunes);

                var br1 = document.createElement("br");
                spanTooltipRunes.appendChild(br1);

                var br2 = document.createElement("br");
                spanTooltipRunes.appendChild(br2);

                var spanBoldMast = document.createElement("b");
                var mastHeader = document.createTextNode("Masteries:");
                spanBoldMast.appendChild(mastHeader);
                spanTooltipRunes.appendChild(spanBoldMast);

                //summoners 1 et 2
                var summ1 = document.createElement("img");
                summ1.className = "summoner1";
                summ1.setAttribute("src","http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/Summoner"+ player.spell1 +".png");
                imageDiv.appendChild(summ1);
                var summ2 = document.createElement("img");
                summ2.className = "summoner2";
                summ2.setAttribute("src","http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/Summoner"+ player.spell2+".png");
                imageDiv.appendChild(summ2);
              }
              //Espace entre les deux teams
              var trm = document.createElement("tr");
              tbody.appendChild(trm);

              var tdm = document.createElement("td");
              tdm.style.height="80px";
              trm.appendChild(tdm);

              var tr2 = document.createElement("tr");
              tbody.appendChild(tr2);

              //Boucle for pour les joueurs de la team 2
              for(var i = 0 ; i < JSON.team2.length ; i++){
                var player = JSON.team2[i];
                var td1 = document.createElement("td");
                tr2.appendChild(td1);

                var center1 = document.createElement("center");
                td1.appendChild(center1);

                //Player Name
                var h50 = document.createElement("h5");
                h50.className = "summoner-name-red";
                var h50text = document.createTextNode(player.name);
                h50.appendChild(h50text);
                center1.appendChild(h50);

                var imageDiv = document.createElement("div");
                imageDiv.className = "image image-red";
                td1.appendChild(imageDiv);

                //Champion name img x2
                var img = document.createElement("img");
                img.setAttribute("width", "145");
                img.setAttribute("src", "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"+player.champion+"_0.jpg");
                img.setAttribute("alt", player.champion);
                imageDiv.appendChild(img);

                //KDA
                var h51 = document.createElement("h5");
                h51.className = "kda";
                var h51text = document.createTextNode("-");
                h51.appendChild(h51text);
                imageDiv.appendChild(h51);

                //WL
                var h52 = document.createElement("h5");
                h52.className = "wl";
                var h52text = document.createTextNode("W:"+player.wins+" - L:"+player.losses);
                h52.appendChild(h52text);
                imageDiv.appendChild(h52);

                //bg
                var h53 = document.createElement("h5");
                h53.className = "bg";
                imageDiv.appendChild(h53);

                //Division image diamond*2 (tier)*2 (division) (leaguepoints)
                var tooltipDiv = document.createElement("a");
                tooltipDiv.className = "tooltip3";
                tooltipDiv.setAttribute("href","#");
                imageDiv.appendChild(tooltipDiv);

                var imgLeague = document.createElement("img");
                imgLeague.className = "league";
                imgLeague.setAttribute("src","https://boost-rankedboost.netdna-ssl.com/file/2014/09/"+player.tier+"-rewards-lol.png");
                tooltipDiv.appendChild(imgLeague);

                var spanTooltipDiv = document.createElement("span");
                tooltipDiv.appendChild(spanTooltipDiv);
                
                var spanCenter = document.createElement("center");
                spanTooltipDiv.appendChild(spanCenter);

                var spanBold = document.createElement("b");
                var spanBoldText = document.createTextNode(player.tier+" "+player.division+" - "+player.leaguePoints+" LP");
                spanBold.appendChild(spanBoldText);
                spanCenter.appendChild(spanBold);

                //League division
                var h6 = document.createElement("h6");
                h6.className = "leaguen";
                var h6Text = document.createTextNode(player.division);
                h6.appendChild(h6Text);
                imageDiv.appendChild(h6);

                //runes et masteries
                var tooltipRunes = document.createElement("a");
                tooltipRunes.className = "tooltip2";
                tooltipRunes.setAttribute("href","");
                imageDiv.appendChild(tooltipRunes);

                var imgRunes = document.createElement("img");
                imgRunes.className = "runes";
                imgRunes.setAttribute("src","http://vignette2.wikia.nocookie.net/leagueoflegends/images/9/90/7_Rune_pages.png/revision/latest/scale-to-width-down/99?cb=20150423134410&format=webp");
                tooltipRunes.appendChild(imgRunes);

                var spanTooltipRunes = document.createElement("span");
                tooltipRunes.appendChild(spanTooltipRunes);

                var spanBoldRunes = document.createElement("b");
                var runesHeader = document.createTextNode("Runes:");
                spanBoldRunes.appendChild(runesHeader);
                spanTooltipRunes.appendChild(spanBoldRunes);

                var br1 = document.createElement("br");
                spanTooltipRunes.appendChild(br1);

                var br2 = document.createElement("br");
                spanTooltipRunes.appendChild(br2);

                var spanBoldMast = document.createElement("b");
                var mastHeader = document.createTextNode("Masteries:");
                spanBoldMast.appendChild(mastHeader);
                spanTooltipRunes.appendChild(spanBoldMast);

                //summoners 1 et 2
                var summ1 = document.createElement("img");
                summ1.className = "summoner1";
                summ1.setAttribute("src","http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/Summoner"+ player.spell1 +".png");
                imageDiv.appendChild(summ1);
                var summ2 = document.createElement("img");
                summ2.className = "summoner2";
                summ2.setAttribute("src","http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/Summoner"+ player.spell2+".png");
                imageDiv.appendChild(summ2);
              }

              //HR
              var hr2 = document.createElement("hr");
              lookup.appendChild(hr2);

              //Header banned champions
              var headerBanned = document.createElement("h2");
              var headerSpan = document.createElement("span");
              var headerSpanText = document.createTextNode("Banned");
              headerSpan.appendChild(headerSpanText);
              headerBanned.appendChild(headerSpan);
              var headerBannedText = document.createTextNode(" Champions");
              headerBanned.appendChild(headerBannedText);
              lookup.appendChild(headerBanned);

              //create div table-responsive
              tableRB = document.createElement("div");
              tableRB.className = "table-responsive";
              lookup.appendChild(tableRB);

              //create table table
              tableB = document.createElement("table");
              tableB.className = "table";
              tableRB.appendChild(tableB);

              //create tbody
              tbodyB = document.createElement("tbody");
              tableB.appendChild(tbodyB);

              //create tr
              trB = document.createElement("tr");
              tbodyB.appendChild(trB);

              //boucle for * nombre de ban blue (3 normalement)
              for(var i = 0 ; i < JSON.banned1.length ; i++){
                var banned = JSON.banned1[i];
                //create td
                tdB = document.createElement("td");
                trB.appendChild(tdB);

                //create center
                centerB = document.createElement("center");
                tdB.appendChild(centerB);

                //create div image image-blue
                bannedDiv = document.createElement("div")
                bannedDiv.className = "image image-blue";
                centerB.appendChild(bannedDiv);

                //create img ChampionBannedBlueName
                bannedImg = document.createElement("img");
                bannedImg.setAttribute("width","145");
                bannedImg.setAttribute("src","http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"+banned+"_0.jpg");
                bannedImg.setAttribute("alt","championName");
                bannedDiv.appendChild(bannedImg);
              }
              //boucle for * nombre de ban red (3 normalement)
              for(var i = 0 ; i < JSON.banned2.length ;i++){
                var banned = JSON.banned2[i];
                //create td
                tdB = document.createElement("td");
                trB.appendChild(tdB);

                //create center
                centerB = document.createElement("center");
                tdB.appendChild(centerB);

                //create div image image-blue
                bannedDiv = document.createElement("div")
                bannedDiv.className = "image image-red";
                centerB.appendChild(bannedDiv);

                //create img ChampionBannedBlueName
                bannedImg = document.createElement("img");
                bannedImg.setAttribute("width","145");
                bannedImg.setAttribute("src","http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"+banned+"_0.jpg");
                bannedImg.setAttribute("alt","championName");
                bannedDiv.appendChild(bannedImg);  
              }

}

// using jQuery
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function toggleLogin() {
      $('#signModal').modal('hide');
      $('#loginModal').modal('toggle');
    }
function toggleSignin() {
      $('#loginModal').modal('hide');
      $('#signModal').modal('toggle');
    }

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