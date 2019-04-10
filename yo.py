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








