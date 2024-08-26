'''
BARRIERS AND LATCHES
Version A: Barriers

sync_point.wait() waits for 3 threads to reach there and only after that goes to the next point, if not it blocks
'''

import time
import threading



sync_point = threading.Barrier(parties = 3)



def process_request(user_name: str, wait_time: int):
    time.sleep(wait_time)

    print(f'Get request from {user_name}')
    sync_point.wait()

    print(f'Process request for {user_name}')
    sync_point.wait()

    print(f'Done {user_name}')



lstarg = [
    ('lorem', 1),
    ('ipsum', 2),
    ('dolor', 3)
]

_ = [ threading.Thread(target=process_request, args=arg).start() for arg in lstarg ]