var first = 0;
var last = 1;
var length = document.getElementsByClassName("slider-list")[0].children.length - 1;
$(document).ready(function(){   
  document.getElementById("prevButton").style.display = 'none';
  if(length < 2){
    document.getElementById("nextButton").style.display = 'none';
  }
});
$("#prevButton").click(function(){
  if(first > -1){    
    document.getElementById(last).style.display = 'none';
    first--;
    last--;
    document.getElementById(first).style.display = 'inline-block';
    document.getElementById("nextButton").style.display = 'inline-block';
  }
  if(first == 0){
    document.getElementById("prevButton").style.display = 'none';
  }else{
    document.getElementById("prevButton").style.display = 'inline-block';
  }
});
$("#nextButton").click(function(){
  if(last < length){    
    document.getElementById(first).style.display = 'none';
    first++;
    last++;
    document.getElementById(last).style.display = 'inline-block';
    document.getElementById("prevButton").style.display = 'inline-block';
  }
  if(last == length){
    document.getElementById("nextButton").style.display = 'none';
  }else{
    document.getElementById("nextButton").style.display = 'inline-block';
  }
});