import argparse
from utils import get_args
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

def main(args):
    new_df = {}

    for file in tqdm(args.result_files):
        file_path = file['path']
        file_name = file['name']
        df = pd.read_csv(file_path)
        for col in df.columns:
            if 'readability' not in col:
                continue
            new_df[f"{file_name}_{col}"] = df[col]  

    new_df = pd.DataFrame.from_dict(new_df)
    
    plt.figure(figsize=(12,4))
    new_df.boxplot()
    plt.savefig(f"{args.output_directory}/boxplot.png")
    plt.show()

if __name__ == '__main__':
    args = get_args(argparse.ArgumentParser(), file='analysis_cmsd_config.json')
    

    main(args)