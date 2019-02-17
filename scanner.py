import socket
import threading
from os import system

total=0
th1=0
th2=0
th3=0
th4=0
rg=254
ipadd=[]
system("clear")
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n")
print("                RANGE SCANNER 0.1 \n")
print("                           Made by:- Sarthak Saini")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

print("enter the ip range xxx.xxx.xxx.<> leave the '<>' area example:- 192.168.0.")
ip=input(">")

for i in range(255):
    ipadd.append(ip+str(i))


print("[+] Ip range generated")



def makethread(count):
    global ipadd

    port=80
    temp=0

    if count==2:
        temp=count+65
        count=0

    else:
        temp=count+63


    while temp>count:
        ip=""
        sockets=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        ip=str(ipadd[count])

        if sockets.connect_ex((ip,port))==0:
            print("Ip--{} -- is alive on port {}".format(ip,port))
        sockets.close()

        count+=1




def main():
    global total,th1,th2,th3,th4,rg
    sockets=""
    total=int(254/4)
    th1=rg-total
    rg=rg-total
    th2=rg-total
    rg=rg-total
    th3=rg-total
    th4=th3-total


    print("[+] Threads initiated")
    p1 = threading.Thread(target=makethread,args=(th1,))
    p2 = threading.Thread(target=makethread,args=(th2,))
    p3 = threading.Thread(target=makethread,args=(th3,))
    p4 = threading.Thread(target=makethread,args=(th4,))
    print("[+] Process Started")
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("\n--------------------------------------------------\n")
    print("Scan Complete ....!! Sire ;)")

def start():
    try:
        main()
    except:
        print("\nwanna quit me press ctrl+c again to kill those threads !!")
        print("have a nice day sir (- _ ^)")

start()
