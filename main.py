import argparse
import json
from utils import get_args, extract_from_all
from models.gpt_model import get_gpt_response, add_task_prompt, get_gpt_config




if __name__ == '__main__':
    args = get_args(argparse.ArgumentParser())

    # qa_pairs = extract_qa_pairs(args.xml_path)
    # print(qa_pairs)

    qa_pairs = extract_from_all(args.xml_path)
    # print(len(qa_pairs))
    # print(qa_pairs.head(6))

    # add_task_prompt([],qa_pairs.iloc[0])

    response = get_gpt_response(qa_pairs.iloc[0], [], get_gpt_config(reading_level=2), verbose=True)
    print(response)

    response = get_gpt_response(qa_pairs.iloc[0], [], get_gpt_config(reading_level=5), verbose=True)
    print(response)

    response = get_gpt_response(qa_pairs.iloc[0], [], get_gpt_config(reading_level=8), verbose=True)
    print(response)

    response = get_gpt_response(qa_pairs.iloc[0], [], get_gpt_config(reading_level=11), verbose=True)
    print(response)