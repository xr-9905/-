from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import uvicorn
import pandas as pd

app = FastAPI()

file_path = os.path.join(os.path.dirname(__file__), 'html_tables', 'table_1.html')

@app.get("/", response_class=HTMLResponse)
async def read_table():
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_table = file.read()
        return HTMLResponse(content=html_table)
    except Exception as e:
        return HTMLResponse(content=f"Error reading the table: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)