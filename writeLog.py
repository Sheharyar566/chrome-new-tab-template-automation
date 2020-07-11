log_file = 'F://work/log.txt'

def writeLog(message):
    with open(log_file, 'a') as log:
        log.write(str(message) + '\n')