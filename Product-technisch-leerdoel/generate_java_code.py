import cohere
import os

def read_calculatorJsFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            js_content = file.read()
        return js_content
    except FileNotFoundError:
        return 'File not found.'
    except Exception as e:
        return str(e)

js_content = read_calculatorJsFile('Product-technisch-leerdoel/Tests/calculator.js')

# Stel je Cohere API-sleutel in
cohere_api_key = '7Qw4MRgR92E4sriEvoL5XKMxN00LpwLYuZYLzSQi'
co = cohere.Client(cohere_api_key)

# Definieer de prompt op basis van je input
prompt = f"""
Write an java class based on the following input: {js_content}
This input is an javascript class that defines a lot of functions.
Transform this functions to java functions with the same logic.

Use the following requirements for this functions:
- Create the class Calculator defines in the given input.
- Create one public function that calls all the other functions given in the input.
- Make all the other functions private.
- All the parameters are int values. 
- Make a main class in the same directory that calls the Calculator class.
- Don't make the main class in the Calculator class.
- So you makes two classes, the Calculator class and the Main class.
- Make logic in the main class that calls one of the functions in the Calculator class.
- Calls from the main class the public function in the Calculator class where logic is created that calls the function that is called from the main class.
- print in the main class the output given from the Calculator class in the console.

Don't use in the output any text that is not java code. I want an written file that only have java code and nothing else.
"""

# Maak de API-aanroep
response = co.generate(
    model='command-xlarge-nightly',  # of een ander geschikt model
    prompt=prompt,
    max_tokens=500
)

# Haal de gegenereerde code op
generated_code = response.generations[0].text.strip()

def write_output_files(java_code):
    os.makedirs('Product-technisch-leerdoel/Java_test/', exist_ok=True)
    # Write the generated Java code to separate files
    class_definitions = java_code.split('public class ')
    for class_def in class_definitions[1:]:
        class_name = class_def.split(' ')[0]
        class_content = f"public class {class_def}"
        file_path = os.path.join('Product-technisch-leerdoel/Java_test/', f"{class_name}.java")
        with open(file_path, 'w') as file:
            file.write(class_content)

write_output_files(generated_code)
def addImport(file_path, new_content):
    try:
        with open(file_path, 'r+') as file:
            content = file.read()
            content.replace('`', '')
            file.seek(0)
            file.write(new_content + content)
    except Exception as e:
        print(f"An error occured: {e}")

addImport('Product-technisch-leerdoel/Java_test/Calculator.java', 'import java.util.Random;\n\n')
def remove_characters_from_file(file_path, characters_to_remove):
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove the specific characters
        for char in characters_to_remove:
            content = content.replace(char, '')

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")

remove_characters_from_file('Product-technisch-leerdoel/Java_test/Main.java', '`')

print("De gegenereerde code is geschreven naar de map Java_test")

def readCalculatorJavaFile(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      content = file.read()
    return content
  except FileNotFoundError:
    return 'File not found.'
  except Exception as e:
    return str(e)

content = readCalculatorJavaFile('Product-technisch-leerdoel/Java_test/Calculator.java')
# Definieer de prompt op basis van je Calculator java class
prompt = f"""
Write a Java test using JUnit for the following class:
{content}
"""

# Maak de API-aanroep
response = co.generate(
    model='command-xlarge-nightly',  # of een ander geschikt model
    prompt=prompt,
    max_tokens=10000
)

# Haal de gegenereerde code op
generated_code = response.generations[0].text.strip()

# Write the generated code to a file
with open('Product-technisch-leerdoel/Java_test/CalculatorTest.java', 'w') as file:
    file.write(generated_code)

remove_characters_from_file('Product-technisch-leerdoel/Java_test/CalculatorTest.java', '`')
def remove_word_or_sentence(file_path, text_to_remove):
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove the specific word or sentence
        content = content.replace(text_to_remove, '')

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"'{text_to_remove}' removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
remove_word_or_sentence('Product-technisch-leerdoel/Java_test/CalculatorTest.java', 'java')
remove_word_or_sentence('Product-technisch-leerdoel/Java_test/CalculatorTest.java', 'Here is a Java test using JUnit for the Calculator class:')

