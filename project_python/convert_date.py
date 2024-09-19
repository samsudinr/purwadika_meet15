import pandas as pd
from datetime_helper import datetime_conv


data = {'date': ['2024-01-01', ' 12/02/2024', '12/28/2024', '2024-09-09T10:30:00', '1999/12/31']}
df = pd.DataFrame(data)

df['new_date'] = df['date'].apply(lambda x: datetime_conv(x))
print(df)
