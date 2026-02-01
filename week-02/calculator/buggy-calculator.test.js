// Tests for buggy calculator

const { add, subtract, multiply, divide, calculatePercentage, isEven } = require('./buggy-calculator');

// Test helper function
function test(description, testFunction) {
  try {
    testFunction();
    console.log(`✅ PASS: ${description}`);
  } catch (error) {
    console.log(`❌ FAIL: ${description}`);
    console.log(`   Error: ${error.message}`);
  }
}

function expect(actual) {
  return {
    toBe(expected) {
      if (actual !== expected) {
        throw new Error(`Expected ${expected} but got ${actual}`);
      }
    }
  };
}

// Run tests
console.log('\n🐛 Running Buggy Calculator Tests...\n');

test('add 5 + 3 equals 8', () => {
  expect(add(5, 3)).toBe(8);
});

test('subtract 10 - 4 equals 6', () => {
  expect(subtract(10, 4)).toBe(6);
});

test('multiply 6 * 7 equals 42', () => {
  expect(multiply(6, 7)).toBe(42);
});

test('divide 20 / 4 equals 5', () => {
  expect(divide(20, 4)).toBe(5);
});

test('calculatePercentage: 10% of 200 equals 20', () => {
  expect(calculatePercentage(200, 10)).toBe(20);
});

test('isEven: 4 is even', () => {
  expect(isEven(4)).toBe(true);
});

test('isEven: 7 is not even', () => {
  expect(isEven(7)).toBe(false);
});

console.log('\n🔍 Tests complete! Check which ones failed.\n');