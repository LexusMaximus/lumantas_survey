from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import GPUGamingSurvey

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/gpugamingsurvey/{id}")
async def read_survey(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        gpugamingsurvey = session.get(GPUGamingSurvey, id)
        return {"message": gpugamingsurvey}
    

@app.post("/GPUGamingSurvey")
async def root(GPUGamingSurvey  : GPUGamingSurvey):
    with Session(engine) as session:
        session.add(GPUGamingSurvey)
        session.commit()
        session.refresh(GPUGamingSurvey)
        return {"message": GPUGamingSurvey}