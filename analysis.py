import argparse
from utils import get_args
import pandas as pd
import matplotlib.pyplot as plt

def main(args):
    new_df = {}

    for file in args.result_files:
        file_path = file['path']
        file_name = file['name']
        df = pd.read_csv(file_path)
        new_df[f"{file_name}_original"] = df['input_readability']
        new_df[f"{file_name}_converted"] = df['output_readability']

    new_df = pd.DataFrame.from_dict(new_df)
    
    plt.figure(figsize=(12,4))
    new_df.boxplot()
    plt.savefig(f"{args.output_directory}/boxplot.png")
    plt.show()

if __name__ == '__main__':
    args = get_args(argparse.ArgumentParser(), file='analysis_config.json')
    

    main(args)