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