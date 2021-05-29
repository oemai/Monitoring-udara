import serial
import mysql.connector
import time
# global s1,s2,a2
dev=serial.Serial("/dev/ttyUSB0", baudrate=9600)
dev.flush()
lineA = []
lineB = []
lineC = []
lineD = []
lineE = []
lineF = []
line =[]

# one=dev.write(b'A')
# line=dev.readline()
# lineA=line.decode("ascii")
# print("Data Zahri: ",lineA)
# print(type(lineA))

# one=dev.write(b'B')
# line=dev.readline()
# lineA=line.decode("ascii")
# print("Data Afif: ",lineA)
# print(type(lineA))

db=mysql.connector.connect(host="localhost", user="root", passwd="", database="sensor_gas")   
mycursor = db.cursor()
while db.is_connected:
    # if dev.write(b'A'):
    one=dev.write(b'A')
    line=dev.readline()
    lineA=line.decode("ascii")
    print("Data Sensor 1: ",lineA)
    print(type(lineA))

    v1=int(lineA[0:4])
    v2=int(lineA[4:8])
    v3=int(lineA[8:12])
    v4=int(lineA[12:16])
    v5=int(lineA[16:20])
    v6=int(lineA[20:24])
    
    print("Data Sensor 1")
    print("Data[1]:",v1)
    print("Data[2]:",v2)
    print("Data[3]:",v3)
    print("Data[4]:",v4)
    print("Data[5]:",v5)
    print("Data[6]:",v6)
    print(type(v1))

    mycursor = db.cursor()
    mycursor.execute("INSERT INTO node1 (time,sensor_A,sensor_B,sensor_C,sensor_D,sensor_E,sensor_F) VALUES (now(),%i,%i,%i,%i,%i,%i)" % (v1,v2,v3,v4,v5,v6))
    db.commit()   
    print("{} Data Berhasil Ditambahkan".format(mycursor.rowcount))
    mycursor.close()
    time.sleep(5)


    one=dev.write(b'B')
    line=dev.readline()
    lineA=line.decode("ascii")
    print("Data Sensor 2 : ",lineA)
    print(type(lineA))

    v1=int(lineA[0:4])
    v2=int(lineA[4:8])
    v3=int(lineA[8:12])
    v4=int(lineA[12:16])
   
    print("Int")
    print("Data[1]:",v1)
    print("Data[2]:",v2)
    print("Data[3]:",v3)
    print("Data[4]:",v4)
    print(type(v1))

    mycursor = db.cursor()
    mycursor.execute("INSERT INTO node2 (time,speed,dust,temperature,humidity) VALUES (now(),%i,%i,%i,%i)" % (v1,v2,v3,v4))
    db.commit()   
    print("{} Data Berhasil Ditambahkan".format(mycursor.rowcount))
    mycursor.close()
    time.sleep(5)

  
