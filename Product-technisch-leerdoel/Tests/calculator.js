module.exports = {
    sum: function(number1, number2) {
        return number1 + number2;
    },
    substract: function(number1, number2) {
        return number1 - number2;
    },
    multiply: function(number1, number2) {
        return number1 * number2;
    },
    divide: function(number1, number2) {
        if (number2 === 0) {
            throw new Error('Cannot divide by zero');
        }
        return Math.floor(number1 / number2);
    },
    square: function(number) {
        return number * number;
    },
    squareRoot: function(number) {
        return Math.sqrt(number);
    },
    calculatePercentage: function(part, whole) {
        return Math.floor((part / whole) * 100);
    },
    performRandomOperation: function(number1, number2) {
        const operations = [this.sum, this.substract, this.multiply, this.divide, this.square, this.squareRoot, this.calculatePercentage];
        const randomIndex = Math.floor(Math.random() * operations.length);
        const randomOperation = operations[randomIndex];
        return randomOperation(number1, number2);
    }
};