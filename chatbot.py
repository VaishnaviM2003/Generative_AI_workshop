import streamlit as st
import os
from langchain.chains import LLMChain
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from trulens_eval import TruChain, Feedback, Huggingface, Tru

hugs = Huggingface()
tru = Tru()

# Load environment variables from .streamlit/secrets.toml
COHERE_API_KEY = os.environ['COHERE_API_KEY'] = "tFKVM9lLvDa3dUwXmBp4XHr8KoS7ylxSoecgMhm0"
HUGGINGFACE_API_KEY = os.environ["HUGGINGFACE_API_KEY"] = "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"

template = """You are a chatbot having a conversation with a human.
        {chat_history}
        Human: {human_input}
        Chatbot:"""
prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")
llm = ChatCohere(cohere_api_key=COHERE_API_KEY)
chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)

# Ensure extend_existing=True is set for TruChain if it defines trulens_apps table
chain_recorder = TruChain(chain, extend_existing=True)

st.title("Contextual Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Record with TruLens
        with chain_recorder as recording:
            full_response = chain.run(prompt)
        message_placeholder = st.empty()
        message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response})

tru.run_dashboard()
