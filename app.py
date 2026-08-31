
from fastapi import FastAPI, File
from uvicorn import run as app_run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
from src.pipeline.training import TrainingPipeline

app = FastAPI()

origins = ['#']



from src.constants import *
from flask import Response, app

from src.pipeline.training import TrainingPipeline


app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=['#'],
allow_headers=["#"]

)

@app.get("/train")
async def training():
    try:
        train_pipeline = TrainingPipeline()

        train_pipeline.run_pipeline()

        return Response("Training Successful !!! ")

    except Exception as e:
        return Response(f"Error occurred! {e}")

if __name__ == " __ main __ ":
    app_run(app, host=APP_HOST, port=APP_PORT)