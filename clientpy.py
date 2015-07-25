import socket
import sys

def run(user, password, *commands):
    global line
    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"
    lines = []
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            line = rline.strip()
            lines.append(line)
            print(line)
            rline = sfile.readline()
    finally:
        sock.close()

    return lines

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


#OURCODE STARTS
#this is our username and password
login_user,login_pass = "Here_for_Beer","johnsmith"

#runs any input, this is a placeholder for quick functions
def runthis(input):
   return run(login_user,login_pass,input)

#1 returns how much cash we have
def cash():
    return  run(login_user,login_pass,"MY_CASH")

#2 return our shares
def our_shares():
    return  run(login_user,login_pass,"MY_SECURITIES")

#3 our current sell and buy orders with number of shares and price per
def orders():
    return  run(login_user,login_pass,"MY_ORDERS")

#4 Out all securities on exchange
def securities():
    return  run(login_user,login_pass,"SECURITIES")

#5 list all orders on exchange for a ticker
def orders(ticker):
    return  run(login_user,login_pass,"ORDERS "+str(ticker))

#6 BID <ticker> <price> <shares>
def buy(ticker,price,shares):
   return run(login_user,login_pass,"BID "+str(ticker)+" "+ str(price)+" "+str(shares))

#7 ASK <ticker> <price> <shares>
def sell(ticker,price,shares):
   return run(login_user,login_pass,"ASK "+str(ticker)+" "+ str(price)+" "+str(shares))

#8 clears your bid(buy)
def clear_bid(ticker):
    return run(login_user,login_pass,"CLEAR_BID "+str(ticker))

#9 clears your ask(sell)
def clear_ask(ticker):
    return run(login_user,login_pass,"CLEAR_ASK "+str(ticker))

#10 close the connection "gracefully"
def close_connection():
    run(login_user,login_pass,"CLOSE_CONNECTION")
    print("The connection was closed gracefully")

def start_parsing():
    allSecurities = str( securities() )

lines = securities()
print(lines)