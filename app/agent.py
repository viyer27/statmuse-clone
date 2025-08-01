from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_community.chat_models import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
import os
import ssl

# ✅ Load environment variables from .env
load_dotenv(find_dotenv())

# 🔐 Read API key and DB URL
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

# 🛡️ Set up SSL for Aiven PostgreSQL
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 🛢️ Connect to the database with SSL
db = SQLDatabase.from_uri(
    DATABASE_URL,
    engine_args={"connect_args": {"ssl_context": ssl_context}}
)

# 🤖 Set up the LLM with the correct key
llm = ChatOpenAI(
    model="gpt-4o",  # You can change to "gpt-3.5-turbo" if needed
    temperature=0,
    openai_api_key=OPENAI_API_KEY
)

# 🧰 Build the SQL Toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# 🧠 Create the agent executor
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    handle_parsing_errors=True
)
