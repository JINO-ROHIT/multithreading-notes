'''
HELLO WORLD VERSION MULTITHREADING
the order can differ because they are CONCURRENT not PARALLEL
'''

import threading



def do_task():
    print('Hello from example thread')



th = threading.Thread(target=do_task)
th.start()

print('Hello from main thread')