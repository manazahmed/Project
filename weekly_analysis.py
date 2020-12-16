import pandas as pd

import math

import itertools

from matplotlib import pyplot

import matplotlib.pyplot as plt

sheet = ["AN","AP","AR","AS","BR","CH","CT","DN","DD","DL","GA","GJ","HR","HP","JK","JH","KA","KL","LA","LD","MP","MH","MN","ML","MZ","NL","OR","PY","PB","RJ","SK","TN","TG","TR","UP","UT","WB","UN"]

pd.set_option("display.max_rows", None, "display.max_columns", None)

growth = pd.read_excel("D:\States_Input4.xlsx", sheet_name= sheet)

writer = pd.ExcelWriter('D:/Weekly_analysis18.xlsx', engine='xlsxwriter')

#data=growth['TN']

for l in sheet:

    data=growth[l]

    con=0

    rec=0

    dec=0

    tot=0

    j=0

    week=[]

    fweek=[]

    cal=[]

    time=[]

    for k in range(0,int(len(data)/7)):

        for i in range(0,7):
        

            x=data.iloc[i+j]

        #T = T + x['Confirmed']

            con = con + x['Confirmed']

            rec= rec + x['Recovered']

            dec= dec+ x['Deceased']

            tot= tot +x['Total']

            t = x['Date']
        
        j=j+7

        week.append([con,rec,dec,tot])

        fweek.append(con)

        time.append(t)

    #print(len(fweek))


    for i in range(0,len(fweek)-1):

        try:
               
            calculation = 7/(math.log(fweek[i+1])- (math.log(fweek[i])))

        except ValueError:

            calculation=0.1

        except ZeroDivisionError:

            calculation=0.1
            
        cal.append(calculation)

   # print ("length_cal",len(cal))

    #print ("Time",len(time))

    for (i,j) in zip(week,time):

        i.append(j)

    for (i,k) in zip(week,cal):

        i.append(k)
     
    #print(week)

    df=pd.DataFrame(week,columns=['Confirmed','Recovered','Deceased','Total','Date','Growth_Rate'])

    df=df[['Date','Confirmed','Recovered','Deceased','Total','Growth_Rate']]

    df.to_excel(writer,sheet_name=l,index=False)
    
    #df.plot(x = 'Date', y = 'Growth_Rate', kind='bar')
'''
    plt.title(l)
    plt.ylabel(['Growth_Rate'])
    plt.xlabel('Date')
    plt.show()
    exit()
'''   
writer.save()
writer.close()

##################---Getting Input from the user---##################

iuser = input("Enter the State Name:")

growth = pd.read_excel("D:/Weekly_analysis18.xlsx", sheet_name= iuser)

growth.plot(x = 'Date', y = 'Growth_Rate', kind='bar')
plt.title(iuser)
plt.ylabel(['Growth_Rate'])
plt.xlabel('Date')
plt.show()
    
#####################################################


