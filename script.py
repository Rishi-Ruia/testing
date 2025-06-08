import pandas as pd

# Load the full Pokémon species info
poke_df = pd.read_csv("pokemon.csv")
moves_df = pd.read_csv("final_pokemon_moves.csv")

# Step 1: Filter base forms from pokemon.csv
base_forms = poke_df[poke_df["form"].isnull() | (poke_df["form"].str.strip() == "")]
base_forms = base_forms.reset_index(drop=True)

# Create a mapping: lowercase name → new Dex number based on row order
base_forms["name_clean"] = base_forms["name"].str.lower()
name_to_new_dex = {name: i + 1 for i, name in enumerate(base_forms["name_clean"])}

# Step 2: Filter moves_df to only include base forms
moves_df["name_clean"] = moves_df["Pokemon"].str.lower()
filtered_moves = moves_df[moves_df["name_clean"].isin(name_to_new_dex.keys())].copy()

# Step 3: Assign new Dex numbers
filtered_moves["Dex"] = filtered_moves["name_clean"].map(name_to_new_dex)

# Step 4: Sort by Dex and save
final_df = filtered_moves.sort_values(by="Dex")
final_df = final_df.drop(columns=["name_clean"])
final_df.to_csv("final_pokemon_moves_cleaned.csv", index=False)

print("✅ Cleaned file saved as final_pokemon_moves_cleaned.csv")
