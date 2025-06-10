from typing import List
from pokemon import Pokemon, Move
from player import Player
from random import randint
import game

class Bot(Player):
    def __init__(self) -> None:
        super().__init__()
        
    # Makes the bot do its move and returns a summary of the move. Also makes the bot switch if its current pokemon has fainted.
    def bot_turn(self, player_mon: Pokemon, move: Move) -> str:
        move_result: str = game.attack(self.current, move, player_mon, move.is_special)
        if "healed" in move_result:
            return f"{self.current.name} healed!"
        if self.current.hp == 0:
            # Disable the bot's moves
            pass

        return move_result
    
    # Forces the bot to switch in the event that its current pokemon faints or there is an ability that forces the bot to switch.
    def auto_switch(self):
        for i in range(len(self.mons)):
            if (self.mons[i] != self.current) and (self.mons[i].hp != 0):
                self.switch(i)