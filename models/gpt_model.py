import openai
import json

def get_api_key():
    gpt_gpt_config = get_gpt_config()
    with open(gpt_gpt_config["key_path"], "r") as f:
        api_key = f.read()
    return api_key

def get_gpt_config(path = "gpt_config.json", reading_level = 6):
    with open(path, "r") as f:
        gpt_config = json.load(f)
    gpt_config["prompt"] = gpt_config[f"prompt{reading_level}"]
    return gpt_config

def create_gpt_messages(samples=False, input_limit=10):
    """
    This function creates the gpt message for the given seq_in, seq_out and intent
    """
    messages = []
    # raise NotImplementedError
    return messages

def formulate_gpt_prompt(messages, gpt_config):
    """
    This function formulates the gpt prompt for the given messages
    """
    base_prompt = gpt_config["prompt"]
    prompt = []
    prompt.append({"role": "system", "content": base_prompt})
    for message in messages:
        prompt.append(message)
    return prompt

def add_task_prompt(messages, task_prompt):
    """
    This function adds the task sentence to the messages list
    """
    # content = ''
    # question, answer = task_prompt
    # content += f"Question: {question}\n"
    # content += f"Answer: {answer}\n"
    messages.append({"role": "user", "content": task_prompt})
    return messages

def get_gpt_response(user_message, samples, gpt_config, input_limit=10, verbose=False):
    """
    This function returns the gpt response for the given prompt
    """
    messages = create_gpt_messages(samples, input_limit=input_limit)
    messages = formulate_gpt_prompt(messages, gpt_config)
    messages = add_task_prompt(messages, user_message)

    openai.api_key = get_api_key()

    if verbose:
        print(messages)

    response = openai.ChatCompletion.create(
        model=gpt_config["model"],
        messages=messages
    )
    return response.choices[0].message.content