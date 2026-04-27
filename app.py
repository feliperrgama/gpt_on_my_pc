from openai.types.responses import response
from openai import OpenAI
import dotenv as denv
import os

denv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt do usuário:
print("O que você deseja saber sobre futebol?")
user_prompt = input("-> ")


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um pesquisador sênior de tudo sobre o futebol, com foco no contexto de seleções mundiais e copas do mundo"},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)
