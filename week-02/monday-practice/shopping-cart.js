const TAX_RATE = 1.1;
const DISCOUNT_RATE = 0.1;
const DISCOUNT_THRESHOLD = 100;

function calculateSubtotal(cart) {
    let subtotal = 0;

    for (let i = 0; i < cart.length; i++) {
        subtotal = subtotal + (cart[i].price * cart[i].quantity)
    }
    return subtotal;
}

function applyDiscount (total)
{    if (total > DISCOUNT_THRESHOLD) {
        total = total - (total * DISCOUNT_RATE);
    }
    return total;
}

function applyTax (total) {
    total = total * TAX_RATE;
    return total;
}

function processCart (cart) {
    const subtotal = calculateSubtotal(cart);
    const afterDiscount = applyDiscount(subtotal);
    const finalPrice = applyTax (afterDiscount);
    return finalPrice;
}

const cart = [
    {price: 20, quantity: 4},
    {price: 42, quantity: 3},
    {price: 72, quantity: 1}
];

console.log(processCart(cart));