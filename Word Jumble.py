import random

tech_brands = ["HP", "Dell", "Acer", "Lenovo", "Toshiba", "Apple", "Asus", "Sony", "Samsung", "Sharp", "Vizio", "Gateway", "Nokia", "HTC", "Philips"]

selection = random.choice(tech_brands)
answer = selection

jumble = list(selection)

for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,

guess = raw_input("\nWhat kind of brand is jumbled?")
guess = guess.upper()

if guess == answer:
    print("Correct")
else:
    print(answer)
