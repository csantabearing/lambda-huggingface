from transformers import pipeline
from fastapi import FastAPI
from mangum import Mangum
import datetime
import json

model_path = './model'
classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
dfSentiment = pd.read_csv('./sentiment_data.csv')
dfSentiment['timestamp'] = pd.to_datetime(dfSentiment['timestamp'], format='%Y-%m-%d')

app = FastAPI(title='Serverless Lambda FastAPI', root_path="/Prod/")


@app.get("/sentiment", tags=["Sentiment Analysis"])
def sentiment(text: str):
    return {'result': classify(text)}


@app.get("/reddit", tags=["Tsla Bot"])
def sentiment(date0: datetime.date, dateF: datetime.date, column: str):
    cols = [x for x in dfSentiment.columns if column in x]
    dfFilter = dfSentiment[(dfSentiment['timestamp'] > date0) & (dfSentiment['timestamp'] > dateF)]
    return {'result': dfFilter[['timestamp'] + cols].to_dict('records')}


@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Ok"}


handler = Mangum(app=app)