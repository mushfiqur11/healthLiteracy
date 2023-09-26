import argparse
import json
from utils import get_args, extract_from_all
from models.gpt_model import get_gpt_response, add_task_prompt, get_gpt_config
from metrics import combined_readability
import numpy as np
import pandas as pd
from tqdm import tqdm, trange


def main(args):
    print(args)
    df = pd.read_csv(args.csv_path)

    results = []

    batch_size = 10
    for i in trange(0,len(df),batch_size):
        sentences = {}
        for col in args.columns:
            sent = ".".join(df.iloc[i:i+batch_size][col])
            readability = combined_readability(sent)
            if readability is None:
                continue
            sentences[col] = sent
            sentences[f"{col}_readability"] = readability
        results.append(sentences)

    results = pd.DataFrame.from_records(results)
    results.to_csv(args.output, index=False)


if __name__ == '__main__':
    args = get_args(argparse.ArgumentParser(), file='cmsd_temp_config.json')

    main(args)
