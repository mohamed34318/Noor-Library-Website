const test1 = document.getElementById('ww');
const body = document.getElementById('body');
const megaMenu1 = document.getElementById('ee');
const megaMenu2 = document.getElementById('ee2');
const div2 = document.getElementById('div2');
const btn1 = document.getElementById('btn1');
const commentBox = document.getElementById('commentBox');
const img = document.getElementById('img');
const span = document.getElementById('span');
const btn2 = document.getElementById('btn2');
const btn3 = document.getElementById('btn3');
const btn4 = document.getElementById('btn4');
const btn5 = document.getElementById('btn5');
const btn11 = document.getElementById('btn11');
const btn22 = document.getElementById('btn22');
const btn33 = document.getElementById('btn33');
const btn44 = document.getElementById('btn44');
const btn55 = document.getElementById('btn55');
const ad = document.getElementById('ad');
const dat = document.getElementById('dat');
const sidebar = document.getElementById("sidebar");
const image = document.getElementById("image");
const data = document.getElementById("data");
const authorDescription = document.getElementById("authorDescription");
const bookDescription = document.getElementById("bookDescription");
const bookReview = document.getElementById("bookReview");
const header = document.getElementById("header");
const content = document.getElementById("content");
const quot1 = document.getElementById("quot");
const h3 = document.getElementById("h3");
const rate1= document.getElementById("rate");
 document.onclick = function (e)
{
  if (e.target.id !== 'span' &&e.target.id !== 'div2' &&e.target.id !== 'ee' && e.target.id !== 'ww')
  {
    ww.classList.remove('active');
    ee.classList.remove('active');

    
     
   
   }
   if (e.target.id !== 'div2' &&e.target.id !== 'span' &&e.target.id !== 'ee'&&e.target.id !== 'ww' )
  {
     body.classList.remove('active');
  sidebar.classList.remove('active');
  image.classList.remove('active');
  data.classList.remove('active');
  authorDescription.classList.remove('active');
  bookDescription.classList.remove('active');
  bookReview.classList.remove('active');
      header.classList.remove('active');
      h3.classList.remove('active');
       rate1.classList.remove('active');

    
     
   
   }
   if (e.target.id !== 'dat' &&e.target.id !== 'ee2'&&e.target.id !== 'ad'&&e.target.id !== 'commentBox'&&e.target.id !== 'btn1'&&e.target.id !== 'btn2'&&e.target.id !== 'btn3'&&e.target.id !== 'btn4'&&e.target.id !== 'btn5'&&e.target.id !== 'btn11'&&e.target.id !== 'btn22'&&e.target.id !== 'btn33'&&e.target.id !== 'btn44'&&e.target.id !== 'btn55' )
  {
     body.classList.remove('active1');
  sidebar.classList.remove('active1');
  image.classList.remove('active1');
  data.classList.remove('active1');
  authorDescription.classList.remove('active1');
  bookDescription.classList.remove('active1');
  bookReview.classList.remove('active1');
      header.classList.remove('active1');
      h3.classList.remove('active1');
       rate1.classList.remove('active1');

    
     
   
    }
    if (e.target.id !== 'quot' &&e.target.id !== 'dat' &&e.target.id !== 'ee2'&&e.target.id !== 'ad'&&e.target.id !== 'commentBox' )
  {
     body.classList.remove('active2');
  sidebar.classList.remove('active2');
  image.classList.remove('active2');
  data.classList.remove('active2');
  authorDescription.classList.remove('active2');
  bookDescription.classList.remove('active2');
  bookReview.classList.remove('active2');
       header.classList.remove('active2');
       h3.classList.remove('active2');
        rate1.classList.remove('active2');

    
     
   
   }
    if (e.target.id !== 'commentBox'&&e.target.id !== 'quot'&&e.target.id !== 'ee2'&&e.target.id !== 'dat'&&e.target.id !== 'ad' )
    {
       ww.classList.remove('active1');
       ee2.classList.remove('active1');
    }
   if (e.target.id !== 'img' &&e.target.id !== 'ee2' &&e.target.id !== 'div2'&&e.target.id !== 'span'&&e.target.id !== 'btn1'&&e.target.id !== 'btn11'&&e.target.id !== 'btn22'&&e.target.id !== 'btn33'&&e.target.id !== 'btn44'&&e.target.id !== 'btn55'&&e.target.id !== 'btn2'&&e.target.id !== 'btn3'&&e.target.id !== 'btn4'&&e.target.id !== 'btn5'&&e.target.id !== 'commentBox'&&e.target.id !== 'ad'&&e.target.id !== 'dat')
  {
    ww.classList.remove('active');
     ee2.classList.remove('active');
     btn11.classList.remove('active');
     btn22.classList.remove('active');
     btn33.classList.remove('active');
     btn44.classList.remove('active');
     btn55.classList.remove('active');
      
    
   }
 
  
}

