from rich_dataframe import prettify
import pandas as pd

speed_dating = pd.read_csv('Medium_4earn_2023-05-12at1716.csv')


table = prettify(speed_dating)