// Calculator tests
// 'require('./calculator')' is a js command that imports code from another file
/* this part of the code - {add, subtract, multiply, divide} - is importing
the functions from the calculator.js file */
const { add, subtract, multiply, divide } = require('./calculator');

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
    },
    toThrow() {
      let thrown = false;
      try {
        actual();
      } catch {
        thrown = true;
      }
      if (!thrown) {
        throw new Error('Expected function to throw an error');
      }
    }
  };
}

// Run tests
console.log('\n🧪 Running Calculator Tests...\n');

test('add 2 + 3 equals 5', () => {
  expect(add(2, 3)).toBe(5);
});

test('subtract 5 - 2 equals 3', () => {
  expect(subtract(5, 2)).toBe(3);
});

test('multiply 3 * 4 equals 12', () => {
  expect(multiply(3, 4)).toBe(12);
});

test('divide 10 / 2 equals 5', () => {
  expect(divide(10, 2)).toBe(5);
});

test('divide by zero throws error', () => {
  expect(() => divide(10, 0)).toThrow();
});

console.log('\n✨ Tests complete!\n');