# Vocabularly learner

import numpy as np
import pandas as pd
import yaml


filename = 'words.txt'
words = pd.read_csv(filename, header=0, sep='\t')
n_words = len(words)
print(f"Dictionary with {n_words} words loaded.")

done = False
while not done:
    i = np.random.randint(0, n_words)
    word = words.loc[i, 'English']
    resp = input(f"\nWhat is the French for '{word}'?")
    print(words.loc[i, 'French'])
    resp = input(f"Press return to continue or 'q' to quit: ")
    if resp.lower() == 'q':
        break
