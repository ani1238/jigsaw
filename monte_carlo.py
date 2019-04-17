# -*- coding: utf-8 -*-
import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

data=pd.read_csv('data.csv')

sp.random.seed(12345)
mydata=data.loc[data['1.1'] ==11]
mydata.columns=['index','gender','time','age','shape','row','col','clicks','maxdiff','clicks-time']

data3x3=mydata.loc[(mydata['row']==3) & (mydata['col']==3)]
 

timemean3x3=data3x3["time"].mean()
timestd3x3=data3x3["time"].std()


clicksmean3x3=data3x3["clicks"].mean()
clickstd3x3=data3x3["clicks"].std()

#generating random clicks
clicks3x3=np.array(sp.random.normal(clicksmean3x3,clickstd3x3/3,500),dtype='int')
print(clicks3x3)

#plotting clicks histogram
plt.hist(clicks3x3)
plt.title("plotting clicks")
plt.xlabel("clicks")
plt.ylabel("Frequency")
plt.show()

#generating random time
time3x3=np.array(sp.random.normal(timemean3x3,timestd3x3/3,500))
print(time3x3)

#plotting time histogram
plt.hist(time3x3)
plt.title("plotting time")
plt.xlabel("time")
plt.ylabel("Frequency")
plt.show()

#plotting clicks vs time scatter plot
plt.plot(clicks3x3, time3x3, 'ro')
plt.axis([10, 35, 30, 70])
plt.show()



maxdif=data3x3['maxdiff'].mean()

click_time=data3x3[['clicks-time']]

#converting string of clicks-time to list of floats
mindiflis=list()
for index, row in click_time.iterrows():
    lists=row['clicks-time'][1:-1]
    lists=lists.split(',')
    list1=list()
    for i in lists:
        var=float(i)
        list1.append(var)
    mindif=float('inf')
    for i in range(0,len(list1)-1):
        if ((list1[i+1]-list1[i]<mindif)&(list1[i+1]-list1[i]!=0.0)):
            mindif=list1[i+1]-list1[i]
    mindiflis.append(mindif)
  
#generating random value of clicks-time          
mindif=np.array(mindiflis).mean()

stmean=(maxdif-mindif)/2;

stdiv=min(stmean-mindif,maxdif-stmean)
print(stmean,stdiv)
for i in range(0,500):
    click=clicks3x3[i]
    time=time3x3[i]
    avgclick=time/click
    list2=list()
    list2.append(0.0)
   # list3=np.array(sp.random.uniform(mindif,avgclick,(click-2)))
   # print(list3)
    for j in range(0,click-2):
        rand=np.random.uniform(j*avgclick,(j+1)*avgclick)
        list2.append(rand)
    list2.append(time)
    print(list2)
    
#fuzzy
time=ctrl.Antecedent(np.arange(30,70,1),'time')
iq=ctrl.Consequent(np.arange(70,200,1),'iq')

time.automf(5)
time.view()

iq['normal']=fuzz.gaussmf(iq.universe,115,4)
iq['superior']=fuzz.gaussmf(iq.universe,130,4)
iq['very superior']=fuzz.gaussmf(iq.universe,145,4)
iq['dullness']=fuzz.gaussmf(iq.universe,85,4)
iq['mensa level']=fuzz.gaussmf(iq.universe,200,4)

iq.view()
rule1=ctrl.Rule(time['poor'],iq['mensa level'])
rule2=ctrl.Rule(time['mediocre'],iq['very superior'])
rule3=ctrl.Rule(time['average'],iq['superior'])
rule4=ctrl.Rule(time['decent'],iq['normal'])
rule5=ctrl.Rule(time['good'],iq['dullness'])

rule3.view()

iq_control=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5])
iqsim=ctrl.ControlSystemSimulation(iq_control)

iqsim.input['time'] = 45
iqsim.compute()

print(iqsim.output['iq'])
