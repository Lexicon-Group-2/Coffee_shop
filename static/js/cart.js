
var trash = document.getElementsByClassName("trash-bin-img")

for (let t of trash) {
  t.addEventListener("mouseover", () => {
    t.src = "/media/trash_bin_hover.png"
    t.width = "40"
  }, false);
  t.addEventListener("mouseleave", () => {
    t.src = "/media/trash_bin.png"
    t.width = "30"
  }, false);
}

const csrftoken = getToken('csrftoken');

var btns = document.getElementsByClassName('update-cart-btn')

for (let btn of btns) {
  btn.addEventListener('click', () => {
    var productId = btn.dataset.product
    var action = btn.dataset.action

    if (user != 'AnonymousUser') {
      updateUserOrder(productId, action)
    }
  })
}

function updateUserOrder(productId, action) {
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
    location.reload()
  });
}


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