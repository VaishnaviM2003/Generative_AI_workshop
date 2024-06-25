from langchain.prompts import PromptTemplate

# Simple prompt with placeholders
prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)

# Filling placeholders to create a prompt
filled_prompt = prompt_template.format(adjective="funny", content="robots")
print(filled_prompt)