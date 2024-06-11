from flask import Flask
from flask import request
import json
import api 
import enums

app = Flask(__name__)

@app.route('/table', methods=['GET', 'POST'])
def tablesMethods():
    db = api.API.Table
    match request.method:
            case 'GET':
                answer = db.get()['answer']
                if answer == 'null':
                    return None
                else:
                    return answer

            case 'POST':
                content_type = request.headers.get('Content-Type')
                if (content_type == 'application/json; charset=utf-8'):
                    json = request.json
                    return db.add(**json)
                else:
                    return None


@app.route('/table/', methods=['GET', 'DELETE'])
def tablesMethodsByIndex():
    db = api.API.Table
    id = str(request.args.get('value'))

    match request.method:
            case 'GET':
                answer = db.get(id=id)['answer']
                if answer == 'null':
                    return None
                else:
                    return str(answer)
            case 'DELETE':
                return db.delete(id=id)

@app.route('/user', methods=['GET', 'POST'])
def userMethods():
    db = api.API.User
    match request.method:
        case 'GET':
            answer = db.get()['answer']
            if answer == 'null':
                return None
            else:
                return answer

        case 'POST':
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json; charset=utf-8'):
                json = request.json
                return db.add(**json)
            else:
                return None

@app.route('/user/', methods=['GET', 'DELETE'])
def userMethodsByIndex():
    db = api.API.User
    id = str(request.args.get('value'))
    match request.method:
        case 'GET':
            answer = db.get(id=id)['answer']
            if answer == 'null':
                return None
            else:
                return str(answer)
        case 'DELETE':
            return db.delete(id=id)

@app.route('/booking', methods=['GET', 'POST'])
def bookingMethods():
    db = api.API.Booking
    match request.method:
        case 'GET':
            answer = db.get()['answer']
            if answer == 'null':
                return None
            else:
                return answer

        case 'POST':
            content_type = request.headers.get('Content-Type')
            if (content_type == 'application/json; charset=utf-8'):
                json = request.json
                return db.add(**json)
            else:
                return None

@app.route('/booking/', methods=['GET', 'DELETE'])
def bookingMethodsByIndex():
    db = api.API.Booking
    id = str(request.args.get('value'))
    match request.method:
        case 'GET':
            answer = db.get(id=id)['answer']
            if answer == 'null':
                return None
            else:
                return str(answer)
        case 'DELETE':
            return db.delete(id=id)

@app.route('/user-find/', methods=['GET'])
def findUser():
    db = api.API.User
    id = str(request.args.get('value'))
    answer = db.find(id)['answer']
    
    if answer == 'null':
        return None
    else:
        test = json.dumps({"value":answer})
        _test = json.dumps(answer)
        return str(answer)


@app.route('/booked-dates', methods=['GET'])
def getBookingDates():
    db = api.API.Booking
    answer = db.getBookedDates()['answer']
    if answer == 'null':
        return None
    else:
        return answer


app.run(host='0.0.0.0', port=8001)