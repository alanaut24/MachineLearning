# equation of line y = mx + b
# to find out what m and b is
# use with stock prices
# continuous data
# features are like attributes

import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

print(df.head)