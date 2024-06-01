const isPalindrome = require('./isPalindrome')

test('Tacocat returns true', () => { 
    expect(isPalindrome("tacocat")).toBe(true)
})

test('Jesse returns false', () => {
    expect(isPalindrome("Jesse")).toBe(false)
})