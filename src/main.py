import os
import argparse
import sys
import absl.logging

sys.dont_write_bytecode = True
absl.logging.set_verbosity(absl.logging.ERROR)

#setup global dataframe variable

df = build_dataset()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true')
    
    args = parser.parse_args()

if __name__ == '__main__':
    main()