from datetime import datetime

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

