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

// this is an exception test for the method divide. Divide must throw an exception if the zere number is 0.
test('divide of two numbers, can not devide to zero', () => {
    const result = () => { 
        calculator.divide(2, 0);
    }
    expect(result).toThrow();
})

// kwadraat
test('square number', () => { 
    expect(calculator.square(3)).toBe(9);
})

// wortel
test('squareRoot number', () => {
    expect(calculator.squareRoot(9)).toBe(3);
})

// percentage
test('calculate percentage', () => {
    expect(calculator.calculatePercentage(3, 4)).toBe(75);
})

// this test tests a method that calles 1 or more functions of: sum, substract, multiply, divide, square, squareRoot, calculatePercentage
test('add multiple funtions from above', () => {
    const result = calculator.performRandomOperation(4, 2);
    expect(result).not.toBeNaN();
})
