import serial
import urllib.request

con = serial.Serial('COM5','9600')
print("id | kelembapan | suhu | wbgt | lux | co2 | kecepatan angin")
while(1):
	while(con.inWaiting()==0):
		pass
	s = str(con.readline(), "utf-8")
	data = s.split(";")
	if len(data) == 7:
		url = "http://localhost:3000/api/data/tambah/sensor/"+data[0]+"/data/"+data[1]+","+data[2]+","+data[3]+","+data[4]+","+data[5]+","+data[6]
		urllib.request.urlopen(url)
		print(data[0]+" | "+data[1]+" | "+data[2]+" | "+data[3]+" | "+data[4]+" | "+data[5]+" | "+data[6])
	else:
		pass