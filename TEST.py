import pandas as pd
import quandl

df = quandl.get("THAISE/MI_SET", authtoken="6JGEazn-nq3x76z1-pnT")

print(df.head(600*1))
