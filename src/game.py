from pokemon import Pokemon, Move
from random import randint, random
from typing import Tuple

# Creates Pokemon objects for both players
def create_pokemon_objects() -> None:
    pass

# Pokemon "attacker" attacks Pokemon "victim" with Move "move" and returns a string that summarizes the attack
def attack(attacker: Pokemon, move: Move, victim: Pokemon, special: bool) -> str:
    if move.name == "Recover":
        heal = (int) (attacker.max_hp * 0.5)
        attacker.hp = max([attacker.max_hp, attacker.hp + heal])
        return f"{attacker.name} used Recover and now has {attacker.hp} HP!"

    effectiveness: str = determine_effectiveness(move, victim)

    damage_mod, crit_message = get_damage_mod(attacker, move)
    
    random: float = damage_mod * (random() * 0.15 + 0.85)
    damage: int = damage_calc(attacker, move, victim, special, random)
    if randint(1, 100) <= move.accuracy:
        victim.hp = max([0, victim.hp - damage])
        if victim.hp == 0:
            return f"{attacker.name} used {move.name} and {victim.name} fainted! {crit_message}"
        else:
            return f"{attacker.name} used {move.name}, {effectiveness} It did {damage * 100 / victim.max_hp}%. {crit_message}"
    else:
        return f"{move.name} missed!"
    
def determine_effectiveness(move: Move, victim: Pokemon) -> str:
    if Move.effective(move, victim) >= 2:
        effectiveness = "it was SUPER EFFECTIVE!"
    elif Move.effective(move, victim) <= 0.5:
        effectiveness = "it was not very effective."
    elif Move.effective(move, victim) == 0:
        effectiveness = f"{victim.name} was immune."

    return effectiveness

def get_damage_mod(attacker: Pokemon, move: Move,) -> Tuple[float, str]:
    damage_mod: float = 1.0
    crit_message: str = ""
    # add STAB to damage modification
    if attacker.type1 == move.type or attacker.type2 == move.type:
        damage_mod = 1.5
    # 1 in 24 chance of having a critical hit
    if randint(1, 24) == 1:
        damage_mod *= 1.5
        crit_message = "It was a critical hit!"

    return damage_mod, crit_message

# Helper method to calculate the amount of damage a move will do to a pokemon
def damage_calc(attacker: Pokemon, move: Move, victim: Pokemon, special: bool, random: float) -> int:
    if not special:
        return (int) ((((((((2 * attacker.level) / 5) + 2) * attacker.atk * move.power) / victim.defense) / 50) + 2) * Move.effective(move, victim) * random)
    else:
        return (int) ((((((((2 * attacker.level) / 5) + 2) * attacker.spatk * move.power) / victim.spdef) / 50) + 2) * Move.effective(move, victim) * random) 