test1.onclick = function ()
{
    
    
   megaMenu1.classList.toggle('active');
   
  body.classList.toggle('active');
  sidebar.classList.toggle('active');
  image.classList.toggle('active');
  data.classList.toggle('active');
  authorDescription.classList.toggle('active');
  bookDescription.classList.toggle('active');
  bookReview.classList.toggle('active');
   header.classList.toggle('active');
   rate1.classList.toggle('active');
   h3.classList.toggle('active');
   
    
}
btn1.onclick = function ()
{
    
    
         megaMenu2.classList.toggle('active');
         ad.innerText = "اضف مراجعة";
  btn11.classList.toggle('active');
  body.classList.toggle('active1');
  sidebar.classList.toggle('active1');
  image.classList.toggle('active1');
  data.classList.toggle('active1');
  authorDescription.classList.toggle('active1');
  bookDescription.classList.toggle('active1');
  bookReview.classList.toggle('active1');
   header.classList.toggle('active1');
   rate1.classList.toggle('active1');
   h3.classList.toggle('active1');
    
}
btn2.onclick = function ()
{
    
    
         megaMenu2.classList.toggle('active');
      ad.innerText = "اضف مراجعة";
  btn22.classList.toggle('active');
    body.classList.toggle('active1');
  sidebar.classList.toggle('active1');
  image.classList.toggle('active1');
  data.classList.toggle('active1');
  authorDescription.classList.toggle('active1');
  bookDescription.classList.toggle('active1');
  bookReview.classList.toggle('active1');
   header.classList.toggle('active1');
   rate1.classList.toggle('active1');
   h3.classList.toggle('active1');
    
}
btn3.onclick = function ()
{
    
    
         megaMenu2.classList.toggle('active');
         ad.innerText = "اضف مراجعة";
  btn33.classList.toggle('active');
    body.classList.toggle('active1');
  sidebar.classList.toggle('active1');
  image.classList.toggle('active1');
  data.classList.toggle('active1');
  authorDescription.classList.toggle('active1');
  bookDescription.classList.toggle('active1');
  bookReview.classList.toggle('active1');
   header.classList.toggle('active1');
   rate1.classList.toggle('active1');
   h3.classList.toggle('active1');
    
}
btn4.onclick = function ()
{
    
    
         megaMenu2.classList.toggle('active');
        ad.innerText = "اضف مراجعة";
  btn44.classList.toggle('active');
     body.classList.toggle('active1');
  sidebar.classList.toggle('active1');
  image.classList.toggle('active1');
  data.classList.toggle('active1');
  authorDescription.classList.toggle('active1');
  bookDescription.classList.toggle('active1');
  bookReview.classList.toggle('active1');
   header.classList.toggle('active1');
   rate1.classList.toggle('active1');
   h3.classList.toggle('active1');
    
}
btn5.onclick = function ()
{
    
    
         megaMenu2.classList.toggle('active');
   ad.innerText = "اضف مراجعة";
   
  btn55.classList.toggle('active');
     body.classList.toggle('active1');
  sidebar.classList.toggle('active1');
  image.classList.toggle('active1');
  data.classList.toggle('active1');
  authorDescription.classList.toggle('active1');
  bookDescription.classList.toggle('active1');
  bookReview.classList.toggle('active1');
   header.classList.toggle('active1');
   rate1.classList.toggle('active1');
   h3.classList.toggle('active1');
    
}
quot1.onclick = function ()
{
    
    
         megaMenu2.classList.toggle('active1');
   ad.innerText = "اضف اقتباس";
   commentBox.ariaPlaceholder="ff"
  
   body.classList.toggle('active2');
    h3.classList.toggle('active2');
  sidebar.classList.toggle('active2');
  image.classList.toggle('active2');
  data.classList.toggle('active2');
  authorDescription.classList.toggle('active2');
  bookDescription.classList.toggle('active2');
  bookReview.classList.toggle('active2');
   header.classList.toggle('active2');
   rate1.classList.toggle('active2');
   h3.classList.toggle('active1');
    
}


function myFunction() {
   alert("this book is added in the Shopping cart...!");
 }

 function myFunction2() {
   alert("order are done...!");
 }



