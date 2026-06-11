import os
from dotenv import load_dotenv
from google import genai


def main():
    # load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("API could not be accessed")
    
    # create instance of gemini client
    client = genai.Client(api_key=api_key)
    
    # send prompt and get response object from gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="How many days of rains does NYC get during the summer?" # hardcoded
    )
    # print the response
    print(response.text)
    
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
