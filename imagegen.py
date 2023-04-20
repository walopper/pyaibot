import openai
import config

openai.api_key = config.api_key

def imageFromPromp(prompt: str):
    result = openai.Image.create(
        prompt=prompt,
        n=4,
        size="1024x1024"
    )

    return result.data


def mapUrl(item):
    return item.url


prompt = input("Enter images generation prompt >>> ")

response = imageFromPromp(prompt)

print(response)