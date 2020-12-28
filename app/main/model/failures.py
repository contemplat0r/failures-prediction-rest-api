import datetime
from .. import db, flask_bcrypt
import jwt
from .. config import key


class HDDSMARTPrediction(db.Model):

    __tablename__ = 'hdd_smart_prediction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    track_dev_id = db.Column(db.String(50))
    timestamp = db.Column(db.String(30))
    model = db.Column(db.String(50))
    serial_number = db.Column(db.String(50))
    capacity_bytes = db.Column(db.BigInteger)
    failure = db.Column(db.Integer)
    prediction = db.Column(db.Float) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __init__(self, track_dev_id, timestamp, model, serial_number, capacity_bytes, failure, prediction, user_id):
        self.track_dev_id = track_dev_id
        self.timestamp = timestamp
        self.model = model
        self.serial_number = serial_number
        self.capacity_bytes = capacity_bytes
        self.failure = failure
        self.prediction = prediction
        self.user_id = user_id


class HDDSMARTData(db.Model):

    __tablename__ = 'hdd_smart_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    track_dev_id = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.String(30))
    date = db.Column(db.String(10))
    model = db.Column(db.String(50))
    serial_number = db.Column(db.String(50))
    capacity_bytes = db.Column(db.BigInteger)
    failure = db.Column(db.Integer)
    smart_1_normalized =   db.Column(db.Float)
    smart_1_raw =          db.Column(db.Float)
    smart_3_normalized =   db.Column(db.Float)
    smart_3_raw =          db.Column(db.Float)
    smart_4_normalized =   db.Column(db.Float)
    smart_4_raw =          db.Column(db.Float)
    smart_5_normalized =   db.Column(db.Float)
    smart_5_raw =          db.Column(db.Float)
    smart_7_normalized =   db.Column(db.Float)
    smart_7_raw =          db.Column(db.Float)
    smart_9_normalized =   db.Column(db.Float)
    smart_9_raw =          db.Column(db.Float)
    smart_10_normalized =  db.Column(db.Float)
    smart_10_raw =         db.Column(db.Float)
    smart_12_normalized =  db.Column(db.Float)
    smart_12_raw =         db.Column(db.Float)
    smart_187_normalized = db.Column(db.Float)
    smart_187_raw =        db.Column(db.Float)
    smart_188_normalized = db.Column(db.Float)
    smart_188_raw =        db.Column(db.Float)
    smart_190_normalized = db.Column(db.Float)
    smart_190_raw =        db.Column(db.Float)
    smart_192_normalized = db.Column(db.Float)
    smart_192_raw =        db.Column(db.Float)
    smart_193_normalized = db.Column(db.Float)
    smart_193_raw =        db.Column(db.Float)
    smart_194_normalized = db.Column(db.Float)
    smart_194_raw =        db.Column(db.Float)
    smart_195_normalized = db.Column(db.Float)
    smart_195_raw =        db.Column(db.Float)
    smart_197_normalized = db.Column(db.Float)
    smart_197_raw =        db.Column(db.Float)
    smart_198_normalized = db.Column(db.Float)
    smart_198_raw =        db.Column(db.Float)
    smart_199_normalized = db.Column(db.Float)
    smart_199_raw =        db.Column(db.Float)
    smart_240_normalized = db.Column(db.Float)
    smart_240_raw =        db.Column(db.Float)
    smart_241_normalized = db.Column(db.Float)
    smart_241_raw =        db.Column(db.Float)
    smart_242_normalized = db.Column(db.Float)
    smart_242_raw        = db.Column(db.Float)
    batch_id             = db.Column(db.String(50))


    def __init__(
            self,
            track_dev_id,
            user_id,
            timestamp,
            date,
            serial_number,
            model,
            failure,
            capacity_bytes,
            smart_1_normalized,
            smart_1_raw,
            smart_3_normalized,
            smart_3_raw,
            smart_4_normalized,
            smart_4_raw,
            smart_5_normalized,
            smart_5_raw,
            smart_7_normalized,
            smart_7_raw,
            smart_9_normalized,
            smart_9_raw,
            smart_10_normalized,
            smart_10_raw,
            smart_12_normalized,
            smart_12_raw,
            smart_187_normalized,
            smart_187_raw,
            smart_188_normalized,
            smart_188_raw,
            smart_190_normalized,
            smart_190_raw,
            smart_192_normalized,
            smart_192_raw,
            smart_193_normalized,
            smart_193_raw,
            smart_194_normalized,
            smart_194_raw,
            smart_195_normalized,
            smart_195_raw,
            smart_197_normalized,
            smart_197_raw,
            smart_198_normalized,
            smart_198_raw,
            smart_199_normalized,
            smart_199_raw,
            smart_240_normalized,
            smart_240_raw,
            smart_241_normalized,
            smart_241_raw,
            smart_242_normalized,
            smart_242_raw,
            batch_id
        ):
        self.track_dev_id              = track_dev_id
        self.user_id                   = user_id
        self.timestamp                 = timestamp
        self.date                      = date
        self.serial_number             = serial_number
        self.model                     = model
        self.failure                   = failure
        self.capacity_bytes            = capacity_bytes
        self.smart_1_normalized        = smart_1_normalized
        self.smart_1_raw               = smart_1_raw       
        self.smart_3_normalized        = smart_3_normalized
        self.smart_3_raw               = smart_3_raw       
        self.smart_4_normalized        = smart_4_normalized
        self.smart_4_raw               = smart_4_raw       
        self.smart_5_normalized        = smart_5_normalized
        self.smart_5_raw               = smart_5_raw       
        self.smart_7_normalized        = smart_7_normalized
        self.smart_7_raw               = smart_7_raw       
        self.smart_9_normalized        = smart_9_normalized
        self.smart_9_raw               = smart_9_raw       
        self.smart_10_normalized       = smart_10_normalized
        self.smart_10_raw              = smart_10_raw       
        self.smart_12_normalized       = smart_12_normalized
        self.smart_12_raw              = smart_12_raw       
        self.smart_187_normalized      = smart_187_normalized
        self.smart_187_raw             = smart_187_raw       
        self.smart_188_normalized      = smart_188_normalized
        self.smart_188_raw             = smart_188_raw       
        self.smart_190_normalized      = smart_190_normalized
        self.smart_190_raw             = smart_190_raw       
        self.smart_192_normalized      = smart_192_normalized
        self.smart_192_raw             = smart_192_raw       
        self.smart_193_normalized      = smart_193_normalized
        self.smart_193_raw             = smart_193_raw       
        self.smart_194_normalized      = smart_194_normalized
        self.smart_194_raw             = smart_194_raw       
        self.smart_195_normalized      = smart_195_normalized
        self.smart_195_raw             = smart_195_raw       
        self.smart_197_normalized      = smart_197_normalized
        self.smart_197_raw             = smart_197_raw       
        self.smart_198_normalized      = smart_198_normalized
        self.smart_198_raw             = smart_198_raw       
        self.smart_199_normalized      = smart_199_normalized
        self.smart_199_raw             = smart_199_raw       
        self.smart_240_normalized      = smart_240_normalized
        self.smart_240_raw             = smart_240_raw       
        self.smart_241_normalized      = smart_241_normalized
        self.smart_241_raw             = smart_241_raw       
        self.smart_242_normalized      = smart_242_normalized
        self.smart_242_raw             = smart_242_raw       
        self.batch_id                  = batch_id


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    hdd_smart_datas = db.relationship(HDDSMARTData, backref='user', lazy=True)
    hdd_smart_predictions = db.relationship(HDDSMARTPrediction, backref='user', lazy=True)
   

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    @staticmethod  
    #def encode_auth_token(self, user_id):
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
                    'iat': datetime.datetime.utcnow(),
                    'sub': user_id
                }
            return jwt.encode(
                    payload,
                    key,
                    algorithm='HS256'
                )
        except Exception as e:
            return e

    @staticmethod  
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
