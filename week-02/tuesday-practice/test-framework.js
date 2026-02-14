// both functions (below), together, form a working test framework
// test() - runs tests and catches errors
function test(description, testfunction) {
  try {
    testfunction();

    console.log('✅ PASS: ${description}');
  } catch(error) {
    console.log('❌ FAILED: ${description}');
    console.log('    Error: ${error.message}');
  }
}
// expect() - makes assertions and throws errors
function expect(actual) {
  return {
    toBe(expected) {
      if (actual !== expected) {
        throw new Error('Expected ${expected} but got ${actual}');
      }
  }
    };
  }

  module.exports = {test, expect};

  

