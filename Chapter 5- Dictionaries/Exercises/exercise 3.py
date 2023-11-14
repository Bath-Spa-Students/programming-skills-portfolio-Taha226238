# Initial glossary
programming_glossary = {
    'variable': 'A named storage location in a program that can hold the data or values.',
    'function': 'A reusable block of code that performs  specific task.',
    'loop': 'A control structure that allows a set of instructions that can be executed repeatedly.',
    'list': 'An ordered collection of items, which is of different types.',
    'conditional statement': 'A statement that performs different actions depending on whether a condition is True or False.'
}

# Add more terms to the glossary
programming_glossary['dictionary'] = 'A data structure stores key-value pairs.'
programming_glossary['module'] = 'A file containing Python code, typically  reusability.'
programming_glossary['syntax'] = 'The set of rules that dictate  combinations of symbols and keywords in a programming language.'
programming_glossary['iteration'] = 'The process of repeatedly executing a block of code.'
programming_glossary['algorithm'] = 'A step-by-step procedure for solving a problem in a finite number of steps.'

# Loop through the glossary and print each word and its meaning
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")

