'''
EXECUTOR SERVICES AND THREAD POOLS
Version C01: The executor service and Future objects
'''

from concurrent.futures import ThreadPoolExecutor
import time


def get_squared(x):
    #time.sleep(5)
    return x * x



executor = ThreadPoolExecutor(max_workers=1)

future = executor.submit(get_squared, 7)
#print(future.done())

print(future.result())

executor.shutdown(wait=True)

#future.result(timeout = 4) this means wait for 4 seconds and if still no result, throw timeout error