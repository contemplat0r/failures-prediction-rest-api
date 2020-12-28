import datetime
from flask import request
from flask_restx import Resource

from ..util.dto_predict import HDDSMARTPredictionDto

from ..service.failures_service import save_new_hdd_smart_predictions, get_all_failure_predictions, get_device_failure_predictions

from ..util.decorator import token_required

api = HDDSMARTPredictionDto.api
_hdd_smart_prediction = HDDSMARTPredictionDto.smart_prediction
_hdd_smart_prediction_list = HDDSMARTPredictionDto.smart_prediction_list

@api.route('/')
class HDDSMARTPredictionList(Resource):

    @api.doc('hdd_smart_predictions_list', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_list_with(_hdd_smart_prediction, envelope='data')
    def get(self, *args, **kwargs):
        """List all failure predictions"""
        return get_all_failure_predictions(kwargs['user_info'])

    @api.doc('save new predictions', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_list_with(_hdd_smart_prediction_list, envelope='data')
    @api.response(201, "failure predictions successfully saved.")
    def post(self, *args, **kwargs):
        """Save a new predictions """
        data = request.json
        prediction_list = data['prediction_list']

        return save_new_hdd_smart_predictions(kwargs['user_info'], prediction_list)


@api.route('/<track_dev_id>')
class HDDSMARTPredictionDevice(Resource):
    @api.doc('hdd_smart_predictions_track_dev', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_list_with(_hdd_smart_prediction, envelope='data')
    def get(self, track_dev_id, *args, **kwargs):
        """Show device failure predictions"""
        return get_device_failure_predictions(kwargs['user_info'], track_dev_id)

