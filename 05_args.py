'''
PASSING ARGUMENTS
Version A: Using the Thread's constructor
'''

import threading



def do_task(a: int, b: float, c: str):
    print(f'{a}  {b}  {c}')


th = threading.Thread(target = do_task, args = (10, 20, 'hey'))
th.start()