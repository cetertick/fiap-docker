from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.get("/")
def index():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        dbname=os.getenv("DB_NAME"),
    )
    return "Aplicação rodando com Docker e Postgres!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
