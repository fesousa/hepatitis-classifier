import json
import traceback
import os

from joblib import dump, load


def execute(event, context):
    print(event)
    clf = load('model/hepatite.joblib') 
    req = json.loads(event['body'])
    print(req['data'])
    predict = clf.predict([req['data']])
    print("PREDICT", predict.tolist())
    return {'statusCode': 200, "body":json.dumps(predict.tolist()), "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST"}}
        
   
