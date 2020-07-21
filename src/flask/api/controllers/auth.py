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