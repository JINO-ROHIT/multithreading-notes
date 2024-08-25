'''
1. the thread we have created run alongside the main thread, and the output depends on how the OS decides to schedule it. 
2. there is no blocking.
3. if you uncomment the join line, it blocks till we get the result.


The Global Interpreter Lock, or GIL for short, is a design decision with the reference Python interpreter.

It refers to the fact that the implementation of the Python interpreter makes use of a master lock that prevents more than one Python instruction executing at the same time.

This prevents more than one thread of execution within Python programs, specifically within each Python process, that is each instance of the Python interpreter.

The implementation of the GIL means that Python threads may be concurrent, but cannot run in parallel. 
Recall that concurrent means that more than one task can be in progress at the same time; parallel means more than one task actually executing at the same time. 
Parallel tasks are concurrent, concurrent tasks may or may not execute in parallel.

It is the reason behind the heuristic that Python threads should only be used for IO-bound tasks, and not CPU-bound tasks, 
as IO-bound tasks will wait in the operating system kernel for remote resources to respond (not executing Python instructions), 
allowing other Python threads to run and execute Python instructions.


'''



import threading
import time

def do_task():
    time.sleep(5)
    for _ in range(300):
        print('B', end = '')


th = threading.Thread(target = do_task)
th.start()

#th.join()

print("yyya im returned")

for _ in range(300):
    print('A', end = '')

th.join()
print()