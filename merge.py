import pandas as pd

from matplotlib import pyplot

import matplotlib.pyplot as plt


df1 = pd.read_excel("D:/final_output-AN.xlsx") 

df2 = pd.read_excel("D:/final_output-AP.xlsx")

df3 = pd.read_excel("D:/final_output-AR.xlsx") 

df4 = pd.read_excel("D:/final_output-AS.xlsx")

df5 = pd.read_excel("D:/final_output-BR.xlsx") 

df6 = pd.read_excel("D:/final_output-CH.xlsx") 

df7 = pd.read_excel("D:/final_output-CT.xlsx") 

df8 = pd.read_excel("D:/final_output-DN.xlsx") 

df9 = pd.read_excel("D:/final_output-DD.xlsx") 

df10 = pd.read_excel("D:/final_output-DL.xlsx") 

df11 = pd.read_excel("D:/final_output-GA.xlsx") 

df12 = pd.read_excel("D:/final_output-GJ.xlsx") 

df13 = pd.read_excel("D:/final_output-HR.xlsx") 

df14 = pd.read_excel("D:/final_output-HP.xlsx") 

df15 = pd.read_excel("D:/final_output-JK.xlsx") 

df16 = pd.read_excel("D:/final_output-JH.xlsx") 

df17 = pd.read_excel("D:/final_output-KA.xlsx") 

df18 = pd.read_excel("D:/final_output-KL.xlsx") 

df19 = pd.read_excel("D:/final_output-LA.xlsx") 

df20 = pd.read_excel("D:/final_output-LD.xlsx") 

df21 = pd.read_excel("D:/final_output-MP.xlsx") 

df22 = pd.read_excel("D:/final_output-MH.xlsx") 

df23 = pd.read_excel("D:/final_output-MN.xlsx") 

df24 = pd.read_excel("D:/final_output-ML.xlsx") 

df25 = pd.read_excel("D:/final_output-MZ.xlsx") 

df26 = pd.read_excel("D:/final_output-NL.xlsx") 

df27 = pd.read_excel("D:/final_output-OR.xlsx") 

df28 = pd.read_excel("D:/final_output-PY.xlsx") 

df29 = pd.read_excel("D:/final_output-PB.xlsx") 

df30 = pd.read_excel("D:/final_output-RJ.xlsx") 

df31 = pd.read_excel("D:/final_output-SK.xlsx") 

df32 = pd.read_excel("D:/final_output-TN.xlsx") 

df33 = pd.read_excel("D:/final_output-TG.xlsx") 

df34 = pd.read_excel("D:/final_output-TR.xlsx")

df35 = pd.read_excel("D:/final_output-UP.xlsx") 

df36 = pd.read_excel("D:/final_output-UT.xlsx") 

df37 = pd.read_excel("D:/final_output-WB.xlsx") 

df38 = pd.read_excel("D:/final_output-UN.xlsx") 

