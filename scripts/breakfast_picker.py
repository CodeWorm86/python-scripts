# This is a breakfast program
# Written by: CodeWorm86
# Date: 8-15-2025

print("-----------------------")
print("American Breakfast Picker")
print("-----------------------")


print("Please choose a number between 0-3")
classic_usa = input()

classic_american = [
    "scrambled eggs",
    "bacon",
    "buttered toast",
    "orange juice",
]

if classic_usa == "0":
    print("You have ordered", classic_american[0])
elif classic_usa == "1":
    print("You have ordered", classic_american[1])
elif classic_usa == "2":
    print("You have ordered", classic_american[2])
elif classic_usa == "3":
    print("You have ordered", classic_american[3])
else:
    print("That is NOT a breakfast option")
