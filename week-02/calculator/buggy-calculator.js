// Buggy calculator - Find and fix the bugs!

function add(a, b) {
    return a + b;
  }
  
  function subtract(a, b) {
    return a - b;  // BUG 1: Should be a - b
  }
  
  function multiply(a, b) {
    return a * b;
  }
  
  function divide(a, b) {
    return a / b;  // BUG 2: No check for division by zero
  }
  
  function calculatePercentage(number, percent) {
    return number / percent;  // BUG 3: Should be (number * percent) / 100
  }
  
  function isEven(number) {
    return number % 2 === 0;  // BUG 4: Should be === 0
  }
  
  // Export for testing
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { add, subtract, multiply, divide, calculatePercentage, isEven };
  }