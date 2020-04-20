

def is_null(*params):
    for i in params:
        if i == None and i == '':
            return False
    return True


is_null(1,2,3)
