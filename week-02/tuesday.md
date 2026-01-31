# Week 2 - Tuesday: Testing Fundamentals

**Date:** January 31, 2026  
**Time Spent:** 2 hours  
**Status:** ✅ Complete

---

## 🎯 What I Accomplished

### Built a Tested Calculator
- Created calculator.js with 4 functions (add, subtract, multiply, divide)
- Created calculator.test.js with 5 tests
- Ran tests with Node.js
- **ALL 5 TESTS PASSED!** ✅

### Wrote Real Tests
- Unit tests for each calculator function
- Error handling test (divide by zero)
- Used test helper functions
- Used expect assertions

---

## 💡 Key Learnings

### Why Testing Matters
- Tests verify code works correctly
- Catch bugs before users find them
- Give confidence when making changes
- Tests are separate files (kept permanently)
- Professional developers always test

### Types of Tests
1. **Unit Tests** - Test one function (most common)
2. **Integration Tests** - Test multiple parts together
3. **End-to-End Tests** - Test complete user flows
- Testing pyramid: Many unit tests, fewer integration, fewest E2E

### JavaScript Concepts Learned

**Arrow Functions `() => {}`:**
- Modern way to write functions
- Shorter syntax than traditional functions
- Used for callbacks (passing functions to functions)
- Example: `const add = (a, b) => a + b`

**`const` vs `let` vs `var`:**
- `const` = cannot reassign (use by default)
- `let` = can reassign (use when value changes)
- `var` = old way (never use)
- `const` allows modifying object/array contents

**Destructuring:**
- Extract values from objects/arrays
- `const { add, subtract } = require('./calculator')`
- Cleaner than `calculator.add()` every time

**`require()` and `module.exports`:**
- `require()` imports code from other files
- `module.exports` makes code available to other files
- Enables code reuse and organization

**`expect()` Pattern:**
- Test assertion helper
- Returns object with matcher methods
- `expect(value).toBe(expected)` - check equality
- `expect(fn).toThrow()` - check for errors
- Reads like English: "expect add(2,3) to be 5"

---

## 🎓 Test Structure Breakdown

### **1. Import Code to Test**
```javascript
const { add, subtract, multiply, divide } = require('./calculator');
```

### **2. Test Helper Functions**
```javascript
function test(description, testFunction) { ... }
function expect(actual) { return { toBe(), toThrow() }; }
```

### **3. Actual Tests**
```javascript
test('add 2 + 3 equals 5', () => {
  expect(add(2, 3)).toBe(5);
});
```

---

## 🔧 How Tests Work

**When I run `node calculator.test.js`:**

1. Node loads the test file
2. Imports functions from calculator.js
3. Runs each test() call in order
4. Each test calls expect() with actual value
5. expect() returns object with matchers (toBe, toThrow)
6. Matcher checks if test passes or fails
7. test() catches errors and prints ✅ or ❌
8. All results displayed in console

**Test Flow Example:**
```
test() → execute function → expect(result) → .toBe(expected)
                              ↓
                        if match: pass ✅
                        if different: throw error → test() catches → fail ❌
```

---

## 🤔 Challenges & Solutions

### Challenge 1: File Not Creating with echo
- **Issue:** calculator.js not appearing in folder
- **Solution:** Created file directly in Cursor
- **Learning:** Multiple ways to create files, use what works

### Challenge 2: Understanding Arrow Functions
- **Issue:** `() => {}` syntax was unfamiliar
- **Solution:** Learned it's modern function syntax
- **Understanding:** Arrow functions perfect for callbacks

### Challenge 3: Understanding expect()
- **Issue:** How does expect() work internally?
- **Solution:** Analyzed the function I wrote - returns object with methods
- **Insight:** It's just JavaScript! Nothing magical.

---

## 📊 Test Results
```
🧪 Running Calculator Tests...

✅ PASS: add 2 + 3 equals 5
✅ PASS: subtract 5 - 2 equals 3
✅ PASS: multiply 3 * 4 equals 12
✅ PASS: divide 10 / 2 equals 5
✅ PASS: divide by zero throws error

✨ Tests complete!
```

**Success Rate:** 5/5 (100%) ✅

---

## 🌟 Professional Insights

### Testing in Real World
- Professional projects have hundreds/thousands of tests
- Tests run automatically on every code change
- Can't deploy code without passing tests
- Tests are documentation of how code should work

### Code Organization
- Separate test files from source code
- Clear naming: `file.js` and `file.test.js`
- Tests stay in project but don't ship to users

### Testing Best Practices
- Test one thing per test
- Clear test descriptions
- Test both success and error cases
- Keep tests simple and readable

---

## 💭 Reflections

### What Surprised Me
- How satisfying it is to see all tests pass ✅
- Tests are just JavaScript functions
- Arrow functions are everywhere in modern JS
- Testing makes me more confident in my code

### What Clicked Today
- **Arrow functions:** Short syntax for passing functions
- **expect pattern:** Returns object with methods - elegant!
- **const vs let:** Use const by default, makes code safer
- **Test structure:** Separate files, descriptive names, clear assertions

