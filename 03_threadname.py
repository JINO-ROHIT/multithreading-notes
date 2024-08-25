import threading

def get_name():
    print(f'name : {threading.current_thread().name}')

th_foo = threading.Thread(target = get_name, name = 'foo')
th_bar = threading.Thread(target = get_name, name = 'bar')

th_foo.start()
th_bar.start()