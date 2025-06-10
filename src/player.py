from typing import List
from pokemon import Pokemon
from random import randint

class Player:
    def __init__(self) -> None:
        self.mons: List = []
        self.current: Pokemon = self.mons[0]
    
    # Switches the current Pokemon the player is using for the pokemon at index i and returns a string that summarizes the switch
    def switch(self, i: int) -> str:
        if self.mons[i].hp == 0:
            return None
        if self.mons[i] == self.current:
            return None
        
        prev_name = self.current.name
        self.current = self.mons[i]
        return f"{prev_name} switched out and {self.current.name} switched in!"
    
    # Checks if the player has lost
    def has_lost(self) -> bool:
        for pokemon in self.mons:
            if pokemon.hp != 0:
                return False
        
        return True
    
    # Gets pokemon at index i
    def get_pokemon(self, i: int) -> Pokemon:
        return self.mons[i]
