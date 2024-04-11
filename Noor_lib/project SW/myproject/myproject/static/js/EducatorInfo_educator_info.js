const BtnAdd1 = document.querySelector('.rev');
const BtnAdd3 = document.querySelector('.quot');
const DivContainer1 = document.getElementById("div-container1");
const DivContainer = document.getElementById("div-container");
BtnAdd1.addEventListener("click", AddNew);
const BtnAdd2 = document.querySelector('.book');

const DivContainer2 = document.getElementById("div-container2");
const DivContainer3 = document.getElementById("div-container3");
BtnAdd2.addEventListener("click", AddNew2);
BtnAdd3.addEventListener("click", AddNew3);
const revimg = document.querySelector('.revimg');
const bookimg = document.querySelector('.bookimg');
const quotimg = document.querySelector('.quotimg');


//المتغيات دي عشان تغير بيانات التعليقات 
var x='Book name';
var s="User name";
var y="Rate of the Book";
var z = "Text of the coment";
var a = "../img/avatar-05.png";
var w = "../html/FF.html";
var t = "../html/FF.html";

const size = 2;
var array = [size];

   //المتغيات دي عشان تغير بيانات غلاف الكتاب
 var p="../img/mainbooks2.png";
var c="نظريه الفستق";
var m="فهد الاحمدي";
var k="تفاصيل الكتاب";
var j="../html/"

for (let index = 0; index < size; index++)
{
  array[index] = document.createElement("div");
}
var dew2 = document.createElement("div");
 




bookimg.classList.toggle('active');
BtnAdd2.classList.toggle('active');
 BtnAdd2.style.setProperty('--width', '100%');
DivContainer.style.boxShadow = "0px 8px 16px 9px rgb(131 135 155 / 0%)";
DivContainer.style.padding = "0";
  while (DivContainer3.hasChildNodes()) {
    DivContainer3.removeChild(DivContainer3.firstChild);
  }
 
   for (let index = 0; index < array.length; index++)
  {
    
    
  
    
    array[index].innerHTML =
    '<a href="'+j+'"><div class="card"><div class="rate"><img src="../img/star.png" alt=""><img src="../img/rate.png" alt=""><img src="../img/rate.png" alt=""><img src="../img/rate.png" alt=""><img src="../img/rate.png" alt=""></div><div class="image"><img src="'+p+'" alt=""></div><div class="text"><h2>'+c+'</h2><p>'+m+'</p></div><div class="info"><h3>'+k+'</h3><i class="fa - solid fa - arrow - right"><img style="width:20px;filter:grayscale(70%);" src="../img/right-arrow.png" alt=""></i></div></div></a>';
 DivContainer2.appendChild(array[index]);
  }





 //العليقات

