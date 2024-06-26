from langchain_community.llms import Cohere

llm = Cohere(cohere_api_key="nIIrvF6h3kEiARdGQQRG9OC0SHoqTAWGyuKqvD14")
print(llm.invoke("List the seven wonders of the world."))