writer = pd.ExcelWriter('D:/States_Input18.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='AN',index=False)

df2.to_excel(writer, sheet_name='AP',index=False)

df3.to_excel(writer, sheet_name='AR',index=False)

df4.to_excel(writer, sheet_name='AS',index=False)

df5.to_excel(writer, sheet_name='BR',index=False)

df6.to_excel(writer, sheet_name='CH',index=False)

df7.to_excel(writer, sheet_name='CT',index=False)

df8.to_excel(writer, sheet_name='DN',index=False)

df9.to_excel(writer, sheet_name='DD',index=False)

df10.to_excel(writer, sheet_name='DL',index=False)

df11.to_excel(writer, sheet_name='GA',index=False)

df12.to_excel(writer, sheet_name='GJ',index=False)

df13.to_excel(writer, sheet_name='HR',index=False)

df14.to_excel(writer, sheet_name='HP',index=False)

df15.to_excel(writer, sheet_name='JK',index=False)

df16.to_excel(writer, sheet_name='JH',index=False)

df17.to_excel(writer, sheet_name='KA',index=False)

df18.to_excel(writer, sheet_name='KL',index=False)

df19.to_excel(writer, sheet_name='LA',index=False)

df20.to_excel(writer, sheet_name='LD',index=False)

df21.to_excel(writer, sheet_name='MP',index=False)

df22.to_excel(writer, sheet_name='MH',index=False)

df23.to_excel(writer, sheet_name='MN',index=False)

df24.to_excel(writer, sheet_name='ML',index=False)

df25.to_excel(writer, sheet_name='MZ',index=False)

df26.to_excel(writer, sheet_name='NL',index=False)

df27.to_excel(writer, sheet_name='OR',index=False)

df28.to_excel(writer, sheet_name='PY',index=False)

df29.to_excel(writer, sheet_name='PB',index=False)

df30.to_excel(writer, sheet_name='RJ',index=False)

df31.to_excel(writer, sheet_name='SK',index=False)

df32.to_excel(writer, sheet_name='TN',index=False)

df33.to_excel(writer, sheet_name='TG',index=False)

df34.to_excel(writer, sheet_name='TR',index=False)

df35.to_excel(writer, sheet_name='UP',index=False)

df36.to_excel(writer, sheet_name='UT',index=False)

df37.to_excel(writer, sheet_name='WB',index=False)

df38.to_excel(writer, sheet_name='UN',index=False)


writer.save()


sheet = ["AN","AP","AR","AS","BR","CH","CT","DN","DD","DL","GA","GJ","HR","HP","JK","JH","KA","KL","LA","LD","MP","MH","MN","ML","MZ","NL","OR","PY","PB","RJ","SK","TN","TG","TR","UP","UT","WB","UN"]


pd.set_option("display.max_rows", None, "display.max_columns", None)

data = pd.read_excel("D:\States_Input18.xlsx", sheet_name= sheet)

writer=pd.ExcelWriter('D:/COVID-108.xlsx',engine='xlsxwriter')


for sheet_name in sheet:

    info=data[sheet_name]

    info['Active'] = (info['Confirmed'] - info['Recovered'] - info['Deceased']).abs()
    
    info['Active Rate %'] = (info['Confirmed']/info['Total']).abs()*100

    info['Recovery Rate %'] = (info['Recovered']/info['Total']).abs()*100

    info['Death Rate %'] = (info['Deceased']/info['Total']).abs()*100

    info['Traffic Intensity'] = info['Confirmed']/info['Recovered'].abs()

    info['MA'] = (info['Active']/info['Confirmed']).abs()*100

    data[sheet_name].to_excel(writer,sheet_name=sheet_name,index=False)

    print(sheet_name)
    
    print(info.mean())

    #print(mydata.median())
    
'''
    info.plot(x = 'Date', y = ['Active','Confirmed','Recovered','Total','Active Rate %','Recovery Rate %','Death Rate %','Traffic Intensity','MA'], kind='line')

    plt.title(sheet_name)
    plt.ylabel(['Active','Confirmed','Recovered','Total','Active Rate %','Recovery Rate %','Death Rate %','Traffic Intensity','MA'])
    plt.xlabel('Date')
    plt.show()

    info.plot(x = 'Date', y = ['Active','Confirmed','Recovered','Total'], kind='line')

    plt.title(sheet_name)
    plt.ylabel(['Active','Confirmed','Recovered','Total'])
    plt.xlabel('Date')
    plt.show()

    info.plot(x = 'Date', y = ['Total','Active Rate %','Recovery Rate %','Death Rate %'], kind='line')

    plt.title(sheet_name)
    plt.ylabel(['Total','Active Rate %','Recovery Rate %','Death Rate %'])
    plt.xlabel('Date')
    plt.show()

    info.plot(x = 'Date', y = ['Total','Traffic Intensity'], kind='line')

    plt.title(sheet_name)
    plt.ylabel(['Total','Traffic Intensity'])
    plt.xlabel('Date')
    plt.show()

    info.plot(x = 'Date', y = ['Total','MA'], kind='line')

    plt.title(sheet_name)
    plt.ylabel(['Total','MA'])
    plt.xlabel('Date')
    plt.show()

    exit()
 '''

writer.save()
writer.close()

##################---Getting Input from the user----##################

iuser = input("Enter the State Name:")

growth = pd.read_excel("D:/COVID-108.xlsx", sheet_name= iuser)

growth.plot(x = 'Date', y = ['Active','Confirmed','Recovered','Deceased','Total'], kind='line')

plt.title(iuser)
plt.ylabel(['Active','Confirmed','Recovered','Deceased','Total'])
plt.xlabel('Date')
plt.show()

growth.plot(x = 'Date', y = ['Total','Active Rate %','Recovery Rate %','Death Rate %'], kind='line')

plt.title(iuser)
plt.ylabel(['Total','Active Rate %','Recovery Rate %','Death Rate %'])
plt.xlabel('Date')
plt.show()

growth.plot(x = 'Date', y = ['Total','Traffic Intensity'], kind='line')

plt.title(iuser)
plt.ylabel(['Total','Traffic Intensity'])
plt.xlabel('Date')
plt.show()

growth.plot(x = 'Date', y = ['Total','MA'], kind='line')

plt.title(iuser)
plt.ylabel(['Total','MA'])
plt.xlabel('Date')
plt.show()


median=[growth['Active'],growth['Confirmed'],growth['Recovered'],growth['Deceased'],growth['Total']]

fig = plt.figure(figsize =(10,7))

ax = fig.add_subplot(111)

plt.title(iuser)

ax.set_xticklabels(['Active','Confirmed','Recovered','Deceased','Total'])

plt.boxplot(median)

plt.show()


####################################################################   

