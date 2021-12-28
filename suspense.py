import time

def suspenseprint(msg):
    for c in msg:
        print(c, end='', flush=True)
        time.sleep(0.0666)

    print('')

