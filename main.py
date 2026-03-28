import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.available_functions import available_functions
from functions.call_function import call_function
from system_prompt import system_prompt


def generate_content(client, messages):
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )


def main():
    # import .env variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # get CLI args
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # create the client and initialize response history
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response_list = []

    # prompt loop
    for _ in range(20):
        # pass prompt to the model
        response = generate_content(client, messages)

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        # output
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls:
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, True)
                if not function_call_result.parts:
                    raise Exception("Error: Function call result error.")
                if function_call_result.parts[0].function_response.response == None:
                    raise Exception("Error: Function call result error.")
                response_list.append(function_call_result.parts[0])
                if args.verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}"
                    )
        else:
            print(response.text)
            exit(0)

        messages.append(types.Content(role="user", parts=response_list))

    # if we hit max iterations
    exit(1)


if __name__ == "__main__":
    main()
