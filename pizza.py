'''def make_pizza(size, 
               *toppings):
    Summarize the pizza we are about to make.
    print(f"\nMaking a {size}-inch pizza with the following toppings.")
    
    for topping in toppings:
        print(f"-{topping}")
make_pizza(2,'hello', 'world', 4)'''

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)