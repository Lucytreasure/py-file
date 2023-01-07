import pandas as pd
import matplotlib.pyplot as plt

growdata = pd.read_csv('GrowLocations.csv')

lgrowdata = growdata[['Latitude','Longitude']]

bi_growdata = lgrowdata.loc[(lgrowdata['Longitude']>=50.681) & (lgrowdata['Latitude']>=-10.592)]
bi_growdata = bi_growdata.loc[(bi_growdata['Longitude']<=57.985) & (bi_growdata['Latitude']<=1.6848)]


a = bi_growdata['Longitude']
b = bi_growdata['Latitude']

figure, za = plt.subplots()
za.scatter(b,a)
firstmap = plt.imread('map7.png')
za.imshow(firstmap, extent=(-10,1.7,50,57))
figure.savefig('newMap.png')