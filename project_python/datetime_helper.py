from datetime import datetime

# feedback loop
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
