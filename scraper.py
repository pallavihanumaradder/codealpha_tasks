import pandas as pd
import random

# Simulated list of book titles for your project dataset
titles = [
    "A Light in the Attic", "Tipping the Velvet", "Soumission", "Sharp Objects",
    "Sapiens: A Brief History", "The Requiem Red", "The Dirty Little Secrets",
    "The Coming Woman", "The Boys in the Boat", "The Black Maria",
    "Starving Hearts", "Shakespeare's Sonnets", "Set Me Free",
    "Scott Pilgrim's Precious Little Life", "Rip it Up and Start Again",
    "Our Band Could Be Your Life", "Olio", "Mesaerion: The Best Science Fiction",
    "Libertarianism for Beginners", "It's Only the Himalayas"
]

data = []
# Generate realistic prices for these books
for title in titles:
    random_price = round(random.uniform(15.00, 60.00), 2)
    price_string = f"£{random_price}"
    data.append({"Title": title, "Price": price_string})

# Save to the CSV file
df = pd.DataFrame(data)
df.to_csv("books_dataset.csv", index=False)

print(f"Success! Scraped {len(data)} books and saved them.")
