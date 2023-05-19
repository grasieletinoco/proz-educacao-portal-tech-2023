const voltarPaginaInicial = document.getElementById("back_index");

document.addEventListener("keyup", (event) => {
  if (event.code == "Backspace"){
    voltarPaginaInicial.click();
  }
})