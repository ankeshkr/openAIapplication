from openai import OpenAI
from apikey import apikey
import os

os.environ['OPENAI_API_KEY'] = apikey
OpenAI.api_key = apikey

client = OpenAI()
audio_file = open("../../resources/test.mp3", "rb")

print("transcribing audio...")
response = client.audio.transcriptions.create(
    model = "whisper-1",
    file=audio_file,
    response_format="text"
)
print(response)