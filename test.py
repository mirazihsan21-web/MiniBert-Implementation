import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
d6 = pd.DataFrame(
    {
        ( 'birthyear'): {('Paris', 'alice'):1985, ('Paris', 'bob'):1984, ('London', 'charles'): 1992},
        ('hobby'): {('Paris', 'alice'):'Biking', ('Paris', 'bob'):'Dancing'},
        ( 'weight'): {('Paris', 'alice'):68, ('Paris', 'bob'):83, ('London', 'charles'): 112},
        ( 'children'): {('Paris', 'alice'):np.nan, ('Paris', 'bob'):3, ('London', 'charles'): 0},
    }
)
print(d6)
