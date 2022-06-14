# Coffee shop

sara branch

### Any ideas from you guys are most welcome!

# Main app

This app will contain all the logic regarding:

- creation of an account,
- user login,
- user logout,
- basic template for the website.

### **index.html**

- [ ] Decide what content it should have.
- [ ] Add some content to the index page.
- [ ] Apply some css.

### **navbar.html**

- [ ] Aply some css to the navbar.
- [x] This file is in the folder templates/main/navbar.html.
- [ ] Should navbar contain signup url once the person is loged in. In the current stage of the project it is not implemented. However, we have a link within login page...
- [ ] Optionally, add a search button to the navabr. It should render all the products...

### **login.html**

- [x] Apply some css to the login form.
- [x] Perhaps position the login form in the center of the screen (horizontally) with some margin-top.

### **signup.html**

- [x] Apply some css to this page as well.
- [x] display: grid should work nice with grid template for columns set to 2 columns.

### **user.html**

- [x] This is the personal page for each user.
- [ ] This page should perhaps contain order history and on click it will render another html file with the exact order, so that the user can repeat/alter it and reorder again.

- [x] In this page show each review that user have made.

# Store app (or whatever name you would like to have)

This app will contain all the logic regarding:

- product rendering,
- shoping cart,
- checkout page,
- wish list.

### **store.html**

- [ ] Decide what content this page should have.
- [x] In principle it should contain all the products within our shop.
- [x] If we decide to categorize products, for instance types of coffee, type of coffee machines, accesories and so on, then in the store.html file should have small cards and on click it will navigate to a certain category.
- [x] Categories should perhaps also be visible in the store page.

### **product_list.card**

- [x] The easiest way is to make a simple html file with only product card and it's own css within head section.
- [x] Later we can take the css part into our static files to make it clean.
- [x] The product card should contain:
  - [x] a product image,
  - [x] Add to cart button,
  - [x] heart button to add to the wish list,
  - [x] price,
  - [x] title,
  - [ ] very short description.
- [x] For any of the above mentioned things use plain html and just do the styling. Later on we will connect it with django and python.

### **Products**

- [ ] Similar to our Blog project, as Sara suggested, we can add reviews and a loged in user can make a review/comment about each product.
- [ ] In previous case, reviews/comments should be visible at the bottom of each product file.
- [x] Decide about the look for a product card. This will be written only once and a simple for loop will render same things for all the products in our db. Google is our friend, simply google for "product card" and see what you like.
- [x] This card should have something like heart, as Sara added, so that user can put an item into a wish list.

### **cart.html**

- [x] This file should contain all the items that person have put into the cart.
- [x] It should also contain checkout button wich will on click redirect to another page.
- [ ] Apply some css for each product box. Template info are already in the page, have a look.

### **wish_list.html**

- [x] This file should contain all the items that user have put into the wish list.
- [x] Items should be rendered either as table rows or as products in our store within product card.
- [x] User should be able to add them to the card.
- [x] Once they are added to the cart, decide weather we should keep them in the list or not, probably yes so it makes another order easier.

# Some python logic

### **storeApp/\*.py**

- [x] Write some viewes and urls for the logic regarding the store app.
- [ ] More details about this will write later.
