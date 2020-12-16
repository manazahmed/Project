import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt

data = pd.read_csv("D:/state_wise_daily.csv") 


##filter status for all states##
df1 = data[data['Status'] == 'Confirmed']
df2 = data[data['Status'] == 'Recovered']
df3 = data[data['Status'] == 'Deceased']
#print(df1)
#print(df2)
#print(df3)


##filter status for a specific state##
d1=df1[['Date','Status','GA']]
d2=df2[['Date','Status','GA']]
d3=df3[['Date','Status','GA']]
#print(d1)
#print(d2)
#print(d3)


##drop status column and rename## 
del d1['Status']
d1.rename(columns={'GA':'Confirmed'}, inplace=True)
#print(d1)

del d2['Status']
d2.rename(columns={'GA':'Recovered'}, inplace=True)
#print(d2)

del d3['Status']
d3.rename(columns={'GA':'Deceased'}, inplace=True)
#print(d3)


##merge 3 status for specific state##
ijoin=d1.merge(d2,how="inner",on="Date")
fjoin=ijoin.merge(d3,how="inner",on="Date")


##find total##
fjoin['Total'] = fjoin.sum(axis=1)

'''
##find active cases##
#fjoin['Active'] = fjoin['Confirmed'] - fjoin['Recovered'] - fjoin['Deceased']
#print(Active)


##finding rate##
#fjoin['Active Rate %'] = (fjoin['Confirmed']/fjoin['Total'])*100

#fjoin['Recovery Rate %'] = (fjoin['Recovered']/fjoin['Total'])*100

#fjoin['Death Rate %'] = (fjoin['Deceased']/fjoin['Total'])*100


##finding traffic intensity##

#fjoin['Traffic Intensity'] = fjoin['Confirmed']/fjoin['Recovered']

#fjoin['MA'] = (fjoin['Active']/fjoin['Confirmed'])*100

#fjoin['Doubling Rate'] 
'''

writer = pd.ExcelWriter('D:/final_output-GA.xlsx', engine='xlsxwriter')

fjoin.to_excel(writer,index=False)

writer.save()


#fjoin.plot(kind='bar')
#print(pyplot.show())
