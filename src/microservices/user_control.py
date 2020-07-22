'''
File to basically handle all user -> db operations
'''
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

def create_user(name=None, password=None, email_id=None, role=None):
    statement = "INSERT INTO auth (id, username, password, email, role) VALUES (%s, %s, %s, %s, %s)"
    if name and password and email_id and role:
        hashed_password = generate_password_hash(password, method='sha256')
        user_uuid = str(uuid.uuid4())
        
        # write to db after this
        val = (user_uuid, name, password, email_id, role)
        mycursor.execute(sql, val) 
        mydb.commit()
        pass
    else:
        return {'status':503, 'message':'did not recieve name or password', 'object':None}



def get_user(name=None):
    '''
    Must return the user from the db
    '''
    user = None
    ## testing only
    user = {'id':str(uuid.uuid4()), 'name':'sumuk', 'password':'asdadas'}
    return {'status':200, 'message':'OK', 'object':user}


def get_by_id(id):
    return {'name':'sumuk'}


def get_all_users():
    '''
    Must return all users in the table that we have now
    '''
    return None


def check_password(name=None, auth_pass=None):
    '''
    Checks the password and returns from the db
    '''
    if auth_pass and name:

        res = get_user(name=name)
        user = res['object']
        if user == None:
            return {'status':404, 'message':'user not found', 'object':None}
        if check_password_hash(user['password'], auth_pass):
            return {'status':200, 'message':'OK', 'object':user}
        else:
            #TODO:CHANGE THIS BACK
            return {'status':200, 'message':'wrong password', 'object':user}
    else:
        return {'status':404, 'message':'Bad Request. No such user', 'object':None}

