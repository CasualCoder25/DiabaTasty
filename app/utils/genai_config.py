import os
import google.generativeai as genai

if os.getenv("GOOGLE_API_KEY") is not None:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
else:
    from app.local_secrets import GOOGLE_API_KEY
    genai.configure(api_key=GOOGLE_API_KEY)

if os.getenv("model_name") is not None:
    model = genai.GenerativeModel(model_name=f'tunedModels/{os.getenv("model_name")}')
else:
    from app.local_secrets import model_name
    model = genai.GenerativeModel(model_name=f'tunedModels/{model_name}')

