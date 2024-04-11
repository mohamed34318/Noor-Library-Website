const BtnAdd = document.querySelector('.addComment');

const DivContainer = document.getElementById("div-container");
BtnAdd.addEventListener("click", AddNew);

var x='Book name';
var s="User name";
var y="Rate of the Book";
var z = "Text of the cooment";
var a = "../img/avatar-05.png";
var w = "../html/FF.html";
var t = "../html/FF.html";

function AddNew()
{
    
  var dew = document.createElement("div");
  
  var ssw =document.getElementsByName('body');
  dew.innerHTML =
    '   <div class="comment"><a href="'+w+'" class="book-name">' +x+ '<img src="../img/book.png" alt="" style="width: 20px"></a> <div class="content"> <div class="data" style="text-duration:rtl"><a href="'+t+'" class="user-name">'+s+'</a><br><span class="rate">'+y+'</span></br><p>'+z+'</p></div><div class="img" style="justify-content: end;"jac><img class="user" src="'+a+'" alt="" style="width: 40px;"></div></div>';
  DivContainer.appendChild(dew);

 
}
