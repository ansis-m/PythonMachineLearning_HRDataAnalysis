import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})

df['c'] = [3, 6]
new_row = {'a' : 7, 'b' : 8, 'c' : 9}
df = pd.concat([df, pd.DataFrame.from_records([new_row])], ignore_index=True)
