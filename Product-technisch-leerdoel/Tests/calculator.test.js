const calculator = require('./calculator')

// sum
test('sum of two numbers', () => { 
    expect(calculator.sum(1, 2)).toBe(3)
})

// min sum
test('Substract of two numbers', () => { 
    expect(calculator.substract(2, 1)).toBe(1)
})

// vermenigvuldigen
test('multiply of two numbers', () => { 
    expect(calculator.multiply(2, 2)).toBe(4)
})

// delen
test('divide of two numbers', () => {
    expect(calculator.divide(6, 3)).toBe(2)
})
