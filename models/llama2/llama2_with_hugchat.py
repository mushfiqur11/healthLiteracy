import argparse
from hugchat import hugchat
from hugchat.login import Login

parser = argparse.ArgumentParser()
parser.add_argument('--email', type=str, default='', help='type your huggingface email or userid')
parser.add_argument('--password', type=str, default='', help='type your huggingface password')
parser.add_argument('--prompt', type=str, default='Who are you and who built you?', help='type your huggingface password')
args = parser.parse_args()

if __name__ == "__main__":

    # Log in to huggingface and grant authorization to huggingchat
    sign = Login(email=args.email, passwd=args.password)
    cookies = sign.login()

    # Save cookies to the local directory
    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)

    # Load cookies when you restart your program:
    # sign = login(email, None)
    # cookies = sign.loadCookiesFromDir(cookie_path_dir) # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.


    # Create a ChatBot 
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) # or cookie_path="usercookies/<email>.json"
    print(chatbot.chat(args.prompt))

    # Create a new conversation
    # id = chatbot.new_conversation()
    # chatbot.change_conversation(id)