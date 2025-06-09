from typing import List
from pokemon import Pokemon, Move
from player import Player
from random import randint

class Bot(Player):
    def __init__(self) -> None:
        super().__init__()