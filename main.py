from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
        <html>
        <body>
            <form action="/greet" method="post">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    """

@app.post("/greet", response_class=HTMLResponse)
def greet(username: str = Form(...)):
    return f"""
        <html>
        <body>
            <h2>Hello {username}, Welcome to this app for Docker demonstration.</h2>
            <p>Please consider like and subscribe to the channel.</p>
        </body>
        </html>
    """
