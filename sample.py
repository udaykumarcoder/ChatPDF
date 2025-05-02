import google.generativeai as genai

genai.configure(api_key="AIzaSyBhe8YR9d8ir0Mz0CY2EdpNOvsv_TtJkII")
models = genai.list_models()

for model in models:
    print(model.name)
