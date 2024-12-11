from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET", "POST"],  # Allow GET method
    allow_headers=["*"],  # Allow all headers
)

# GET endpoint
@app.get("/api/greet")
async def greet(name: str = "World"):
    return {"message": f"Hello, {name}!"}

# POST endpoint
@app.post("/api/greet")
async def greet_post(request: Request):
    data = await request.json()  # Parse JSON body
    name = data.get("name", "World")
    return {"message": f"Hello, {name}!"}


# uvicorn app:app --reload