from typing import Dict
import random
import math
import pandas as pd
class pokemon:
    dfevo = pd.read_csv("assets/spreadsheets/evo.csv")
    dfmons = pd.read_csv("assets/spreadsheets/pokemon data.csv")
    dfexp = pd.read_csv("assets/spreadsheets/exp chart.csv")
    def __init__(self, dex:int):
        dfevo = pd.read_csv("assets/spreadsheets/evo.csv")
        dfmons = pd.read_csv("assets/spreadsheets/pokemon data.csv")
        dfexp = pd.read_csv("assets/spreadsheets/exp chart.csv")
        self.name = dfmons["name"].str[dex]
        self.dex = dex
        self.hp = math.floor((2* hp +31 + random.randint(0,63))*level)/100+5
        self.attack = math.floor((2*attack+random.randint(0,63))*level/100+5)
        self.defense = math.floor((2*defense+random.randint(0,63))*level/100+5)
        self.spatk = math.floor((2*spatk+random.randint(0,63))*level/100+5)
        self.spdef = math.floor((2*spdef+random.randint(0,63))*level/100+5)
        self.speed = math.floor((2*speed+random.randint(0,63))*level/100+5)
        self.boosts = {"attack": 0, "defense":0, "spatk":0, "spdef":0, "speed" :0}
        self.level = level
        self.ability = ability 