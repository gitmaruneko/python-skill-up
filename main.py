import numpy as np

import pandas as pd

numbers = np.array([10, 20, 30, 40, 50])

df = pd.DataFrame({

    "numbers": numbers

})

print(df)

print("Mean:", df["numbers"].mean())
