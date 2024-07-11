import os
import argparse
import sys
import absl.logging

from models.tokenize_data import tokenize_data
from data.build_dataset import build_dataset
from data.import_dataset import import_dataset

sys.dont_write_bytecode = True
absl.logging.set_verbosity(absl.logging.ERROR)

#setup global dataframe variable


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--verbose', action='store_true')
    
    # args = parser.parse_args()
    dataset = import_dataset()
    tokenize_data(dataset)

if __name__ == '__main__':
    main()