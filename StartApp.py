# use uvicorn to start the app
import uvicorn
from app import app

uvicorn.run(app=app, host="127.0.0.1", port=8000, log_level="info")
