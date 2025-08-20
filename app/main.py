from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
from controller.todo_controller import router as todo_router

app = FastAPI()
origins = [
    "http://localhost:5173",  # Replace with the origin of your React app
    "http://localhost:8000",  # Add other origins as needed
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(todo_router)