### Confidence Growth
- **Monday:** Understanding code quality - 9/10
- **Tuesday:** Writing and running tests - 9/10
- **JavaScript concepts:** Arrow functions, const, destructuring - 8/10

---

## 📝 Code Snippets to Remember

### Arrow Function Patterns
```javascript
// No parameters
const sayHi = () => console.log("Hi!");

// One parameter (can omit parentheses)
const double = x => x * 2;

// Multiple parameters
const add = (a, b) => a + b;

// Multiple lines (need braces and return)
const add = (a, b) => {
  console.log("Adding...");
  return a + b;
};
```

### Test Pattern
```javascript
test('description', () => {
  expect(actualValue).toBe(expectedValue);
});
```

### Module Pattern
```javascript
// Export
module.exports = { add, subtract };

// Import
const { add, subtract } = require('./calculator');
```

---

## 🎯 Next Steps

### Tomorrow (Wednesday)
- More testing practice
- Learn about debugging
- Test-Driven Development (TDD)

### Skills to Practice
- Writing more complex tests
- Testing edge cases
- Error handling patterns

---

## 📚 Resources Used

- Node.js for running tests
- JavaScript arrow functions
- Module system (require/exports)
- Custom test framework (built myself!)

---

**Confidence Level:** 9/10 🚀  
**Favorite Moment:** Seeing all 5 tests pass! ✅  
**Key Takeaway:** Testing gives confidence that code works correctly

---

---

## 📺 LinkedIn Learning: TDD Course

**Course:** JavaScript: Test-Driven Development (ES6)  
**Sections Watched:** TDD Basics + Writing Unit Tests  
**Time:** 28 minutes  
**Link:** https://www.linkedin.com/learning/javascript-test-driven-development-es6

### What I Learned

**Test-Driven Development (TDD) Approach:**
- Write tests BEFORE writing code (opposite of what I knew!)
- Red-Green-Refactor cycle:
  1. **Red:** Write a failing test
  2. **Green:** Write minimum code to pass
  3. **Refactor:** Improve code while keeping tests passing
- This ensures code is testable from the start

**Professional Testing Frameworks:**
- Jest - Facebook's testing framework (industry standard)
- Mocha - Alternative testing framework
- These provide more features than my custom test helper
- Will learn Jest in upcoming lessons

**Types of Tests (Reinforced):**
- **Unit tests:** Test individual functions (what I built!)
- **Integration tests:** Test multiple components together
- **End-to-end tests:** Test complete user workflows
- TDD works best with unit tests

### Key Takeaways

**Biggest Insight:**
TDD can improve code confidence and save developers time in the future. It helps developers test and enhance code features as the code becomes more complicated, and potentially as comments become outdated to the updated code.

**Product Management Perspective:**
As a Product Owner and manager of the digital learning ecosystem at UTS, I know we do testing AFTER the product has been developed. TDD flips this - you test FIRST, then build. This is a fundamental shift in approach.

**This means:**
- Fewer bugs in production
- Code is designed to be testable
- Easier to add features without breaking existing code
- Tests serve as living documentation (unlike comments that get outdated)

### What Made Sense

**Red-Green-Refactor Cycle:**
This workflow clicked immediately:
1. Write test for feature you want
2. See it fail (red)
3. Write code to make it pass (green)
4. Clean up code (refactor)
5. Repeat

**Test Structure:**
The pattern I built matches professional standards:
- Arrange (set up)
- Act (execute function)
- Assert (check result)

This is exactly what `expect(add(2, 3)).toBe(5)` does!

### What Surprised Me

**TDD is Backwards from What I Knew:**
In product development at UTS:
- Build feature → Test feature → Deploy
  
With TDD:
- Write test → Build feature → Verify → Deploy

**Benefits I Hadn't Considered:**
- Tests prevent regression (breaking old features when adding new ones)
- Code is naturally more modular (easier to test = better design)
- Confidence to refactor without fear
- Tests document how code should behave

### Connection to My Work

**At UTS:**
- We test learning platforms after development
- Sometimes discover issues late in process
- Changes can be risky (might break existing features)

**With TDD:**
- Would catch issues immediately
- Safe to make changes (tests verify nothing broke)
- Better quality from the start
- Less time fixing bugs later

### Next Learning Goals

**Need to Learn:**
- How to use npm for testing (not just `node file.js`)
- Jest framework features (mocking, coverage, watch mode)
- When TDD makes sense vs when it doesn't
- Testing more complex code (async, APIs, databases)

**Questions for Future:**
- How do you write tests for UI/frontend?
- What about testing external services?
- How much time does TDD actually save?
- How to convince teams to adopt TDD?

### Confidence Check

**Before TDD Course:** Understood testing basics - 8/10  
**After TDD Course:** Understand professional TDD workflow - 9/10  
**Ready to:** Use testing frameworks like Jest and apply TDD in practice

---

**End of Tuesday - Testing Foundations Solid!** 🎉