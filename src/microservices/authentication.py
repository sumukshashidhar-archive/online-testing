

def authenticate(username, password):
    if username == 'admin' and password == 'admin':
        return 'admin'
    else:
        return False