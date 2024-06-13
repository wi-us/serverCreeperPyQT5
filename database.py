from peewee import *
import datetime

db = SqliteDatabase('Server//Orders_main.sqlite')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Tables(BaseModel):
    guestCountMax = BigIntegerField(null=False)
    vipStatus = BooleanField(null=False)

    @classmethod
    def createTable(cls, **kwargs) -> bool:
        try:
            test = kwargs
            if test['vipStatus'] == 'False':
                test['vipStatus'] = 0
            else:
                test['vipStatus'] = 1
            kwargs = test
            cls.create(**kwargs)
            return True
        except:
            return False

    @classmethod
    def deleteTable(cls, table_id) -> bool:
        try:
            cls.delete().where(cls.id == table_id).execute()
            Booking.delete().where(Booking.table == cls).execute()
            return True
        except:
            return False
        

    @classmethod
    def getAllTables(cls) -> bool:
        try:
            if cls.select().count() == 0:
                return False
            else:
                _arr = []
                for val in cls.select():
                    _arr.append({"id": val.id, 
                                "guestCountMax": val.guestCountMax, 
                                "vipStatus": val.vipStatus})
                return _arr
        except:
            return False
    
    @classmethod
    def getValueById(cls, value):

        if cls.select().count() == 0:
            return None
        else:
            result =  cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            return {"id": result.id, 
                    "guestCountMax": result.guestCountMax, 
                    "vipStatus": result.vipStatus}
            
    @classmethod
    def updateTable(cls, id, **kwargs):
        query = cls.update(**kwargs).where(cls.id == id)
        query.execute()

    @classmethod
    def getTable(cls, id) -> bool:
        try:
            result = cls.select().where(cls.id.contains(str(id))).get()
            return {"id": result.id, 
                    "guestCountMax": result.guestCountMax, 
                    "vipStatus": result.vipStatus}
        except:
            return False

class Users(BaseModel):
    name = CharField(null=False)
    surname = CharField(null=False)
    phone = CharField(null=False)
    email = CharField(null=False)

    @classmethod
    def createTable(cls, **kwargs) -> bool:
        try:
            cls.create(**kwargs)
            return True
        except:
            return False
            

    @classmethod
    def deleteTableByID(cls, table_id) -> bool:
        try:
            cls.delete().where(cls.id == table_id).execute()
            Booking.delete().where(Booking.guest == cls).execute()
            return True
        except:
            return False

    @classmethod
    def getAllTables(cls) -> bool | list[dict]:
        if cls.select().count() == 0:
            return False
        else:
            try:
                _arr = []
                for val in cls.select():
                        _arr.append({"id": val.id, 
                                    "name": val.name, 
                                    "surname": val.surname, 
                                    "phone": val.phone, 
                                    "email": val.email})
                return _arr
            except:
                return False
    
    @classmethod
    def getValueById(cls, value):

        if cls.select().count() == 0:
            return 0
        else:
            result = cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            return {"id": result.id, 
                    "name": result.name, 
                    "surname": result.surname, 
                    "phone": result.phone, 
                    "email": result.email}
            
    @classmethod
    def updateTable(cls, id, **kwargs):
        query = cls.update(**kwargs).where(cls.id == id)
        query.execute()

    @classmethod
    def getTable(cls, id, phone = None) -> bool | str:
        if phone != None:
            try:
                result = cls.select().where(cls.phone.contains(str(phone))).get()
                return str(result.id)
            except:
                return False
        else:
            try:
                result = cls.select().where(cls.id.contains(str(id))).get()
                return {"id": result.id, 
                        "name": result.name, 
                        "surname": result.surname, 
                        "phone": result.phone, 
                        "email": result.email}
            except:
                return False

class Booking(BaseModel):
    table = ForeignKeyField(Tables, backref='bookings', null=True)
    guest = ForeignKeyField(Users, backref='bookings', null=True)
    bookedDate = DateTimeField(default=datetime.datetime.now())
    guestsCount = BigIntegerField(null=False)

    @classmethod
    def createTable(cls, **kwargs) -> bool:
        try:
            test = kwargs
            #table = Tables.select().where(Tables.id == kwargs["table"])
            table = Tables.select().where(Tables.id.contains(kwargs["table"])).get()
            #guests = Users.select().where(Users.id == kwargs["guest"])
            guests = Users.select().where(Users.id.contains(kwargs["guest"])).get()
            cls.create(table=table, guest=guests, bookedDate=kwargs["bookedDate"], guestsCount=kwargs["guestsCount"])
            return True
        except:
            return False

    @classmethod
    def deleteTableByID(cls, table_id) -> bool:
        try:
            cls.delete().where(cls.id == table_id).execute()
            return True
        except:
            return False

    @classmethod
    def getAllTables(cls) -> bool:
        try:
            if cls.select().count() == 0:
                return False
            
            else:
                _arr = []
                for val in cls.select():
                        try:
                            _arr.append({"id": val.id, 
                                        "table": {'id': val.table.id,
                                                    "guestCountMax": val.table.guestCountMax, 
                                                    "vipStatus": val.table.vipStatus}, 
                                        "guest": {"id": val.guest.id, 
                                                    "name": val.guest.name, 
                                                    "surname": val.guest.surname, 
                                                    "phone": val.guest.phone, 
                                                    "email": val.guest.email},
                                        "bookedDate": (val.bookedDate).strftime('%Y-%m-%d %H:%M:%S'), 
                                        "guestsCount": val.guestsCount})
                        except:
                            cls.deleteTableByID(val.id)
                return _arr
        except:
            return False
    
    @classmethod
    def getValyeById(cls, value):

        if cls.select().count() == 0:
            return 0
        else:
            result = cls.select(cls).order_by(cls.id.desc()).limit(1).tuples().get()
            return {"id": result.id, 
                    "table": result.table, 
                    "guestid": result.guest, 
                    "bookedDate": result.bookedDate, 
                    "guestsCount": result.guestsCount}
            
    @classmethod
    def _updateTable(cls, *args):
        val = args[0]
        table = Tables.get(Tables.id == val[1])
        guests = Users.get(Users.id == val[2])
        query = cls.update(table=table, guest=guests, bookedDate=val[3], bookedTime=val[4], guestsCount=val[5]).where(cls.id == val[0])
        query.execute()

    @classmethod
    def updateTable(cls, id, **kwargs):
        table = Tables.get(Tables.id == kwargs["table"].id)
        guests = Users.get(Users.id == kwargs["guest"].id)
        query = cls.update(table=table, guest=guests, bookedDate=kwargs["bookedDate"], guestsCount=kwargs["guestsCount"]).where(cls.id == id)
        query.execute()
    
    @classmethod
    def getTable(cls, id) -> str | bool:
        try:
            val = cls.select().where(cls.id.contains(str(id))).get()
            return {"id": val.id, 
                    "table": {'id': val.table.id,
                                "guestCountMax": val.table.guestCountMax, 
                                "vipStatus": val.table.vipStatus}, 
                    "guest": {"id": val.guest.id, 
                                "name": val.guest.name, 
                                "surname": val.guest.surname, 
                                "phone": val.guest.phone, 
                                "email": val.guest.email},
                    "bookedDate": (val.bookedDate).strftime('%Y-%m-%d %H:%M:%S'), 
                    "guestsCount": val.guestsCount}
        except:
            return False
    
def createTables():
    Tables().create_table()
    Users().create_table()
    Booking().create_table()