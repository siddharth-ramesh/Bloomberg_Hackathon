import socket
import sys

def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
    finally:
        sock.close()

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\nSUBSCRIBE\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
    finally:
        sock.close()


#OURCODE STARTS HERE:
#this is our username and password
login_user,login_pass = "Here_for_Beer","johnsmith"
#runs any input, this is a placeholder for quick functions
def runthis(input):
   return run(login_user,login_pass,input)

#returns how much cash we have
def cash():
    return  run(login_user,login_pass,"MY_CASH")

#return our shares
def our_shares():
    return  run(login_user,login_pass,"MY_SECURITIES")

#BID <ticker> <price> <shares>
def buy(ticker,price,shares):
   return run(login_user,login_pass,"BID "+str(ticker)+" "+ str(price)+" "+str(shares))

#ASK <ticker> <price> <shares>
def sell(ticker,price,shares):
   return run(login_user,login_pass,"ASK "+str(ticker)+" "+ str(price)+" "+str(shares))



#testywesty