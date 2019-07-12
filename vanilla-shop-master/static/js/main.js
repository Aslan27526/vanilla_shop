let products = document.getElementsByClassName("product");

let cart = document.getElementById("cart");

let cartItems = {};

[...products].forEach((element, index, array) => {
    element.addEventListener("click", function() {
        let id = this.id;

        if (id in cartItems) {
            cartItems[id]++;
        } else {
            cartItems[id] = 1;
        }

        console.log(cartItems);

        let total = 0;

        Object.entries(cartItems).forEach(([key, value]) => {
            total += value;
        });
        cart.textContent = total;
    });
});