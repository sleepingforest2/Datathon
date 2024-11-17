import psycopg2
import pandas as pd
import numpy as np
conn = psycopg2.connect(database=mountedDB['mimiciv4725']['database'],
                        user=mountedDB['mimiciv4725']['username'],
                        password=mountedDB['mimiciv4725']['password'],
                        host=mountedDB['mimiciv4725']['host'],
                        port=mountedDB['mimiciv4725']['port'])
query="select * from mimiciv_hosp.labevents limit 10"
test=pd.read_sql_query(query,conn)
query="select * from mimiciv_hosp.d_labitems"
test=pd.read_sql_query(query,conn)
test.to_csv("mimiciv_hosp.d_labitems.csv",index=False)
query="select * from information_schema.tables"
table_name=pd.read_sql_query(query,conn)
query="select * from information_schema.columns"
table_key=pd.read_sql_query(query,conn)
query="select * from mimiciv_icu.d_items"
icu_item=pd.read_sql_query(query,conn)
icu_item.to_csv("mimiciv_icu.d_items.csv",index=False)
candi_data=table_key[table_key.column_name=="itemid"]['table_schema']+'.'+	table_key[table_key.column_name=="itemid"]['table_name']
#mimiciv_hosp.labevents
#
file=pd.read_csv("item_file",header=0,index_col=None)
for i in file.label:
    conn = psycopg2.connect(database=mountedDB['mimiciv4725']['database'],
                        user=mountedDB['mimiciv4725']['username'],
                        password=mountedDB['mimiciv4725']['password'],
                        host=mountedDB['mimiciv4725']['host'],
                        port=mountedDB['mimiciv4725']['port'])
    query="select  subject_id,hadm_id,itemid,charttime,valuenum,ref_range_lower,ref_range_upper from mimiciv_hosp.labevents where itemid={}".format(i)
    data=pd.read_sql_query(query,conn)
    data = data.dropna()
    data['charttime'] = pd.to_datetime(data['charttime'])
    data_last = data.drop_duplicates(subset=['subject_id','hadm_id','itemid'], keep='last')
    data_last.to_csv("Item_"+str(i)+".csv",index=False)
    print(i)