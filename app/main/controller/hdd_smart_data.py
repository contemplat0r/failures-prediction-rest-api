from flask import request

from flask_restx import Resource

from ..service.failures_service import save_new_hdd_smart_data, get_all_hdd_smart_data, get_batch_of_smart_data

from ..util.decorator import token_required

from ..util.dto_data import HDDSMARTDataDto

api = HDDSMARTDataDto.api
_hdd_smart_data = HDDSMARTDataDto.smart_data
_hdd_smart_data_list = HDDSMARTDataDto.smart_data_list

@api.route('/')
class HDDSMARTDataList(Resource):
    @api.doc('hdd_smart_data_list', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_list_with(_hdd_smart_data, envelope='data')
    def get(self, *args, **kwargs):
        """List all data values"""
        return get_all_hdd_smart_data(kwargs['user_info'])

    @api.doc('save new chunk data values', body=_hdd_smart_data_list, params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.response(201, "data values successfully saved.")
    def post(self, *args, **kwargs):
        """Save a new data value """
        data = request.json
        data_list = data['smart_data_list']
        return save_new_hdd_smart_data(kwargs['user_info'], data_list)

@api.route('/<batch_id>')
class HDDSMARTDataBatch(Resource):
    @api.doc('hdd_smart_data_batch', params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @token_required
    @api.marshal_list_with(_hdd_smart_data, envelope='data')
    def get(self, batch_id, *args, **kwargs):
        """List batch of data (data transmitted in a single POST request, together with assigned indetifier"""
        return get_batch_of_smart_data(kwargs['user_info'], batch_id)
