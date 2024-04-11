/*let megaMenu = document.getElementById('megaMenu');
let test = document.getElementById('test');
 let header = document.getElementById('div-container');

    

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
    }*/

    let megaMenu = document.querySelector('#megaMenu');
let test = document.querySelector('#test')



test.addEventListener('click',()=>{
    megaMenu.classList.toggle('open-menu')
})
// test.onclick().megaMenuClick()


let avatar = document.querySelector('.avatar');
let settingsMenu =document.querySelector('.settingsMenu');

avatar.addEventListener('click',()=>{
    settingsMenu.classList.toggle('open-settings')
})