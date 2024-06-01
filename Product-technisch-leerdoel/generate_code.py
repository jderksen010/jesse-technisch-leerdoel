import cohere

# Stel je Cohere API-sleutel in
cohere_api_key = ''
co = cohere.Client(cohere_api_key)

# Definieer de prompt op basis van je test cases
prompt = """
Write a JavaScript module that exports four functions: sum, substract, multiply, and divide.
The functions should be able to handle the following Jest tests:

test('add function should correctly add two numbers', () => {
  expect(calculator.sum(1, 2)).toBe(3);
  expect(calculator.sum(-1, -1)).toBe(-2);
  expect(calculator.sum(0, 0)).toBe(0);
});

test('subtract function should correctly subtract two numbers', () => {
  expect(calculator.substract(5, 3)).toBe(2);
  expect(calculator.substract(0, 5)).toBe(-5);
  expect(calculator.substract(-1, -1)).toBe(0);
});

test('multiply function should correctly multiply two numbers', () => {
  expect(calculator.multiply(2, 3)).toBe(6);
  expect(calculator.multiply(0, 5)).toBe(0);
  expect(calculator.multiply(-1, -1)).toBe(1);
});

test('divide function should correctly divide two numbers', () => {
  expect(calculator.divide(6, 3)).toBe(2);
  expect(calculator.divide(5, 2)).toBe(2.5);
  expect(calculator.divide(-6, -3)).toBe(2);
  expect(() => calculator.divide(1, 0)).toThrow('Cannot divide by zero');
});

Provide the implementation in JavaScript.
Do not place the functions in the module.exports but create a separate function for each test that starts with function and ends with the name of the function, in this case use the function name that is in the test

remove all sentences that are not javascript and do not post the generated code in comments
Remove the sentence 'Here is a JavaScript module that exports the four functions you requested:'.
And remove the following characters: ``` and remove the word javascript
"""

# Maak de API-aanroep
response = co.generate(
    model='command-xlarge-nightly',  # of een ander geschikt model
    prompt=prompt,
    max_tokens=500
)

# Haal de gegenereerde code op
generated_code = response.generations[0].text.strip()

# Schrijf de gegenereerde code naar een bestand
with open('Product-technisch-leerdoel/Tests/calculator.js', 'w') as file:
    file.write(generated_code)

print("De gegenereerde code is geschreven naar calculator.js")