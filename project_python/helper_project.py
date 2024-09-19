from datetime import datetime
import os
import time 
import time

# basic function
def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

# worker sleep
def worker():
    time.sleep(1)
    starttime = time.time()
    print(f"thread Id : {threading.get_ident()},process ID: {os.getpid()},timestamp : {starttime}")


# this function for convert datetime
def datetime_conv(row_data):
  try:
    return datetime.strptime(row_data, '%Y-%m-%d')
  except ValueError:
    try:
      return datetime.strptime(row_data, '%m/%d/%Y')
    except:
        try:
            return datetime.strptime(row_data, '%Y-%m-%dT%H:%M:%S')
        except:
            return datetime.strptime(row_data, '%Y/%m/%d')

