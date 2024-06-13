
from flask_restful import Api, reqparse
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, request
from api import API

app = Flask(__name__)

@app.route('/table/', methods=['GET', 'POST'])
def tablesMethods():
    db = API.Table
    match request.method:
            case 'GET':
                return db.get()['answer']

            case 'POST':
                content_type = request.headers.get('Content-Type')
                if (content_type == 'application/json; charset=utf-8'):
                    json = request.json
                    return db.add(**json)['answer']
                else:
                    return 'Failed'


@app.route('/table/<id>', methods=['GET', 'DELETE'])
def tablesMethodsByIndex(id):
    if id == 0:
        return "Failed"
    
    match request.method:
            case 'GET':
                return API.Table.getByID(id)['answer']
            case 'DELETE':
                return API.Table().delete(id)['answer']


@app.route('/user/', methods=['GET', 'POST'])
def userMethods():
    match request.method:
        case 'GET':
                return API.User.get()['answer']

        case 'POST':
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json; charset=utf-8'):
                json = request.json
                return API.User.add(**json)['answer']
            else:
                return "Failed"

@app.route('/user/<id>', methods=['GET', 'DELETE'])
def userMethodsByIndex(id):
    if id == 0:
        return "Failed"
    
    match request.method:
        case 'GET':
                return API.User.getByID(id=id)['answer']
        case 'DELETE':
            return API.User.delete(id=id)['answer']

@app.route('/booking/', methods=['GET', 'POST'])
def bookingMethods():
    match request.method:
        case 'GET':
            return API.Booking.get()['answer']

        case 'POST':
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json; charset=utf-8'):
                json = request.json
                return API.Booking.add(**json)['answer']
            else:
                return 'Failed'

@app.route('/booking/<id>', methods=['GET', 'DELETE'])
def bookingMethodsByIndex(id):
    if id == 0:
        return "Failed"
    
    match request.method:
        case 'GET':
            return API.Booking.getByID(id=id)['answer']
        case 'DELETE':
            return API.Booking.delete(id=id)['answer']

@app.route('/user-find/<phone>', methods=['GET'])
def findUser(phone):
    if phone == 0:
        return "Failed"
    return API.User.find(phone)['answer']


@app.route('/booked-dates/', methods=['GET'])
def getBookingDates():
    return API.Booking.getBookedDates()['answer']

SWAGGER_URL = '/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swag.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)


api = Api(app)

new_user_post_args = reqparse.RequestParser()
new_user_post_args.add_argument("name",
                                type=str,
                                help="You must input a name.",
                                required=True)

new_user_post_args.add_argument("age",
                                type=int,
                                help="You must specify the age for a given name.",
                                required=False)



# http://localhost/api/new_user
app.run(host="0.0.0.0", port=80, debug=True)
