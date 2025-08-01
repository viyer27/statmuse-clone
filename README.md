# StatMuse Clone – NBA Query Engine

This is the backend for an AI-powered NBA stats query engine inspired by StatMuse. It uses **FastAPI**, **LangChain**, **OpenAI**, and **PostgreSQL** to convert natural language questions into SQL queries and return answers based on historical NBA stats.

🔗 **Live Demo Coming Soon**

---

## Features

- Natural language understanding via OpenAI + LangChain  
- FastAPI backend with a modern async architecture  
- PostgreSQL database with cleaned player & team stats  
- Environment-secure API key usage  
- Query processing and structured JSON responses  

---

## Project Structure

```
statmuse-clone/
├── app/
│   └── main.py              # FastAPI app entry point
├── start.sh                 # Startup script for deployment
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not committed)
├── .gitignore
└── README.md                # This file
```

---

## Local Development

### 1. Clone the repo

```bash
git clone https://github.com/viyer27/statmuse-clone.git
cd statmuse-clone
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the root of the project and add the following:

```
OPENAI_API_KEY=your_openai_key
DATABASE_URL=postgresql://username:password@host:port/dbname
```

> ⚠️ Make sure `.env` is not committed — it's excluded in `.gitignore`.

### 5. Start the server

```bash
bash start.sh
```

Your FastAPI app should now be running at:  
**http://127.0.0.1:8000**

---

## ☁️ Deploying to Render (Free Hosting)

1. Push your latest code to GitHub  
2. Go to [https://render.com](https://render.com)  
3. Click **“New → Web Service”**  
4. Select your GitHub repo  
5. Configure:
   - **Build Command**: (leave blank)
   - **Start Command**: `./start.sh`
   - **Environment**: Python 3.10+
6. Add your environment variables (`OPENAI_API_KEY`, `DATABASE_URL`) under the "Environment" tab  
7. Click **Deploy**

---

## Query Limiting (Planned)

Query limits per user (~5 queries each) will be added using:
- IP-based tracking or cookies
- Lightweight Redis or in-memory counter
- Middleware to block excess requests

---

## Data Source

The NBA data is processed from Basketball Reference stats between 1999–2025. All data is cleaned and stored in PostgreSQL.

---

## 🧑‍💻 Author

Built by **Venki Iyer**  
GitHub: [@viyer27](https://github.com/viyer27)

---

## 📄 License

MIT License
