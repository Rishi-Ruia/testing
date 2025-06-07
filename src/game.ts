class Game {
    protected static names: string[];
    protected static type1: string[];
    protected static type2: string[];
    protected static atk: number[];
    protected static def: number[];
    protected static spd: number[];
    protected static spatk: number[]; 
    protected static spdef: number[];
    protected static hp: number[];
    protected static pokedexNum: number[]; 
    protected static baseStatTotal: number[];
    public static poke: Pokemon[] = Pokemon[1025]; // may or may not use this
    protected static GUI: GUI;
    protected static user: Player;
    protected static bot: Bot;
    protected static volume;

    // Initializes the game
    static init(): void {

    }

    // Creates Pokemon objects for both players
    static createPokemonObjects(): void {

    }

    // Pokemon "attacker" attacks Pokemon "attacked" with Move "attack" and returns a string that
    // summarizes the attack
    static attack(attacker: Pokemon, attack: Move, attacked: Pokemon, special: boolean): string {
        return ""
    }

    // Helper method to calculate the amount of damage a move will do to a pokemon
    static damageCalc(attacker: Pokemon: attack: Move, attacked: Pokemon, 
        special: boolean, random: number): number {
        return 0
    }

    static mute(): void {

    }
}