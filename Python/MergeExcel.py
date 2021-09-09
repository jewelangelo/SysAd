import numpy as np
import pandas as pd
import glob

all_data = pd.DataFrame()
for f in glob.glob("C:\PyScripts\SLA Report\Data\Raw\*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

writer = pd.ExcelWriter('C:\PyScripts\SLA Report\Data\Merged\MergedTicket.xlsx')
all_data.to_excel(writer,'sheet1', index=False)
writer.save()

df = pd.read_excel(writer)
df.insert(6, "Type", '', False)
df.insert(13, "Pending Time Prior to Assigning Agent", '=(P2+Q2+R2+S2)/86400', False)
df.insert(14,"Pending Time After to Assigning Agent", '=(T2+U2)/86400', False)
df.to_excel('C:\PyScripts\SLA Report\Data\Merged\MergedTicket.xlsx', index=False)

