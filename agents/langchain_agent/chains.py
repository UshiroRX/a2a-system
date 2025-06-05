from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from common.config import OPENAI_API_KEY
import requests

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7, model_name="gpt-4")

prompt = PromptTemplate.from_template("""
Ты — умный агент. Пользователь задал вопрос: "{question}"

Вот ответ:
{context}

Ответь кратко, чётко, укажи номер страницы, если он есть.
""")


chain = LLMChain(llm=llm, prompt=prompt)

def get_context_from_llama(query: str):
    try:
        res = requests.post("http://llamaindex:8000/search", json={"query": query}, timeout=5)
        res.raise_for_status()
        data = res.json()
        print("✅ Данные от Llama:", data)
        return data["context"]
    except Exception as e:
        print("❌ Ошибка при запросе к LlamaIndex:", e)
        return "Ошибка получения контекста."


def run_chain(user_input: str) -> str:
    context = get_context_from_llama(user_input)
    response = chain.run(question=user_input, context=context)
    print(response)
    return response

