from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.2)
response = llm.invoke([HumanMessage(content="Explain quantum computing in two sentences.")])
print(response.content[0]["text"])
