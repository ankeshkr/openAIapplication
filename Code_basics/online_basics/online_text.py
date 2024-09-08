from openai import OpenAI
from apikey import apikey
import os

os.environ['OPENAI_API_KEY'] = apikey
OpenAI.api_key = apikey

client = OpenAI()
prompt = "which city is the largest in the world"

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[{"role":"user", "content":prompt}]
)

print(response)