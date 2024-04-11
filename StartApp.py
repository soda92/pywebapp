# use uvicorn to start the app
import uvicorn
from app import app

uvicorn.run(app=app, host="0.0.0.0", port=80, log_level="info")
