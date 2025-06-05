# 🤖 A2A Multi-Agent System

Это мультиагентная система на Python, использующая LangChain и LlamaIndex для ответа на вопросы о содержимом книг или документов.

## 🧠 Архитектура


- 🧠 **LangChain Agent** (FastAPI, GPT-4): обрабатывает запрос пользователя, вызывает инструменты.
- 📚 **LlamaIndex Agent** (FastAPI, LlamaIndex): ищет релевантный контекст в проиндексированной книге.
- 📡 Обмен между агентами — через **HTTP API** (A2A-протокол).

---

## 🧾 Возможности

- 📄 Отображение номера страницы
- 🧠 Обработка естественного языка с GPT-4
- 🐳 Изолированная работа агентов через Docker

---

## 📁 Структура проекта
a2a-system/  
├── agents/  
│ ├── langchain_agent/ # LangChain + FastAPI  
│ ├── llamaindex_agent/ # LlamaIndex + FastAPI  
│ └── common/ # Общие конфиги (например .env loader)  
├── .env # OpenAI ключ  
├── docker-compose.yml  
├── README.md  
└── .gitignore  

---

## 🚀 Быстрый старт

### 1. Склонировать репозиторий

```bash
git clone https://github.com/yourname/a2a-system.git
cd a2a-system
```
### 2. Создать .env
OPENAI_API_KEY=sk-...
### 3. Добавить файл в llamaindex_agent/data/ (например, nginx.pdf)
Затем запустить команду для создания векторной базы вашего документа
```bash
python3 index_builder.py 
```
### 4. Запустить
docker compose up --build


## Использование
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "На какой странице объясняется, что такое reverse proxy?"}'
