import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from scipy.stats import norm
import matplotlib.mlab as mlab

data=pd.read_csv('data1.csv')

sp.random.seed(12345)
data.columns=['index','gender','time','age','shape','row','col','clicks','maxdiff','clicks-time','iq']
time=data["time"]

#plotting time histogram
plt.hist(time)
plt.title("plotting time")
plt.xlabel("time")
plt.ylabel("Frequency")
#plt.show()
fig=plt.figure()

mean=time.mean()
std=time.std()
f= open("databyage.txt","w+")


for i in range(6,16):
    databyage=data.loc[data['age']==i]
    databyage=databyage["time"]
    plt.subplot(2,5,i-5)
    plt.hist(databyage)
    agemean=databyage.mean()
    agestd=databyage.std()
    c=databyage.count()
    f.write("%d,%f,%f,%d",i,agemean,agestd,c)
    


    #print(databyage)

plt.show()

# best fit of data
(mu, sigma) = norm.fit(time)

# the histogram of the data
n, bins, patches = plt.hist(time, 54, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)

#plot
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
plt.grid(True)

plt.show()
