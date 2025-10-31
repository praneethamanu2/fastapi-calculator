from fastapi import FastAPI, HTTPException
from operations import add, subtract, multiply, divide
import logging

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Calculator API")

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Calculator API is running"}

@app.get("/add")
def add_numbers(a: float, b: float):
    logger.info(f"add called with a={a}, b={b}")
    return {"result": add(a, b)}

@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    logger.info(f"subtract called with a={a}, b={b}")
    return {"result": subtract(a, b)}

@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    logger.info(f"multiply called with a={a}, b={b}")
    return {"result": multiply(a, b)}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    logger.info(f"divide called with a={a}, b={b}")
    try:
        return {"result": divide(a, b)}
    except ValueError as e:
        logger.error(f"Division error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

from fastapi.responses import HTMLResponse

@app.get("/ui", response_class=HTMLResponse)
def calculator_ui():
    return """
    <html>
      <head><title>Calculator</title></head>
      <body>
        <h1>Calculator</h1>
        <input id="a" value="2" />
        <input id="b" value="3" />
        <select id="op">
          <option value="add">add</option>
          <option value="subtract">subtract</option>
          <option value="multiply">multiply</option>
          <option value="divide">divide</option>
        </select>
        <button id="calc">Calculate</button>
        <p id="result"></p>
        <script>
          document.getElementById('calc').onclick = async () => {
            const a = document.getElementById('a').value;
            const b = document.getElementById('b').value;
            const op = document.getElementById('op').value;
            const res = await fetch(`/${op}?a=${a}&b=${b}`);
            const data = await res.json();
            document.getElementById('result').innerText = "Result: " + (data.result ?? data.detail);
          };
        </script>
      </body>
    </html>
    """

