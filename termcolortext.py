from termcolor import colored
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.theme import Theme
from termcolor import colored

custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "fabio" : "black on bright_yellow",
    "pippo" : "bold red underline on white"
})
console = Console(theme=custom_theme)

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
style_tag = 'pippo'

text = 'left foot right foot left foot right. Feet in the day, feet at night.'
l1 = ['right','night']
renderable = reduce(lambda t, x: t.replace(*x), chain([text.lower()], ((t, f'[{style_tag}] {t} [/{style_tag}]') for t in l1)))
console.print(renderable)

"""
print(reduce(lambda t, x: t.replace(*x), chain([text.lower()], ((t, colored(t,'white','on_red')) for t in l1)))) 
"""
