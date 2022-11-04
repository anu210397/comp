from geopy import distance
import requests
import pandas as pd
import csv
f1 = pd.read_csv('C:/Users/ECESIS/Desktop/miles/tax1.csv')
f2 = pd.read_csv('C:/Users/ECESIS/Desktop/miles/comp_dummy.csv')
matching_county = (f2[f2.county.isin(f1.county)])
#print(matching_county)
order = matching_county.reset_index(drop=True)
#print(order)
tax = f1.GLA
tax1 = int(tax)

print((tax1))
type(tax1)
df = order.astype({'GLA':'int'})
#print(df)
#print(df.dtypes)
#type(df)

if (1000 <tax1 <=1500) :
    
   
    GLA = (df[(df['GLA'] >1200)  & (df['GLA'] <= 1400)]) 
    #print(GLA)
    order_GLA = GLA.reset_index(drop=True)
    print(order_GLA)
elif (1500 <tax1 <=2500):

    GLA = (df[(df['GLA'] >1500)  & (df['GLA'] <= 2500)]) 
    #print(GLA)
    order_GLA = GLA.reset_index(drop=True)
    print(order_GLA)
    
else:
    print("none")
    
df_1 = order_GLA.astype({' Year_ Built':'int'})
yr_built = f1. Year_Built
year__built = int(yr_built)

print((year__built))
type(year__built)
if (1990 <year__built <=2000) :    
    YB = (df_1[(df_1[' Year_ Built'] >1990)  & (df_1[' Year_ Built'] <= 2000)]) 
    print(YB)
else:
    print("none")
    
YB.to_csv('C:/Users/ECESIS/Desktop/comp_selectio/comp.csv')