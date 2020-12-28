from flask_restx import Namespace, fields


class HDDSMARTPredictionDto:

    api = Namespace('HDDSMARTPrediction', description='HDDSMARTPrediction related operations')

    smart_prediction = api.model(
	    'SMARTPrediction',
            {
                'track_dev_id': fields.String(30, description='tracked device id', example="0"),
                'timestamp': fields.String(30, description='Prediction Timestamp', example="2019-12-01 14:20:30"),
                'model': fields.String(required=True, description='HDD model', example="XYZ"),
                'serial_number': fields.String(required=True, description='HDD serial number', example="HD00"),
                'capacity_bytes': fields.Integer(example=1000000000),
                'failure': fields.Integer,
                'prediction': fields.Float
            }
	)

    prediction_list_example = {'prediction_list': [
                {
                    "track_dev_id": "0",
                    "timestamp": "2019-12-01 14:20:30",
                    "model": "XYZ",
                    "serial_number": "HD00",
                    "capacity_bytes": 1000000000,
                    "failure": 0,
                    "prediction": 0
                },
                {
                    "track_dev_id": "1",
                    "timestamp": "2019-12-01 14:20:40",
                    "model": "UVT",
                    "serial_number": "00DH",
                    "capacity_bytes": 1000000001,
                    "failure": 1,
                    "prediction": 1
                }
            ]
        }

    smart_prediction_list = api.model(
            'SMARTPredictionList',
            {
                'prediction_list': fields.List(fields.Nested(smart_prediction))
            }
        )
