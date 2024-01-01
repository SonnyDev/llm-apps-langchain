import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

model = ChatOpenAI(model="gpt-4", temperature=0.0)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Tu es un historien renommé qui donne des réponses correctes et éloquantes aux questions d'histoire.",
        ),
        ("human", "{question}"),
    ]
)
runnable = prompt | model | StrOutputParser()

for chunk in runnable.stream({"question": "Qu'est-ce que la revolution francaise"}):
    print(chunk, end="", flush=True)
