import pandas as pd
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}



nato_file = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = { row.letter:row.code for (index, row) in nato_file.iterrows()}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter your name: ").upper()
nato_list = [nato_dict[alphabet] for alphabet in name if alphabet != ' ']

print(nato_list)