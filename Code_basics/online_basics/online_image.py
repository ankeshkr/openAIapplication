from openai import OpenAI
from apikey import apikey
import os
from PIL import Image
from io import BytesIO
import requests

os.environ['OPENAI_API_KEY'] = apikey
OpenAI.api_key = apikey

client = OpenAI()
prompt = "a cute cat jumping over a fence, cartoon, caolorful"

print("generating image...")
response = client.images.generate(
    model = "dall-e-3",
    prompt=prompt,
    size=1024*1024,
    n=1
)

print(response)
image_url = response.data[0].url
image = requests.get(image_url)
image = Image.open(BytesIO(image.content))
image.show()
image.save("generated_image.png")