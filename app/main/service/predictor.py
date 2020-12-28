import json
import os
import pickle

import requests

import numpy as np
import pandas as pd

def get_data_source_url(url, batch_id):
    return '{}/data/{}'.format(url, batch_id)

def get_prediction_consumer_url(url):
    return '{}/predict/'.format(url)

def predict(models, data):
    features_df = data.drop(['track_dev_id', 'timestamp', 'date', 'serial_number', 'model', 'failure'], axis=1)
    probabilities = models[0].predict_proba(features_df)
    for model in models[1:]:
       probabilities = np.add(probabilities, model.predict_proba(features_df)) 
    return pd.concat(
            [
                data[['track_dev_id', 'timestamp', 'serial_number', 'model', 'failure', 'capacity_bytes']], pd.DataFrame({'prediction': probabilities[:, 1] / len(models)})
            ],
            axis=1
        )

def data_from_json(data_json):
    return pd.DataFrame(data_json['data'])

def get_data_from_source(json_source, auth_token):
    print("get_data_from_source, auth_token: ", auth_token)
    response = requests.get(json_source, headers={'Authorization': auth_token})
    return response.json() 

def get_models(models_source):
    models = []

    for model_name in models_source:
        model_file = open(model_name, 'rb')
        models.append(pickle.load(model_file))
        model_file.close()

    return models

def final_transform(prediction_df):
    return {'prediction_list': json.loads(prediction_df.to_json(orient='records'))}

def send_prediction_to_consumer(consumer_url, auth_token, prediction):
    return requests.post(consumer_url, json=prediction, headers={'Authorization': auth_token})

def execute_by_db_update_event(api_url, auth_token, batch_id, models_source):
    data_source_url = get_data_source_url(api_url, batch_id)
    data = get_data_from_source(data_source_url, auth_token)
    models = get_models(models_source)
    data = data_from_json(data)
    prediction = predict(models, data)
    prediction = final_transform(prediction)
    consumer_url = get_prediction_consumer_url(api_url)
    success = send_prediction_to_consumer(consumer_url, auth_token, prediction)

    return prediction

    
if __name__ == '__main__':
    execute_by_db_update_event('smart_short_0.json', ['xgb_clf.pkl', 'lgbm_clf.pkl'])
