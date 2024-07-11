import os
import torch
from datasets import load_dataset
import pandas as pd

def import_dataset():
    IMDB_dataset = load_dataset('IMDB', split='train[0:1000]')
    IMDB_dataset = IMDB_dataset.shuffle()

    #df = pd.DataFrame(IMDB_dataset)
    print(IMDB_dataset['text'][0])
    return IMDB_dataset

    # folder_path = 'data/external'
    # IMDB_dataset_export = os.path.join(folder_path, 'IMDB_data.csv')
    # df.to_csv(IMDB_dataset_export, index=False)
    
    # print(f"Data exported to {IMDB_dataset_export}")

if __name__ == '__main__':
    import_dataset()