import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
def index():
    content = """
    <h1>Hello FastAPI Web</h1>
    <div>This is hwere our fake pypi app will live!</div>
    """
    return fastapi.responses.HTMLResponse(content)


if __name__ == "__main__":
    uvicorn.run(app)
