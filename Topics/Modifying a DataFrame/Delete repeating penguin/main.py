# your code here. The dataset is already loaded, the variable that contains the DataFrame is called penguins_example
import numpy as np

penguins_example.drop(index=6, inplace=True)
penguins_example.index = np.arange(1, len(penguins_example) + 1)

print(penguins_example)
