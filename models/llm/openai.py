from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


class ChatModel:
    def __init__(self, model_name: str, api_key: str):
        self.chat_model = ChatOpenAI(model=model_name,  api_key=api_key)

    def chat(self, system_prompt: str, human_message: str) -> AIMessage:
        messages = [
            SystemMessage(system_prompt),
            HumanMessage(human_message)
        ]

        return self.chat_model.invoke(messages)
