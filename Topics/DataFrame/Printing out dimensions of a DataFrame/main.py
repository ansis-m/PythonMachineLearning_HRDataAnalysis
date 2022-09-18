import pandas as pd

pets = {
    'species': ['cat', 'dog', 'parrot', 'cockroach'],
    'name': ['Dr. Mittens Lamar', 'Diesel', 'Peach', 'Richard'],
    'legs': [4, 4, 2, 6],
    'wings': [0, 0, 2, 4],
    'looking_for_home': ['no', 'no', 'no', 'yes']
}
df = pd.DataFrame(pets)
print(df.head())
