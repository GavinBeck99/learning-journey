// Debug practice - Using console.log to understand code

function processOrder(items, discount) {
    console.log("🔍 processOrder called");
    console.log("  items:", items);
    console.log("  discount:", discount);
    
    let total = 0;
    
    for (let i = 0; i < items.length; i++) {
      console.log(`\n  Processing item ${i}:`, items[i]);
      total = total + items[i].price * items[i].quantity;
      console.log("  Running total:", total);
    }
    
    console.log("\n  Total before discount:", total);
    
    const discountAmount = total * (discount / 100);
    console.log("  Discount amount:", discountAmount);
    
    const finalTotal = total - discountAmount;
    console.log("  Final total:", finalTotal);
    
    return finalTotal;
  }
  
  // Test data
  const shoppingCart = [
    { name: "Book", price: 25, quantity: 2 },
    { name: "Pen", price: 5, quantity: 3 },
    { name: "Notebook", price: 10, quantity: 1 }
  ];
  
  console.log("\n📦 Processing shopping cart...\n");
  const result = processOrder(shoppingCart, 10);
  console.log("\n💰 Final price:", result);