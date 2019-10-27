import numpy as np
import pandas as pd


 
def quarter_volume():
    # ��ȡ�����ļ�
    data = pd.read_csv("GOOGL.csv",index_col='Date')
    data.index = pd.to_datetime(data.index)
    
    #���ݳ���������̼۸�Open������߼۸�High������ͼ۸�Low�������̼۸�Close���ľ�ֵ���ɽ�����Volume���ܺ�
    df=data.resample('Q').agg({'Open':'mean','High':'mean','Low':'mean','Close':'mean','Adj Close':'mean','Volume':'sum'})
    
    #ͨ���ɽ����ܺͽ�������
    df=df.sort_values(by='Volume',ascending=False)
    return df