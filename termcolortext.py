from termcolor import colored
text='left foot right foot left foot right. Feet in the day, feet at night.'
l1=['night','right']
result = " ".join(colored(t,'white','on_red') if t in l1 else t for t in text.lower().split())
print(result)

from termcolor import colored
text='left foot right foot left foot right. Feet in the day, feet at night.'
l1=['right','night']
formattedText = []
for t in text.lower().split():
    if t in l1:
        formattedText.append(colored(t,'white','on_red'))
    else: 
        formattedText.append(t)

print(" ".join(formattedText))

from functools import reduce
from itertools import chain

text = 'left foot right foot left foot right. Feet in the day, feet at night.'
l1 = ['right','night']

print(reduce(lambda t, x: t.replace(*x), chain([text.lower()], ((t, colored(t,'white','on_red')) for t in l1)))) 