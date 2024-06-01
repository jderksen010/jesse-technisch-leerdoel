import openai

# Set your OpenAI API key
openai.api_key = 'MIJN_SECRET'

# Define the prompt based on your test cases
prompt = """
Write a JavaScript module that exports four functions: add, subtract, multiply, and divide.
The functions should be able to handle the following Jest tests:

test('add function should correctly add two numbers', () => {
  expect(calculator.add(1, 2)).toBe(3);
  expect(calculator.add(-1, -1)).toBe(-2);
  expect(calculator.add(0, 0)).toBe(0);
});

test('subtract function should correctly subtract two numbers', () => {
  expect(calculator.subtract(5, 3)).toBe(2);
  expect(calculator.subtract(0, 5)).toBe(-5);
  expect(calculator.subtract(-1, -1)).toBe(0);
});

test('multiply function should correctly multiply two numbers', () => {
  expect(calculator.multiply(2, 3)).toBe(6);
  expect(calculator.multiply(0, 5)).toBe(0);
  expect(calculator.multiply(-1, -1)).toBe(1);
});

test('divide function should correctly divide two numbers', () => {
  expect(calculator.divide(6, 3)).toBe(2);
  expect(calculator.divide(5, 2)).toBe 2.5);
  expect(calculator.divide(-6, -3)).toBe 2);
  expect(() => calculator.divide(1, 0)).toThrow('Cannot divide by zero');
});

Provide the implementation in JavaScript.
"""

# Make the API call with the new API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500
)

# Print the generated code
print(response['choices'][0]['message']['content'].strip())