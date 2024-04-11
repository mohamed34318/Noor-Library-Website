const BtnAdd = document.querySelector('.addComment');

const DivContainer = document.getElementById("div2-container");
BtnAdd.addEventListener("click", AddNew);

var x='Educator name';
var s="50";
var y="12";
var z = "3";
var a = "../img/avatar-05.png";
var w = "../html/Educator.html";
var d = "8";

function AddNew()
{
    
  var dew = document.createElement("div");
  
  var ssw =document.getElementsByName('body');
  dew.innerHTML =
    '<div class="educator"><a href="'+w+'"><div class="content"><img src="'+a+'"><h2>'+x+'</h2><span></span><div><div class="row"> <div class="rate1" style="direction:ltr!impotant"><img src="../img/military-rank.png" ><p>'+z+'</p><h4>الرتبه في كل الايام</h4></div><div class="rate1" style="direction:rtl"><p>'+d+'</p><h4 class="rank">ترتيب اليوم</h4><img src="../img/military-rank.png" ></div></div><div class="row"> <div class="rate" style="direction:ltr"><p>'+y+'</p><h4>الكتب المنشورة</h4><i class="fa fa-book"  style=" float: left;   color: #45b09e;margin-left:4px"></i></div><div class="rate"><img src="../img/285661_star_icon.png"><h4>التقييم</h4><img src="../img/285661_star_icon.png"><img src="../img/285661_star_icon.png"><img src="../img/285661_star_icon.png"><img src="../img/1976054_fav_favorite_favorites_love_star_icon.png"><p>('+s+')</p></div></div></div></div></a></div>';
  DivContainer.appendChild(dew);

 
}