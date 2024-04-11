# use fastapi to serve a static web page
# run with: uvicorn app:app --reload
import fastapi
import fastapi.responses
import fastapi.staticfiles

app = fastapi.FastAPI()
file = "index.html"

@app.get("/")
async def root():
    return fastapi.responses.FileResponse(file)
