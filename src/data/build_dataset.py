import itertools
import pandas as pd
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)

def build_dataset():
    df = pd.read_csv('data/external/IMDB_data.csv')
    return df

if __name__ == '__main__':
    build_dataset()