def hello():
    msg = "Hello, World!"

    if not msg:
        raise Exception('Not the correct message')
    else:
        return msg
