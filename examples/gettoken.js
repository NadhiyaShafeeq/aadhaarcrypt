function gettoken(){

  var url =  "http://127.0.0.1:5000/generate-token" //you can add ur own host here

  var formData = new FormData();
  formData.append("name", "Dante");
  formData.append("email", "foo@bar.com");

  try{
    var xhttp = new XMLHttpRequest();
  }catch(e){
    console.log(e)
  }

  xhttp.open("POST", url);
  xhttp.send(formData);
  xhttp.onreadystatechange = function(){
    if(this.state == 200 && this.readyState == 4){
      console.log(this.reponseText);
    }
  }
}

gettoken();
