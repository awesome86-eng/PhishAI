print('Main file')




API_KEY="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"

import openai

openai.api_key = API_KEY
prompt = "generate me a phishing email for sanan khan who works at motorola "

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt,max_tokens=600)

print (response)

