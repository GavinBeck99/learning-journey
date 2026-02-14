// Calculator tests

// Import our test framework. test and expect are the functions in ./test-framework
const { test, expect } = require('./test-framework');

/* Import calculator functions, add, subtract, mutliply and divide are the 
functions in ./calculator
*/
const { add, subtract, multiply, divide } = require('./calculator');

// Write tests
test('add 2 + 3 equals 5', () => {
  const result = add(2, 3);
  expect(result).toBe(5);
});

test('subtract 10 - 4 equals 6', () => {
  const result = subtract(10, 4);
  expect(result).toBe(6);
});

test('multiply 3 * 4 equals 12', () => {
  const result = multiply(3, 4);
  expect(result).toBe(12);
});

test('divide 20 / 4 equals 5', () => {
  const result = divide(20, 4);
  expect(result).toBe(5);
});

test('divide by zero throws error', () => {
  try {
    divide(10, 0);
    throw new Error('Should have thrown error');
  } catch (error) {
    expect(error.message).toBe('Cannot divide by zero');
  }
});