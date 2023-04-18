import openai
import config

openai.api_key = config.api_key
model_engine =  config.model_engine

messages = [{ "role": "system", "content": "You are a GoLang expert developer" }]

while True:
    content =  input('>>> ')

    if content == 'exit':
        break

    messages.append({ "role": "user", "content": content })

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages)
    
    messages.append({ "role": "assistant", "content": response })

    print(response.choices[0].message.content)