import os
import argparse
from openai import OpenAI

client = OpenAI(api_key="")

parser = argparse.ArgumentParser(description="Chat with OpenAI GPT model")
parser.add_argument('-p', '--prompt', type=str, required=True, help="The prompt to send to the GPT model")

args = parser.parse_args()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Linux terminal assistant. Your responses should be concise one-liners that can be directly pasted into the terminal, without any comments or additional text."},
        {"role": "user", "content": args.prompt},
    ]
)

print(completion.choices[0].message.content.strip())
