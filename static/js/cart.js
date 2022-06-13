// please read django documentation for this part.
  // I just copy/paste entire function from
  // https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax
  function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
const csrftoken = getToken('csrftoken');


console.log(user)
var btns = document.getElementsByClassName('update-cart-btn')
var test = document.getElementsByClassName('test-element')[0]




  for (let btn of btns) {
    btn.addEventListener('click', () => {
      var productId = btn.dataset.product
      var action = btn.dataset.action

      if (user != 'AnonymousUser') {
        test.innerHTML = "it works"
        updateUserOrder(productId, action)
      }
    })
  }

function updateUserOrder(productId, action) {
  test.innerHTML = 'productId :' + productId + ', action :' + action
  var url = '/update_item/'
  
  fetch(url, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken': csrftoken,
    }, 
    body:JSON.stringify({'productId': productId, 'action':action})
  })
  .then((response) => {
      return response.json();
  })
  .then((data) => {
    console.log('data: ', data)
    location.reload()
  });
}