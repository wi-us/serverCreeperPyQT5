import database as db
import json

def serializeJson(object) -> str:
    return json.dumps(object)

def deserializeJson(string : str) -> str:
    return json.loads(string)


CODE_200 = "200 OK"
CODE_400 = "400 Bad Request"
CODE_401 = "401 Unauthorized"
CODE_404 = "404 Not Found"
CODE_501 = "501 Not Implemented"

class API:
    """
    /user/\n
    /table/\n
    /booking/
    """

    PATHS = {
            "user":"/user/",
            "table":"/table/",
            "booking":"/booking/",
    }

    class User:
        path = "/user/"
        def add(**kwargs) -> dict:
            """ 
            Method:         POST\n
            Description:    add a new user row to database\n
            Return:         {'code': CODE_200, 'answer': "Success"} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                if db.Users().createTable(**kwargs):
                    return {'code': CODE_200, 'answer': "Success"}
                else: 
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
        def find(phone : int) -> str:
            """ 
            Method:         GET\n
            Description:    get user ID by his phone number\n
            Return:         {'code': CODE_200, 'answer': id} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                phone = int(phone)
                id = db.Users().getTable(id = 0, phone = phone)
                if id != False:
                    return {'code': CODE_200, 'answer': id}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
        def getByID(id : int) -> str:
            """
            Method:         GET\n
            Description:    get a user row by id\n
            Return:         {'code': CODE_200, 'answer': serializeJson(data)} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                id = int(id)
                data = db.Users().getTable(id)
                if id != False:
                    return {'code': CODE_200, 'answer': serializeJson(data)}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
        def get() -> str:
            """
            Method:         GET\n
            Description:    get all user rows\n
            Return:         {'code': CODE_200, 'answer': serializeJson(data)} or {'code': CODE_400, 'answer': "Failed"}
            """
            try:
                data = db.Users().getAllTables()
                if data != False:
                    return {'code': CODE_200, 'answer': serializeJson(data)}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}

        
        def delete(id : int) -> str:
            """
            Method:         DELETE\n
            Description:    delete user row by id\n
            Return:         {'code': CODE_200, 'answer': "Success"} or {'code': CODE_400, 'answer': "Failed"}
            """
            try:
                if db.Users().deleteTableByID(id):
                    return {'code': CODE_200, 'answer': "Success"}
                else:
                    {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        


    class Table:
        path = "/table/"
        def add(**kwargs) -> str:
            """ 
            Method:         POST\n
            Description:    add a new table row to database\n
            Return:         {'code': CODE_200, 'answer': "Success"} or {'code': CODE_400, 'answer': "Failed"}
            """
            try:
                if db.Tables().createTable(**kwargs):
                    return {'code': CODE_200, 'answer': "Success"}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
       
        def getByID(id : int) -> str:
            """
            Method:         GET\n
            Description:    get a table row by id\n
            Return:         {'code': CODE_200, 'answer': serializeJson(data)} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                data = db.Tables().getTable(id)
                if data != False:
                    return {'code': CODE_200, 'answer': serializeJson(data)}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
        def get() -> str:
            """
            Method:         GET\n
            Description:    get all table rows\n
            Return:         {'code': CODE_200, 'answer': serializeJson(data)} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                data = db.Tables().getAllTables()
                if data != False:
                    return {'code': CODE_200, 'answer': serializeJson(data)}
                else:
                    {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
        
        def delete(id : int) -> str:
            """
            Method:         DELETE\n
            Description:    delete table row by id\n
            Return:         {'code': CODE_200, 'answer': "Success"} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                if db.Tables().deleteTable(int(id)):
                    return {'code': CODE_200, 'answer': "Success"}
                else:
                    {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
    class Booking:
        path = "/booking/"
        def add(**kwargs) -> str:
            """ 
            Method:         POST\n
            Description:    add a new booking row to database\n
            Return:         {'code': CODE_200, 'answer': "Success"} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                if db.Booking().createTable(**kwargs):
                    return {'code': CODE_200, 'answer': "Success"}
                else:
                    {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
       
        def getByID(id : int) -> str:
            """
            Method:         GET\n
            Description:    get a booking row by id\n
            Return:         {'code': CODE_200, 'answer': serializeJson(data)} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                data = db.Booking().getTable(id)
                if data != False:
                    return {'code': CODE_200, 'answer': serializeJson(data)}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
            
        def get() -> str:
            """
            Method:         GET\n
            Description:    get all booking rows\n
            Return:         {'code': CODE_200, 'answer': serializeJson(data)} or {'code': CODE_400, 'answer': "Failed"}
            """
            try:
                data = db.Booking().getAllTables()
                if data != False:
                    return {'code': CODE_200, 'answer': serializeJson(data)}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
        def getBookedDates() -> str:
            try:
                data = db.Booking().getAllTables()
                arr = []
                if data != False:    
                    for item in data:
                        arr.append({'bookedDate':item['bookedDate'], 'table':item['table']})
                    return {'code': CODE_200, 'answer': serializeJson(arr)}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
        def delete(id : int) -> None:
            """
            Method:         DELETE\n
            Description:    delete booking row by id\n
            Return:         {'code': CODE_200, 'answer': "Success"} or {'code': CODE_400, 'answer': "Failed"}
            """

            try:
                if db.Booking().deleteTableByID(id):
                    return {'code': CODE_200, 'answer': "Success"}
                else:
                    return {'code': CODE_400, 'answer': "Failed"}
            except:
                return {'code': CODE_400, 'answer': "Failed"}
        
    
