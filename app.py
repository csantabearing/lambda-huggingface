from transformers import pipeline
import json
model_path='./model'
classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def handler(event, context):
    body = event['body']
    queries = json.loads(body)['query']
    sentiments={'result':[classify(x) for x in queries]}
    result={
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {'model_path':model_path},
        "body": json.dumps(sentiments)
    }  
    return result