from src.flask.api.controllers.sql import sql_auth


def login(username, password):
    '''
    Has to search the sql database for this combination and return the appropriate response
    with all the needed data about the user
    '''
    row = sql_auth(username)
    if row['password'] == password:
        return row
    else:
        return False


def temp_login(username, password):
    '''
    Has to search the sql database for this combination and return the appropriate response
    with all the needed data about the user
    '''
    if True:
        return {"status":True}
    else:
        return {"status":False, "message":"Wrong Password"}
