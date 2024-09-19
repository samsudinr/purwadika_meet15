import threading
import os
import time 

def worker():
    time.sleep(1)
    starttime = time.time()
    print(f"thread Id : {threading.get_ident()},process ID: {os.getpid()},timestamp : {starttime}")

if __name__ == "__main__":
    print(f"Main process ID: {os.getpid()}")

    print("== Running using loop")    
    for _ in range(5):
        worker()
    
    print("== runnig using threading")
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    

    for thread in threads:
        thread.join()
    