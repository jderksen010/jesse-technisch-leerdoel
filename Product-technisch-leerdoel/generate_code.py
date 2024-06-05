import cohere
import subprocess

def readCalculatorTestFile(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      js_content = file.read()
    return js_content
  except FileNotFoundError:
    return 'File not found.'
  except Exception as e:
    return str(e)

# Stel je Cohere API-sleutel in
cohere_api_key = '7Qw4MRgR92E4sriEvoL5XKMxN00LpwLYuZYLzSQi'
co = cohere.Client(cohere_api_key)

js_content = readCalculatorTestFile('Product-technisch-leerdoel/Tests/calculator.test.js')

# Definieer de prompt op basis van je test cases
prompt = f"""
Write a JavaScript module that exports all the functions in the following js test file:
{js_content}

The functions should be able to handle all the given Jest tests. And all the tests must be succeeded.
Never let the result of an test ends on 2 numbers after the comma but use whole numbers like 75 instead of 75.00.

And for the test about randomOperation, don't use the following code because then the test failed:
const randomOperation = operations[Math.floor(Math.random() * operations.length)];
return randomOperation(number1, number2);

Provide the implementation in JavaScript. Place all the functions in the module.exports.
Remove all sentences that are not JavaScript and do not post the generated code in comments.
Remove the sentence 'Here is a JavaScript module that contains the functions you requested:'.
And remove the following characters: ``` and remove the word JavaScript & js.
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
def run_command(command):
    try:
        # Run the npm test command
        result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding='utf-8')
        
        # Print the output
        print("Test Output:\n", result.stdout)
        
        # Print any errors
        if result.stderr:
            print("Errors:\n", result.stderr)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("Command executed successfully.")
        else:
            print("Command failed.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to run the commands
command_run_tests = 'npm test'
command_run_generateJava = 'python Product-technisch-leerdoel/generate_java_code.py'
run_command(command_run_tests)
run_command(command_run_generateJava)
