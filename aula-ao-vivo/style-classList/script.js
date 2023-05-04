
//STYLE BUTTON E TÍTULO
const forms_title = document.getElementsByClassName('forms_title')[0];
const button = document.querySelector('button');

//STYLE TÍTULO
forms_title.style.color = '#9400D3';
forms_title.style.textTransform = 'uppercase';
//STYLE BUTTON
button.style.backgroundColor = '#FF1493';
button.style.color = '#FFFFFF';
button.style.borderRadius = '10px';
button.style.border = 'solid 2px #9400D3';
button.style.textTransform = 'uppercase';


//CAPTURANDO INPUT E MENSAGEM DE ERRO DAS TAGS DE USERNAME
const usernameInput = document.getElementById('login-usuario')
const usernameErrorMessage = document.getElementsByClassName('error-text')[0];

//CAPTURANDO INPUT E MENSAGEM DE ERRO DAS TAGS DE PASSWORD
const passwordInput = document.getElementById('login-senha');
const passwordErrorMessage = document.getElementsByClassName('error-text')[1];

//SIMULANDO INTERAÇÃO DO USUÁRIO

//USUÁRIO INSERIU USERNAME ERRADO
usernameInput.classList.add('error')
usernameErrorMessage.classList.add('visible')

//USUÁRIO ACERTOU USERNAME MAS ERROU SENHA

//SINALIZAR QUE ELE ACERTOU
usernameInput.classList.remove('error')
usernameInput.classList.add('correct')
usernameErrorMessage.classList.remove('visible')
//SINALIZAR QUE ELE ERROU
passwordInput.classList.add('error')
passwordErrorMessage.classList.add('visible')


