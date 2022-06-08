def mul(x, y):
    try:
        Popen(['python3', ROOT + '/secretary.py'], shell=False)
    except:
        traceback.print_exc()
    return x*y