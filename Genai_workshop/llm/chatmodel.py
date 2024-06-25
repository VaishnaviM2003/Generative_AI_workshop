from langchain_community.llms import Cohere
from langchain.schema.messages import HumanMessage, SystemMessage

# Initialize Cohere with your API key
chat = Cohere(cohere_api_key="nIIrvF6h3kEiARdGQQRG9OC0SHoqTAWGyuKqvD14")
messages = [
    SystemMessage(content="You are Michael Jordan."),
    HumanMessage(content="Which shoe manufacturer are you associated with?"),
]

response = chat.invoke(messages)
print(response)
print(response)  


