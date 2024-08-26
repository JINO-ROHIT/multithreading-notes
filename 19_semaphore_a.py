'''
SEMAPHORES
Version A: Paper sheets and packages


This code demonstrates the use of semaphores to coordinate actions between multiple threads. Let's break it down:

1. Import statements:
   ```python
   import time
   import threading
   ```
   These import the necessary modules for timing and threading.

2. Semaphore initialization:
   ```python
   sem_package = threading.Semaphore(0)
   ```
   This creates a semaphore initialized with a value of 0. Semaphores are used for synchronization between threads.

3. `make_one_sheet()` function:
   ```python
   def make_one_sheet():
       for _ in range(4):
           print('Make 1 sheet')
           time.sleep(1)
           sem_package.release()
   ```
   This function simulates making 4 sheets, one at a time. After each sheet is made, it calls `sem_package.release()`, which increments the semaphore counter.

4. `combine_one_package()` function:
   ```python
   def combine_one_package():
       for _ in range(4):
           sem_package.acquire()
           sem_package.acquire()
           print('Combine 2 sheets into 1 package')
   ```
   This function attempts to create 4 packages. For each package, it needs to acquire the semaphore twice (representing 2 sheets), then it combines them into a package.

5. Thread creation and starting:
   ```python
   threading.Thread(target=make_one_sheet).start()
   threading.Thread(target=make_one_sheet).start()
   threading.Thread(target=combine_one_package).start()
   ```
   This creates and starts three threads: two for making sheets and one for combining packages.

The key concept here is the use of the semaphore for synchronization:
- Each `make_one_sheet()` thread releases the semaphore once for each sheet it makes.
- The `combine_one_package()` thread must acquire the semaphore twice before it can make a package.

This ensures that packages are only created when enough sheets are available. If sheets aren't being produced fast enough, the package-making thread will wait until they are available.

The expected output would show sheets being made, and once two sheets are available, a package is created. This process repeats until all sheets are made and combined into packages.

This simulation mimics a real-world scenario where one process produces items (sheets) and another process consumes them (combining into packages), with the semaphore ensuring proper coordination between the processes.


'''

import time
import threading



sem_package = threading.Semaphore(0)



def make_one_sheet():
    for _ in range(4):
        print('Make 1 sheet')
        time.sleep(1)
        sem_package.release()



def combine_one_package():
    for _ in range(4):
        sem_package.acquire()
        sem_package.acquire()
        print('Combine 2 sheets into 1 package')



threading.Thread(target=make_one_sheet).start()
threading.Thread(target=make_one_sheet).start()
threading.Thread(target=combine_one_package).start()