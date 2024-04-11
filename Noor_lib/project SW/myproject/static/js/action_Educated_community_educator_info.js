let megaMenu = document.getElementById('megaMenu');
let test = document.getElementById('test');
let header = document.getElementById('div-container');
 
let hide = document.getElementById("hide");
let main = document.getElementById("main-nav");
let settings = document.getElementById("settings");
if (hide)
{
    console.log("3");
    }
hide.onclick = function ()
{
    
    
         main.classList.toggle('open-settings');
         settings.classList.toggle('opensettings');
   
    
}

test.onclick = function ()
{
    megaMenu.classList.toggle('open-menu');
    header.classList.toggle('open-menu2');

    
}


let avatar = document.getElementById('avatar');
let settingsMenu =document.getElementById('settingsMenu');

   
avatar.onclick = function (){
    settingsMenu.classList.toggle('open-settings');
}
document.onclick = function (e)
    {
        if (e.target.id !== 'test' && e.target.id !== 'megaMenu')
        {
            megaMenu.classList.remove('open-menu');
            

               
    }
     if (e.target.id !== 'avatar' && e.target.id !== 'settingsMenu')
        {
            settingsMenu.classList.remove('open-settings');
    }
    if (e.target.id !== 'test' && e.target.id !== 'megaMenu'&&e.target.id !== 'avatar' && e.target.id !== 'settingsMenu')
        {
            header.classList.remove('open-menu2');
            }
    }