from transformers import pipeline
import json
model_path='./model'
classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def handler(event, context):
    body = event['body']
    queries = json.loads(body)['query']
    result={'result':[classify(x) for x in queries]}
    return json.dumps(result)