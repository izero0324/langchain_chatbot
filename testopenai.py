import json
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Read API key from secret file
f = open('langchain/secret.json')
data = json.load(f)
api_key = data["key"]
f.close()

# export key
os.environ["OPENAI_API_KEY"] = api_key

#initial openai model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
# simple chat function
print(llm.invoke("how can langsmith help with testing?"))


# chat with prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])


output_parser = StrOutputParser()
# pipeline
chain = prompt | llm | output_parser
print(chain.invoke({"input": "how can langsmith help with testing?"}))