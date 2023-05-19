const linkPerfil = document.getElementById("link-perfil");
const navSecundaria = document.getElementById("nav-perfil");
const linkMeusDados = document.getElementById("link-perfil-dados");
/*
linkPerfil.addEventListener("mouseover", ()=> {
  navPerfil.style.display = "block"
})
*/

/*
document.addEventListener("keyup", (event)=> {
  if(navSecundaria.style.display == "block" && event.code == "Digit1"){
    linkMeusDados.click()
  }
   else if (event.code == "Digit1") {
    navSecundaria.style.display = "block";
  }
})
*/

/*
document.addEventListener("keyup", (event)=> {
  if (event.code == "Digit1") {
    if (navSecundaria.style.display == "block") {
      linkMeusDados.click()
    } else {
      navSecundaria.style.display = "block";
    }
  };
   
})
*/

document.addEventListener("keyup", (event)=> {
  if(event.code == 'Escape'){
    navSecundaria.style.display = "none"
  }

  if (event.code == "Digit1") {
    if (navSecundaria.style.display == "block") {
      linkMeusDados.click()

    } else {
      navSecundaria.style.display = "block";
    }
  };
   
})

