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
    qa_pairs = extract_from_all(args.xml_path)
    results = []

    for i in trange(len(qa_pairs)):
        sentence = f"Question: {qa_pairs.iloc[i]['answer']}, Answer: {qa_pairs.iloc[i]['question']}"

        if combined_readability(sentence) is None:
            continue

        response = get_gpt_response(sentence, [], get_gpt_config(reading_level=args.reading_level), verbose=args.verbose)
        if combined_readability(response) is None:
            continue

        results.append({
            "input": sentence,
            "input_readability": combined_readability(sentence, verbose=args.verbose),
            "output": response,
            "output_readability": combined_readability(response, verbose=args.verbose)
        })

    results = pd.DataFrame.from_records(results)
    results.to_csv(args.output, index=False)


if __name__ == '__main__':
    args = get_args(argparse.ArgumentParser())

    main(args)