function AddNew()
{
  
 DivContainer.style.boxShadow = "0px 8px 16px 9px rgb(131 135 155)";
 DivContainer.style.padding = "30px";
  BtnAdd1.style.setProperty('--width', '100%');
  BtnAdd2.style.setProperty('--width', '0%');
  BtnAdd3.style.setProperty('--width','0%');
  revimg.classList.toggle('active');
  quotimg.classList.remove('active');
  bookimg.classList.remove('active');

  BtnAdd1.classList.toggle('active');
  BtnAdd2.classList.remove('active');
  BtnAdd3.classList.remove('active');
  
    
    
    while(DivContainer2.hasChildNodes())
  {
    DivContainer2.removeChild(DivContainer2.firstChild);
  }
  
  for (let index = 0; index < array.length; index++)
  {
    
    
  
    
    array[index].innerHTML =
      '<div class="comment"><a href="' + w + '" class="book-name">' + x + '<img src="../img/book.png" alt="" style="width: 20px"></a> <div class="content"> <div class="data" style="text-duration:rtl"><a href="' + t + '" class="user-name">' + s + '</a><br><span class="rate">' + y + '</span></br><p>' + z + '</p></div><div class="img" style="justify-content: end;width:20%!important;display:inline;"><img class="user" src="' + a + '" alt="" style="width: 60px;!important;height:60px!important"></div></div>';
    DivContainer1.appendChild(array[index]);
  }
 //غلاف الكتاب
}
function AddNew2()
{

  DivContainer.style.boxShadow = "0px 8px 16px 9px rgb(131 135 155 / 0%)";
DivContainer.style.padding = "0";
 revimg.classList.remove('active');
  bookimg.classList.toggle('active');
  quotimg.classList.remove('active');
  BtnAdd2.classList.toggle('active');
  BtnAdd1.classList.remove('active');
  BtnAdd3.classList.remove('active');
  BtnAdd2.style.setProperty('--width', '100%');
  BtnAdd1.style.setProperty('--width', '0%');
  BtnAdd3.style.setProperty('--width','0%');
 while (DivContainer1.hasChildNodes()) {
    DivContainer1.removeChild(DivContainer1.firstChild);
  }
   while (DivContainer3.hasChildNodes()) {
    DivContainer3.removeChild(DivContainer3.firstChild);
  }
 
   for (let index = 0; index < array.length; index++)
  {
    
    
  
    
    array[index].innerHTML =
    '<a href="'+j+'"><div class="card"><div class="rate"><img src="../img/star.png" alt=""><img src="../img/rate.png" alt=""><img src="../img/rate.png" alt=""><img src="../img/rate.png" alt=""><img src="../img/rate.png" alt=""></div><div class="image"><img src="'+p+'" alt=""></div><div class="text"><h2>'+c+'</h2><p>'+m+'</p></div><div class="info"><h3>'+k+'</h3><i class="fa - solid fa - arrow - right"><img style="width:20px;filter:grayscale(70%);" src="../img/right-arrow.png" alt=""></i></div></div></a>';
 DivContainer2.appendChild(array[index]);
  }
 
}

//الاقتباسات
  //المتغيات دي عشان تغير بيانات الاقتباس
 var ss="4 82 Narrated Abu Huraira Allah s Apostle said Five are regarded as martyrs They are those who die because of plague Abdominal disease drowning or a falling building etc and ";
 var zz="صحيح البخاري";
 var rr="BMW";
 var vv="../image/bmw_logo_PNG19707.png";
 var dd="لينك كاتب الاقتباس";
 var ww="لينك الكتاب اللي اكتب ليه الاقتباس";

function AddNew3()
{
  DivContainer.style.boxShadow = "0px 8px 16px 9px rgb(131 135 155 / 0%)";
DivContainer.style.padding = "0";
  
  
  BtnAdd3.style.setProperty('--width', '100%');
  BtnAdd2.style.setProperty('--width', '0%');
  BtnAdd1.style.setProperty('--width','0%');

 revimg.classList.remove('active');
  bookimg.classList.remove('active');
  quotimg.classList.toggle('active');
   BtnAdd3.classList.toggle('active');
  BtnAdd1.classList.remove('active');
  BtnAdd2.classList.remove('active');
  
    
    
    while(DivContainer2.hasChildNodes())
  {
    DivContainer2.removeChild(DivContainer2.firstChild);
  }
  
  for (let index = 0; index < array.length; index++)
  {
    
    
  
    
    array[index].innerHTML =
      '<div class="result"><div quote_id="13333" class="single-quote quote_id_13333"><div class="quote-content text-center"> <div class="opacity_background_quote"><div class="quote-content-child"><i class="fa fa-quote-left fa-flip-horizontal"></i><span class="more" style="display:inline;"> '+ss+' </span><i class="fa fa-quote-left fa-flip-horizontal"></i></div></div></div>  <div class="quote_bottom_btns"></div><a href="'+dd+'"class="quote_adder pull-left"><img loading="lazy" class="img-circle" height="25" width="25" src="'+vv+'" > '+rr+'</a><a href="'+ww+'" class="quote_book_title pull-right"><i class="fa fa-book" style="margin-right: 10px;"></i><span>'+zz+'</span></a></div></div></div>';
    DivContainer3.appendChild(array[index]);
  }
 
}