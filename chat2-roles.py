import openai
import config

openai.api_key = config.api_key
model_engine =  config.model_engine

messages = [{ "role": "system", "content": "You are a very helpful assistant expert in ErLang" }]

content =  input('>>> ')

messages.append({ "role": "user", "content": content })

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages)

print(response.choices[0].message.content)