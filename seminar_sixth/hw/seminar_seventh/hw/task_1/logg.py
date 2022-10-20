from datetime import datetime as dt

def log_to_file(arg1, arg2, operation, result):
    path = 'logging.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign}--> {arg1} {operation} {arg2} = {result}\n')
    f.close()