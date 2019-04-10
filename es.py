
import requests
CC=0
a=requests.post("http://192.168.1.231:8080/accreditamento", json={"nome":"Riccardo Consiglio"})

#1
y=requests.get("http://192.168.1.231:8080/esercizi/1", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=d.lower()
a=requests.post("http://192.168.1.231:8080/esercizi/1", json={"data":res})
CC+=1
print(CC)
print(a.json())

#2
y=requests.get("http://192.168.1.231:8080/esercizi/2", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=d*d
a=requests.post("http://192.168.1.231:8080/esercizi/2", json={"data":res})
CC+=1
print(CC)
print(a.json())

#3
y=requests.get("http://192.168.1.231:8080/esercizi/3", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=d["cognome"]
a=requests.post("http://192.168.1.231:8080/esercizi/3", json={"data":res})
CC+=1
print(CC)
print(a.json())

#4
y=requests.get("http://192.168.1.231:8080/esercizi/4", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=len(d)
a=requests.post("http://192.168.1.231:8080/esercizi/4", json={"data":res})
CC+=1
print(CC)
print(a.json())

#5
y=requests.get("http://192.168.1.231:8080/esercizi/5", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d:
	res.append(i.upper())
a=requests.post("http://192.168.1.231:8080/esercizi/5", json={"data":res})
CC+=1
print(CC)
print(a.json())

#6
y=requests.get("http://192.168.1.231:8080/esercizi/6", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=sum(d)
a=requests.post("http://192.168.1.231:8080/esercizi/6", json={"data":res})
CC+=1
print(CC)
print(a.json())

#7
y=requests.get("http://192.168.1.231:8080/esercizi/7", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=0
for i in d:
	if i > 5:
		res+=i
a=requests.post("http://192.168.1.231:8080/esercizi/7", json={"data":res})
CC+=1
print(CC)
print(a.json())

#8
y=requests.get("http://192.168.1.231:8080/esercizi/8", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=0
for i in range(len(d)):
	if i%2 == 0:
		res += d[i]
a=requests.post("http://192.168.1.231:8080/esercizi/8", json={"data":res})
CC+=1
print(CC)
print(a.json())

#9
y=requests.get("http://192.168.1.231:8080/esercizi/9", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=0
for i in d:
	if i%2!=0:
		res+=i
a=requests.post("http://192.168.1.231:8080/esercizi/9", json={"data":res})
CC+=1
print(CC)
print(a.json())

#10
y=requests.get("http://192.168.1.231:8080/esercizi/10", headers={"x-data": "true"})
c=y.json()
d=c["data"]
d.sort()
a=requests.post("http://192.168.1.231:8080/esercizi/10", json={"data":d})
CC+=1
print(CC)
print(a.json())

#11
y=requests.get("http://192.168.1.231:8080/esercizi/11", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d:
	res.append(i.lower())
res.sort()
a=requests.post("http://192.168.1.231:8080/esercizi/11", json={"data":res})
CC+=1
print(CC)
print(a.json())

#12
y=requests.get("http://192.168.1.231:8080/esercizi/12", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d:
	i=i-1
	res.append(i)
a=requests.post("http://192.168.1.231:8080/esercizi/12", json={"data":res})
CC+=1
print(CC)
print(a.json())

#13
y=requests.get("http://192.168.1.231:8080/esercizi/13", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in len(d):
	if i==len(d):
		res.append(d[i])
	else:
		res.append(d[i]+d[i+1]):
a=requests.post("http://192.168.1.231:8080/esercizi/13", json={"data":res})
CC+=1
print(CC)
print(a.json())

#14
y=requests.get("http://192.168.1.231:8080/esercizi/14", headers={"x-data": "true"})
c=y.json()
d=c["data"]
p=0
n=0
z=0
for i in d:
	if i > 0:
		p+=1
	elif i == 0:
		z+=1
	else:
		n+=1
res={
	"positivi":p,
	"negativi":n,
	"zeri":z}
a=requests.post("http://192.168.1.231:8080/esercizi/14", json={"data":res})
CC+=1
print(CC)
print(a.json())

#15
y=requests.get("http://192.168.1.231:8080/esercizi/15", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d:
	if len(i)%2==0:
		res.append(i.upper())
	else:
		res.append(i.lower())
a=requests.post("http://192.168.1.231:8080/esercizi/15", json={"data":res})
CC+=1
print(CC)
print(a.json())

#16
y=requests.get("http://192.168.1.231:8080/esercizi/16", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=""
counter=0
for i in d:
	counter+=1
	if counter==len(d):
		res+=i
	else:
		res+=i+" "
a=requests.post("http://192.168.1.231:8080/esercizi/16", json={"data":res})
CC+=1
print(CC)
print(a.json())

#17
y=requests.get("http://192.168.1.231:8080/esercizi/17", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=""
for i in d:
	res+=i[-1]
a=requests.post("http://192.168.1.231:8080/esercizi/17", json={"data":res})
CC+=1
print(CC)
print(a.json())

#18
y=requests.get("http://192.168.1.231:8080/esercizi/18", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=""
for i in d:
	if len(i)>4:
		res+=i[0]
a=requests.post("http://192.168.1.231:8080/esercizi/18", json={"data":res})
CC+=1
print(CC)
print(a.json())

#19
y=requests.get("http://192.168.1.231:8080/esercizi/19", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in range(d+1):
	if d%i==0:
		res.append(i)
res.sort()
a=requests.post("http://192.168.1.231:8080/esercizi/19", json={"data":res})
CC+=1
print(CC)
print(a.json())

#20
DA FARE
'''
y=requests.get("http://192.168.1.231:8080/esercizi/20", headers={"x-data": "true"})
c=y.json()
d=c["data"]

a=requests.post("http://192.168.1.231:8080/esercizi/20", json={"data":res})
CC+=1
print(CC)
print(a.json())
'''

#21
y=requests.get("http://192.168.1.231:8080/esercizi/21", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d:
	if i<=5:
		res.append(i)
a=requests.post("http://192.168.1.231:8080/esercizi/21", json={"data":res})
CC+=1
print(CC)
print(a.json())

#22
y=requests.get("http://192.168.1.231:8080/esercizi/22", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d:
	if i >=3 and i<=6:
		res.append(i)
a=requests.post("http://192.168.1.231:8080/esercizi/22", json={"data":res})
CC+=1
print(CC)
print(a.json())

#23
DA FARE
'''
y=requests.get("http://192.168.1.231:8080/esercizi/23", headers={"x-data": "true"})
c=y.json()
d=c["data"]

a=requests.post("http://192.168.1.231:8080/esercizi/23", json={"data":res})
CC+=1
print(CC)
print(a.json())
'''

#24
DA FARE
'''
y=requests.get("http://192.168.1.231:8080/esercizi/24", headers={"x-data": "true"})
c=y.json()
d=c["data"]

a=requests.post("http://192.168.1.231:8080/esercizi/24", json={"data":res})
CC+=1
print(CC)
print(a.json())
'''

#25
y=requests.get("http://192.168.1.231:8080/esercizi/25", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=0
for i in d:
	for x in i:
		if x=="a":
			res+=1
a=requests.post("http://192.168.1.231:8080/esercizi/25", json={"data":res})
CC+=1
print(CC)
print(a.json())

#26
y=requests.get("http://192.168.1.231:8080/esercizi/26", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d:
	res.append(i-i*2)
a=requests.post("http://192.168.1.231:8080/esercizi/26", json={"data":res})
CC+=1
print(CC)
print(a.json())

#27
y=requests.get("http://192.168.1.231:8080/esercizi/27", headers={"x-data": "true"})
c=y.json()
d=c["data"]
res=[]
for i in d["negozio"]:
	res.append(i)
for i in d["magazzino"]:
	if i not in res:
		res.append(i)
a=requests.post("http://192.168.1.231:8080/esercizi/27", json={"data":res})
CC+=1
print(CC)
print(a.json())

#28
y=requests.get("http://192.168.1.231:8080/esercizi/28", headers={"x-data": "true"})
c=y.json()
d=c["data"]
prod=[]
num=[]
for i in d["negozio"]:
	if i not in prod:
		prod.append(i)
for i in prod:
	n=d["negozio"].count(i)
	m=d["magazzino"].count(i)
	num.append(n+m)
tupl=zip(prod, num)
res=dict(tupl)
a=requests.post("http://192.168.1.231:8080/esercizi/28", json={"data":res})
CC+=1
print(CC)
print(a.json())

#29
 DA FARE
 '''
y=requests.get("http://192.168.1.231:8080/esercizi/29", headers={"x-data": "true"})
c=y.json()
d=c["data"]
f=d

a=requests.post("http://192.168.1.231:8080/esercizi/29", json={"data":res})
CC+=1
print(CC)
print(a.json())
'''

#30
DA FARE
'''
y=requests.get("http://192.168.1.231:8080/esercizi/30", headers={"x-data": "true"})
c=y.json()
d=c["data"]
f=d

a=requests.post("http://192.168.1.231:8080/esercizi/30", json={"data":res})
CC+=1
print(CC)
print(a.json())


























