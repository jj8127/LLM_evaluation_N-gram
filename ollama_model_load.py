from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# LangChain이 지원하는 다른 채팅 모델을 사용합니다. 여기서는 Ollama를 사용합니다.
llama = ChatOllama(model="llama3.2:latest", stop=["</s>"])
DUChatbot15ep = ChatOllama(model="DUchatbot:latest", stop=["</s>"])
DUChatbot10ep = ChatOllama(model="DUChatbot10ep:latest", stop=["</s>"])
DUChatbot5ep = ChatOllama(model="DUCChatbot5ep:latest", stop=["</s>"])