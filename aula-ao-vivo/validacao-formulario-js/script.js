
function togglePopup(input, label) {

  // Mostrar Popup de Campo Obrigatório
  input.addEventListener("focus",()=>{
    label.classList.add("required-popup");
  })
  
  // Ocultar Popup de Campo Obrigatório
  input.addEventListener("blur",()=>{
    label.classList.remove("required-popup");
  })
}


// ---------- VALIDAÇÃO USERNAME ---------- //
const usernameInput = document.getElementById("username");
const usernameLabel = document.querySelector('label[for="username"]');
const usernameHelper = document.getElementById("username-helper");

togglePopup(usernameInput, usernameLabel)

usernameInput.addEventListener('input', (event) => {
  const valorUsername = event.target.value;

  if (valorUsername.length <=3) {
    usernameInput.classList.remove('correct');
    usernameInput.classList.add('error');
    usernameHelper.innerText = 'Username Precisa Ter Mais de 3 Caracteres';
    usernameHelper.classList.add('visible'); 
    checkInputs.usernameInput = false;  
  } else {
    usernameInput.classList.remove('error');
    usernameInput.classList.add('correct');
    usernameHelper.classList.remove('visible');
    checkInputs.usernameInput = true;
  }
})


// ---------- VALIDAÇÃO EMAIL ---------- //
const emailInput = document.getElementById("email");
const emailLabel = document.querySelector('label[for="email"]');
const emailHelper = document.getElementById("email-helper");

togglePopup(emailInput, emailLabel)

emailInput.addEventListener('input', (event) => {
  const valorEmail = event.target.value;

  if (valorEmail.includes('@') && valorEmail.includes('.com')) {
    emailInput.classList.remove('error');
    emailInput.classList.add('correct');
    emailHelper.classList.remove('visible');
    checkInputs.emailInput = true;
  } else {
    emailInput.classList.remove('correct');
    emailInput.classList.add('error');
    emailHelper.innerText = 'O Email Precisa Incuir um "@" e um ".com"';
    emailHelper.classList.add('visible');
    checkInputs.emailInput = false;
  }
})


// ---------- VALIDAÇÃO IDADE ---------- //
const idadeInput = document.getElementById("idade");
const idadelLabel = document.querySelector('label[for="idade"]');
const idadeHelper = document.getElementById("idade-helper");

togglePopup(idadeInput, idadelLabel)

idadeInput.addEventListener('input', (event) =>{
  const valorIdade = event.target.value;

  if (valorIdade < 18) {
    idadeInput.classList.remove('correct');
    idadeInput.classList.add('error')
    idadeHelper.innerText = 'Você Deve ser Maior de 18 Anos';
    idadeHelper.classList.add('visible');
    checkInputs.idadeInput = false;
  } else {
    idadeInput.classList.remove('error');
    idadeInput.classList.add('correct')
    idadeHelper.classList.remove('visible');
    checkInputs.idadeInput = true;
  }

})


// ---------- VALIDAÇÃO SENHA ---------- //
const senhaInput = document.getElementById("senha");
const senhaLabel = document.querySelector('label[for="senha"]');
const senhaHelper = document.getElementById("senha-helper");

togglePopup(senhaInput, senhaLabel)

senhaInput.addEventListener('blur', (event) => {
  const valorSenha = event.target.value;

  if (valorSenha === "") {
    senhaInput.classList.add('error');
    senhaInput.classList.remove('correct');
    senhaHelper.innerText = 'O Campo Não pode Estar Vazio';
    senhaHelper.classList.add('visible');
    checkInputs.senhaInput = false;
  } else {
    senhaInput.classList.remove('erro');
    senhaInput.classList.add('correct')
    senhaHelper.classList.remove('visible');
    checkInputs.senhaInput = true;
  }
})


// ---------- VALIDAÇÃO CONFIRMA SENHA ---------- //
const confirmaSenhaInput = document.getElementById("confirma-senha");
const confirmaSenhaLabel = document.querySelector('label[for="confirma-senha"]');
const confirmaSenhaHelper = document.getElementById("confirma-senha-helper");

togglePopup(confirmaSenhaInput, confirmaSenhaLabel)

confirmaSenhaInput.addEventListener('blur', (event) =>{
  const valorConfirma = event.target.value;

  if (valorConfirma === senhaInput.value ) {
    confirmaSenhaInput.classList.add('correct');
    confirmaSenhaInput.classList.remove('erro');
    confirmaSenhaHelper.classList.remove('visible'); 
    checkInputs.confirmaSenhaInput = true;      
  }else{
    confirmaSenhaInput.classList.remove('correct');
    confirmaSenhaInput.classList.add('error');
    confirmaSenhaHelper.innerText = 'As Senhas Precisam Ser Iguais';
    confirmaSenhaHelper.classList.add('visible');
    checkInputs.confirmaSenhaInput = false;
  }
})


// ---------- ENVIAR FORMULÁRIO ---------- //
const btnSubmit = document.querySelector("button[type ='submit']")

const checkInputs = {
  usernameInput: false,
  idadeInput:false,
  emailInput: false,
  senhaInput: false,
  confirmaSenhaInput: false
}

btnSubmit.addEventListener("click", (e) =>{
  if (checkInputs.usernameInput == false ||
    checkInputs.emailInput == false ||
    checkInputs.senhaInput == false ||
    checkInputs.confirmaSenhaInput == false
    ){
    e.preventDefault()
    alert('Os Campos Obrigatórios Precisam Ser Preenchidos Corretamente')
  } else {
    alert("Formulário Enviado Com Sucesso")
  }
})