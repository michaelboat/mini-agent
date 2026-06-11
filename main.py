import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
    # load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("API could not be accessed")
    
    # create instance of gemini client
    client = genai.Client(api_key=api_key)
    
    # get user input
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    args = parser.parse_args()
    
    # send prompt and get response object from gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt
    )
    # print the response
    if not response:
        raise ValueError("FAILED API Request")
    
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:\n", response.text)
    
    
    
    
if __name__ == "__main__":
    main()

