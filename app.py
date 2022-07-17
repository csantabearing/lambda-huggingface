from transformers import pipeline
from fastapi import FastAPI
from mangum import Mangum
import json

model_path = './model'
classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

app = FastAPI(title='Serverless Lambda FastAPI')


def other_handler(event, context):
    body = event['body']
    queries = json.loads(body)['query']
    sentiments = {'result': [classify(x) for x in queries]}
    result = {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {
            'model_path': model_path
        },
        "body": json.dumps(sentiments)
    }
    return result


@app.post("/sentiment", tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}


handler = Mangum(app=app)