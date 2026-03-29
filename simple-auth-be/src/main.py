from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.database import Base, engine
from src.features.auth.router import auth_router, user_router


# Prepare db metadata
# Base.metadata.create_all(bind=engine)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This only runs when Uvicorn actually starts the server
    Base.metadata.create_all(bind=engine)
    yield


# Create App object
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Auth feature
app.include_router(auth_router)
app.include_router(user_router)
