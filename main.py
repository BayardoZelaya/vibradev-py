import os
from fastapi import FastAPI
from modules.application_calls import ApplicationCalls


app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"} 

# Add a new endpoint to check the health of the application and return 200 status code
@app.get("/health")
async def health():
    return {"status": "ok"} 

# Add a new endpoint to check the readiness of the application and return 200 status code
@app.get("/ready")
async def ready():
    return {"status": "ok"} 

# Add a new endpoint to check the liveness of the application and return 200 status code
@app.get("/live")
async def live():
    return {"status": "ok"}

# Add a new endpoint to check the version of the application and return 200 status code
@app.get("/version")
async def version():
    return {"version": "0.1.0"}

@app.get("/podname")
async def podname():
    return os.getenv("POD_NAME", "POD_NAME not set")

@app.get("/greeting")
async def greeting(name: str):
    return os.getenv("GREETING", "Hello") + " " + name

application_calls = ApplicationCalls()

@app.get("/call-service")
async def call_service(service_name: str):
    try:
        message = await application_calls.call_go_service(f'http://{service_name}')
        return {"message_from_service": message}
    except Exception:
        return {"error": "Service not available"}, 503