import pandas as pd
import numpy as np

f = pd.read_csv('results.csv')
tmp = f

dates = f['date'].as_matrix()
exact = pd.to_datetime(dates, format='%Y-%m-%d')

tmp['year']  = pd.Series(exact.year , index=tmp.index)
tmp['month'] = pd.Series(exact.month, index=tmp.index)
tmp['day']   = pd.Series(exact.day  , index=tmp.index)
tmp['total_score'] = pd.Series(f['home_score']+f['away_score'], index=tmp.index)

tmp.to_csv('results_modified.csv', index=False)
