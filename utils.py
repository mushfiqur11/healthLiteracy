import json
from bs4 import BeautifulSoup
from argparse import Namespace
from glob import glob
import pandas as pd

import xml.etree.ElementTree as ET

def read_config():
    """Reads the config file and returns a dictionary."""
    config = {}
    with open("config.json", "r") as f:
        config = json.load(f)
    return config

def get_args(args):
    """Returns a dictionary of arguments."""
    config = read_config()
    args.add_argument('--xml_path', type=str, default=config['xml_path'])
    args.add_argument('--age', type=int, default=config['age'])

    args = args.parse_args()
    for arg in vars(args):
        config[arg] = getattr(args, arg)
    return Namespace(**config)
    # return args

def extract_qa_pairs(xml_path):
    """
    Reads and parses the XML file to extract the questions and answers.
    """
    qa = []
    with open(xml_path, "r", encoding="utf8") as f:
        # print(f.read())
        root = ET.fromstring(f.read())

        # Find all QAPair elements
        qa_pairs = root.findall(".//QAPair")

        # Loop through QAPairs and extract questions and answers
        for qa_pair in qa_pairs:
            try:
                question = qa_pair.find("Question").text.strip()
                answer = qa_pair.find("Answer").text.strip()
                qa.append({"question": question, "answer": answer})
            except:
                pass
    return qa

def extract_from_all(root_path):
    """
    Extracts the questions and answers from all XML files in the given path.
    """
    qa_pairs = []
    for xml_path in glob(root_path + "/*.xml"):
        qa_pairs += extract_qa_pairs(xml_path)
    return pd.DataFrame(qa_pairs)