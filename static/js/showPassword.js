
var togglePassword = document.querySelector('#togglePassword'),
    password = document.querySelector('#id_password')

togglePassword.addEventListener('click', () => {
  var type = password.getAttribute('type')
  if (type === 'password') {
    password.setAttribute('type', 'text')
    togglePassword.classList.remove("fa-eye")
    togglePassword.classList.add("fa-eye-slash")
  } else {
    password.setAttribute('type', 'password')
    togglePassword.classList.remove("fa-eye-slash")
    togglePassword.classList.add("fa-eye")
  }
})

function removeFromDOM(className = ".play-container") {
  document.querySelectorAll('.' + className).forEach(el => el.remove());
}

var closeFieldErrorBox = document.getElementsByClassName('btn-close')[0]

closeFieldErrorBox.addEventListener('click', () => {
  removeFromDOM('alert-danger')
})

var fields = document.getElementsByClassName('is-invalid')

for (let field of fields){
  console.log(field.value)
}