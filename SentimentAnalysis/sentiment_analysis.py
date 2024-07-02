'''
This module uses WATSON AI to create a sentiment analysis feature
'''

import json
import requests


def sentiment_analyzer(text_to_analyse):
    '''
    Sentiment Analysis Function returns a dictionary
    '''
    timeout_value = 5
    url = '''https://sn-watson-sentiment-bert.labs.skills.network/
    v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'''
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header, timeout=timeout_value)
    text = json.loads(response.text)
    label = ''
    score = ''

    if response.status_code == 200:
        score = text["documentSentiment"]["score"]
        label = text["documentSentiment"]["label"]
    elif response.status_code == 500:
        label = None
        score = None

    my_output = {
            "score" : score,
            "label"  : label
        }

    return my_output
