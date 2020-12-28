import os
import uuid
import socket

from redis import Redis
import rq

from app.main import db

from app.main.model.failures import HDDSMARTPrediction
from app.main.model.failures import HDDSMARTData
from app.main.model.failures import User

from . import predictor

api_url = os.getenv('API_URL')

redis_url = os.getenv('REDIS_URL')

queue = rq.Queue('prediction-tasks', connection=Redis.from_url(redis_url))

def save_new_hdd_smart_predictions(user_info, predictions):
    success = True
    user_id = user_info['user_id']
    for row in predictions:
        row['user_id'] = user_id
    session = db.session
    try:
        hdd_smart_predictions = [HDDSMARTPrediction(**row) for row in predictions]
        session.add_all(hdd_smart_predictions)
        session.flush()
        session.commit()
        user = session.query(User).filter(User.id==user_id).first()
        if user.hdd_smart_predictions:
            user.hdd_smart_predictions.extend(hdd_smart_predictions)
        else:
            user.hdd_smart_predictions = hdd_smart_predictions
        session.flush()
        session.commit()
    except Exception as e:
        print("save_new_hdd_smart_predictions, exeption: ", e)
        session.rollback()
        session.flush()
        success = False

def get_all_failure_predictions(user_info):
    session = db.session
    if user_info['admin']:
        return session.query(HDDSMARTPrediction).all()
    else:
        return session.query(HDDSMARTPrediction).filter(HDDSMARTPrediction.user_id==user_info['user_id']).all()

def get_device_failure_predictions(user_info, track_dev_id):
    session = db.session
    if user_info['admin']:
        device_prediction = session.query(HDDSMARTPrediction).filter(HDDSMARTPrediction.track_dev_id==track_dev_id).all()
    else:
        device_prediction = session.query(HDDSMARTPrediction).filter(
                HDDSMARTPrediction.user_id==user_info['user_id']
            ).filter(HDDSMARTPrediction.track_dev_id==track_dev_id).all()
    return device_prediction

def save_new_hdd_smart_data(user_info, data):
    success = True
    batch_id = uuid.uuid4().hex
    user_id = user_info['user_id']
    for row in data:
        row['batch_id'] = batch_id
        row['user_id'] = user_id
    session = db.session
    try:
        hdd_smart_datas = [HDDSMARTData(**row) for row in data]
        session.add_all(hdd_smart_datas)
        session.flush()
        session.commit()
        user = session.query(User).filter(User.id==user_id).first()
        if user.hdd_smart_datas:
            user.hdd_smart_datas.extend(hdd_smart_datas)
        else:
            user.hdd_smart_datas = hdd_smart_datas
        session.flush()
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        success = False

    if success:
        job = queue.enqueue('app.main.service.predictor.execute_by_db_update_event', api_url, user_info['auth_token'], batch_id, ['xgb_clf.pkl', 'lgbm_clf.pkl'])
        job.perform()

    return success

def get_all_hdd_smart_data(user_info):
    session = db.session
    if user_info['admin']:
        smart_data = session.query(HDDSMARTData).all()
    else:
        smart_data = session.query(HDDSMARTData).filter(HDDSMARTData.user_id==user_info['user_id']).all()
    return smart_data

def get_batch_of_smart_data(user_info, batch_id):
    session = db.session
    smart_data = session.query(HDDSMARTData).filter(HDDSMARTData.batch_id==batch_id).all()
    return smart_data

def save_changes(data):
    db.session.add(data)
    db.session.commit()
