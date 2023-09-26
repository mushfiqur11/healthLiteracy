# RUN "huggingface-cli login" in Command Prompt
# Needs GPU

from transformers import AutoTokenizer
from transformers import pipeline
import transformers
import argparse
import torch

parser.add_argument('--prompt', type=str, default='Write me a paragraph with at least 100 words on colorectal cancer that has a readability level of 6th grade.\n', help='type your huggingface password')
parser.add_argument('--token_size', type=str, default='7B', help='type your huggingface password')

def get_llama_response(prompt: str) -> None:
    """
    Generate a response from the Llama model.

    Parameters:
        prompt (str): The user's input/question for the model.

    Returns:
        None: Prints the model's response.
    """

    sequences = llama_pipeline(
        prompt,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=256,
    )

    print("Chatbot:", sequences[0]['generated_text'])

if __name__ == "__main__":

    model = f"meta-llama/Llama-2-{args.token_size}-chat-hf" # meta-llama/Llama-2-7b-hf

    tokenizer = AutoTokenizer.from_pretrained(model, use_auth_token=True)

    llama_pipeline = pipeline(
        "text-generation",  # LLM task
        model=model,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    prompt = args.prompt
    response = get_llama_response(prompt)
    print(response)