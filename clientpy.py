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

#runs any input, this is a placeholder for quick functions
def runthis(input):
   return run("Here_for_Beer","johnsmith",input)

#BID <ticker> <price> <shares>
def buy(ticker,price,shares):
   return run("Here_for_Beer","johnsmith","BID "+str(ticker)+" "+ str(price)+" "+str(shares))

#ASK <ticker> <price> <shares>
def sell(ticker,price,shares):
   return run("Here_for_Beer","johnsmith","ASK "+str(ticker)+" "+ str(price)+" "+str(shares))

#testywesty