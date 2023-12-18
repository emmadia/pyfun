def generate_greeting_code(language):
    """
    Generate a simple greeting code based on the user's preferred programming language.

    Parameters:
    - language (str): The preferred programming language.

    Returns:
    - str: Greeting code snippet.
    """
    language_lower = language.lower()

    if language_lower == 'ruby':
        return """puts 'Hello, Ruby!'\n"""
    elif language_lower == 'python':
        return """print('Hello, Python!')\n"""
    elif language_lower == 'java':
        return """public class Greeting {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello, Java!");\n\t}\n}\n"""
    elif language_lower == 'javascript':
        return """console.log('Hello, JavaScript!');\n"""
    elif language_lower == 'go':
        return """package main\n\nimport "fmt"\n\nfunc main() {\n\tfmt.Println("Hello, Go!")\n}\n"""
    elif language_lower == 'php':
        return """<?php\n\techo 'Hello, PHP!';\n?>\n"""
    elif language_lower == 'c':
        return """#include <stdio.h>\n\nint main() {\n\tprintf("Hello, C!\\n");\n\treturn 0;\n}\n"""
    elif language_lower == 'c++':
        return """#include <iostream>\n\nint main() {\n\tstd::cout << "Hello, C++!\\n";\n\treturn 0;\n}\n"""
    else:
        return "Sorry, I don't have a greeting for that language."

if __name__ == "__main__":
    preferred_language = input("Enter your preferred programming language: ")
    greeting_code = generate_greeting_code(preferred_language)
    
    print("\nHere's a simple greeting code snippet for you:\n")
    print(greeting_code)
