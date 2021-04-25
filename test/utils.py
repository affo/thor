from thor import execute_string, ThorException

def exec_ok(stmt):
    v = execute_string(stmt + ';', debug=True)
    if v is not None and len(v.debug_info) > 0:
        return v.debug_info[-1].value
    return None

def exec_ko(stmt):
    try:
        execute_string(stmt + ';', debug=True)
        return None
    except ThorException as e:
        return str(e)
