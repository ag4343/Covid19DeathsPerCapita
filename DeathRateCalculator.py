
f1=open('Apr29-total-covid-deaths-per-million.csv', 'r')
L1=f1.readlines()
f1.close
L2=L1[1:]



countries=[]
for line in L2:
	if line.split(',')[0] not in countries:
		countries.append(line.split(',')[0])


DeathRate=[]
for i in countries:
	list1=[]
	for line in L2:
		if line.split(',')[0] == i and line.split(',')[2] == '"Apr 20':
                    list1.append(i)
                    list1.append(float(line.split(',')[4]))
	DeathRate.append(list1)

def custom_sort(DeathRate):
    return DeathRate[1]

DeathRate.sort(key=custom_sort, reverse=True)


Dictionary={}
for i in DeathRate:
    Dictionary[i[0]]=i[1]

count=0
for i in Dictionary:
        if i != 'San Marino' and i != 'Andorra' and i != 'Sint Maarten (Dutch part)' and i != 'Europe': 
                count=count+1
                print('%-3s %-35s %f' %(count,i, Dictionary[i]))




