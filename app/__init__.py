from flask_restx import Api
from flask import Blueprint

from .main.controller.hdd_smart_data import api as hdd_smart_data_ns
from .main.controller.hdd_smart_predict import api as hdd_smart_prediction_ns


from .main.controller.user import api as user_ns
from .main.controller.auth import api as auth_ns

from flask import Blueprint

blueprint = Blueprint('api', __name__)
authorizations = {
	'apikey': {
		'type': 'apiKey',
		'in': 'header',
		'name': 'Authorization',
		'description': "Type in the *'Value'* input box below: JWT, where JWT is the token"
	    }
	}	   

api = Api(
	blueprint,
	title="RESTPLUS API for HDD FAILURES PREDICTION by SMART DATA",
	version='0.1',
	description='failures prediction web service',
    )

api.add_namespace(hdd_smart_data_ns, path='/data')
api.add_namespace(hdd_smart_prediction_ns, path='/predict')
api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)

