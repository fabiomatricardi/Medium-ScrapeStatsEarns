from rich_dataframe import prettify
import pandas as pd
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
console.print("This is information", style="info")
console.print("[warning]The pod bay doors are locked[/warning]")
console.print("Something terrible happened!", style="danger")


panel = Panel(Text("Hello", justify="right"))
print(panel)
string1 = "Call of PSRA after MOC signature and permit ready"
string2 = "Call of [reverse]PSRA[/reverse] after MOC signature and permit ready"
string3 = "Call of [black on yellow]PSRA[/black on yellow] after MOC signature and permit ready"
string4 = "Call of [fabio]PSRA[/fabio] after MOC signature and [fabio]permit ready[/fabio]"
console.print(string1)
console.print(string2)
console.print(string3)
console.print(string4)

main_string = "Note that the file will download to your Terminal’s current folder, so you’ll want to cd to a different folder if you want it stored elsewhere. If you’re not sure what that means, check out our guide to managing files from the command line. The article mentions Linux, but the concepts are the same on macOS systems, and Windows systems running Bash."
query = "Where is the folder for the download?"

def highlight(main_string,query,style_tag):
    query_list = query.split(' ')
    main_list = main_string.split(' ')
    final_text = ''
    #console.print(main_list)
    for word in main_list:
        if word in query_list:
            final_text = final_text+f'[{style_tag}]'+word+f'[/{style_tag}]'+' '
        else:
            final_text = final_text+' '+word+' '
    #console.print(main_string)
    #console.print(query)
    #console.print(final_text)
    return final_text

a_text = "Large language models (LLMs) with instruction finetuning demonstrate superior generative capabilities. However, these models are resource intensive. To alleviate this issue, we explore distilling knowledge from instruction-tuned LLMs to much smaller ones. To this end, we carefully develop a large set of 2.58M instructions based on both existing and newly-generated instructions. In addition to being sizeable, we design our instructions to cover a broad set of topics to ensure. A thorough investigation of our instruction data demonstrate their diversity, and we generate responses for these instructions using gpt-3.5-turbo. We then exploit the instructions to tune a host of models, dubbed LaMini-LM, of varying sizes, both from the encoder-decoder as well as the decoder-only families. We evaluate our models both automatically (on 15 different NLP benchmarks) and manually. Results show that our proposed LaMini-LM are on par with competitive baselines while being nearly 10 times smaller in size."
a_query = "What is the from we size of LaMini models"

result = highlight(a_text,a_query,'pippo')
console.print(result)

# THIS SOLUTION IS THE BEST BUT I DON'T KNOW HOW TO USE IT WITH RICH!!!!!
########################################################################
# credit https://stackoverflow.com/questions/57251653/highlight-specific-words-in-a-sentence-in-python
from functools import reduce
from itertools import chain

text = 'left foot right foot left foot right. Feet in the day, feet at night.'
l1 = ['right','night']

print(reduce(lambda t, x: t.replace(*x), chain([text.lower()], ((t, colored(t,'white','on_red')) for t in l1)))) 




"""
speed_dating = pd.read_csv('Medium_4earn_2023-05-12at1716.csv')


table = prettify(speed_dating)

"""