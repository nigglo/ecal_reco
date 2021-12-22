import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading of the different data file
run_n=1
data=np.loadtxt(f'/home/cholak/Documents/data_test/run_00000{run_n}/data1.txt', delimiter=',')
tdc=pd.read_csv(f'/home/cholak/Documents/data_test/run_00000{run_n}/tdc_cal.csv', delimiter=',')
qdc=pd.read_csv(f'/home/cholak/Documents/data_test/run_00000{run_n}/qdc_cal.csv', delimiter=',')

#MAKE THE COMPUTATIONS FOR EACH TOFPET MEASURED (HERE IT IS TOFPET 4 AND 5)

#Extraction of the values provided by the data
data5=data.query('tofpet_id==5') #takes data corresponding to tofpet 5
data4=data.query('tofpet_id==4') #takes data corresponding to tofpet 4
tc4=data4['timestamp_coarse']
tc5=data5['timestamp_coarse']
tf4=data4['timestamp_fine']
tf5=data5['timestamp_fine']
ref_channel5=data5['channel']
ref_channel4=data4['channel']
ref_tac5=data5['tac']
ref_tac4=data4['tac']
vc4=data4['value_coarse']
vc5=data5['value_coarse']
vf4=data4['value_fine']
vf5=data5['value_fine']
at=tdc['a'] #take the parameters needed of every channel 
bt=tdc['b']
ct=tdc['c']
dt=tdc['d']
aq=qdc['a']
bq=qdc['b']
cq=qdc['c']
dq=qdc['d']
eq=qdc['e']
tofpet4=data4['channel']
tofpet5=data5['channel']

fig1=plt.figure(1)
plt.title('hits_Tofpet_4')
plt.xlabel('Channels')
plt.ylabel('Hits')
plt.hist(tofpet4,bins=64)

fig2=plt.figure(2)
plt.title('hits_Tofpet_5')
plt.xlabel('Channels')
plt.ylabel('Hits')
plt.hist(tofpet5,bins=64)


def ftdc(tf, a, b, c, d):
  """ Returns the fine timestamp in units of the 160 MHz clock
  
  """
  
  res=(-b - np.sqrt(b**2 - 4*a*(c-tf)))/(2*a) + d
  return res
def fqdc(x, a, b, c, d, e):
  return - c * np.log(1 + np.exp(a*(x-e)**2 - b*(x-e))) + d

#Compute the charge distribution for tofpet 4
index_qdc_4=4*ref_channel4+ref_tac4
index_tdc_4=2*index_qdc_4
x4=vc4-ftdc(tf4,at[index_tdc_4].values,bt[index_tdc_4].values,ct[index_tdc_4].values,dt[index_tdc_4].values)
value_qdc4=(vf4+fqdc(x4,aq[index_qdc_4].values,bq[index_qdc_4].values,cq[index_qdc_4].values,dq[index_qdc_4].values,eq[index_qdc_4].values))/3.65
plot3=plt.figure(3)
plt.title('Charge_Tofpet_4')
plt.hist(value_qdc4,bins=100)

#Compute the charge distribution for tofpet 5
index_qdc_5=4*ref_channel5+ref_tac5
index_tdc_5=2*index_qdc_5
x5=vc5-ftdc(tf5,at[index_tdc_5].values,bt[index_tdc_5].values,ct[index_tdc_5].values,dt[index_tdc_5].values)
value_qdc5=(vf5+fqdc(x5,aq[index_qdc_5].values,bq[index_qdc_5].values,cq[index_qdc_5].values,dq[index_qdc_5].values,eq[index_qdc_5].values))/3.65
plot4=plt.figure(4)
plt.title('Charge_Tofpet_5')
plt.hist(value_qdc5,bins=100)
