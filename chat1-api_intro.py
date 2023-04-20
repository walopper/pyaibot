import openai
import config

openai.api_key = config.api_key
model_engine =  config.model_engine

content =  input('Prompt >>> ')

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{ "role": "user", "content": content }])

# print(response)
print(response.choices[0].message.content)
