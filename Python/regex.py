import re
import pandas as pd

df = pd.read_excel('c:\PyScripts\SLA Report\Data\Merged\MergedTicket.xlsx')
regexList = ['[Ll]at[Ll]', '[Dd]elta.*\Sync', 'FSE.*\BC', '[Rr][Dd][Ss].Deployment.*[Gg][Ii][Ss]']
for i in regexList:
    print(i)
    df=df[df['Title'].str.match(i)==False]
    df.to_excel(r'c:\PyScripts\SLA Report\Data\Merged\MergedTicket.xlsx', index = False, header = True)
    df