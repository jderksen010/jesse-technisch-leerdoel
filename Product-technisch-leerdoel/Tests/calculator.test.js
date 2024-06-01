const calculator = require('./calculator')

// sum
test('sum of two numbers', () => { 
    expect(sum(1, 2)).toBe(3)
})

// min sum
test('2 min 1 = 1', () => { 
    expect(subtract(2, 1)).toBe(1)
})

// vermenigvuldigen
test('2 * 2 = 4', () => { 
    expect(multiply(2, 2)).toBe(4)
})

// delen
test('6 : 3 = 2', () => {
    expect(divide(6, 3)).toBe(2)
})
