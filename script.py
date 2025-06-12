import pandas as pd
import requests
import csv
# # 1) Load your spreadsheet
# dfevo = pd.read_csv("assets/spreadsheets/evo.csv")
# dfmons = pd.read_csv("assets/spreadsheets/pokemon data.csv")
# local_names = set(dfevo["Pokemon"].str.lower().unique())
# other = set(dfmons["name"].str.lower().unique())
# # 2) Fetch the full list of species via HTTP

# # 3) Compute the difference
# missing = sorted(other - local_names)
# print("Missing Pokémon:", missing)


# 1) Load your spreadsheet

df = pd.read_csv("n.csv")
print("dad")
# with open("n.csv", "w", encoding="utf-8") as f:
#     for i in range(1010):
#         line = (
#             str(df["Dex"][i]) + "," +
#             str(df["Pokemon"][i]) + "," +
#             "\"" + str(df["Moves"][i]).replace("-", "") + "\"" + "," +
#             "\"" + str(df["Levels"][i]) + "\""
#         )
#         f.write(line + "\n")

# dfevo = pd.read_csv("assets/spreadsheets/evo.csv")
# dfmons = pd.read_csv("assets/spreadsheets/pokemon data.csv")
# local_names = list(dfevo["Pokemon"].str.lower())
# other_names = list(dfmons["name"].str.lower().unique())
# right_num = list(dfmons["dex"].unique())
# wrong_num = list(dfevo["#"].unique())
# # 2) Fetch the full list of species via HTTP
# order = list()
# # 3) Compute the difference
# for i in local_names:
#     index = other_names.index(i)+1
#     order.append(index)
# print(order)
# mons = list( dfevo["Pokemon"].str.lower())
# s = set()
# for mon in mons:
#     if mon in s:
#         print(mon)
#     s.add(mon)
