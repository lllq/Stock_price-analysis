import numpy as np
import pandas as pd


 
def quarter_volume():
    # 读取数据文件
    data = pd.read_csv("GOOGL.csv",index_col='Date')
    data.index = pd.to_datetime(data.index)
    
    #数据冲采样，开盘价格（Open）、最高价格（High）、最低价格（Low）、收盘价格（Close）的均值及成交量（Volume）总和
    df=data.resample('Q').agg({'Open':'mean','High':'mean','Low':'mean','Close':'mean','Adj Close':'mean','Volume':'sum'})
    
    #通过成交量总和进行排序
    df=df.sort_values(by='Volume',ascending=False)
    return df