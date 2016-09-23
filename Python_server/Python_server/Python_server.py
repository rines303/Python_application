# server.py
import time
from threading import Thread
import threading 
import os
import sys
from time import sleep

IP_ADDRES = '89.40.126.143'

#-------------------------------------------------------------
#                       PROGRESS BAR
#-------------------------------------------------------------
# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr       = "{0:." + str(decimals) + "f}"
    percents        = formatStr.format(100 * (iteration / float(total)))
    filledLength    = int(round(barLength * iteration / float(total)))
    bar             = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()
def start_bar():
    # 
    # Sample Usage
    # 
    # make a list
    items = list(range(0, 10))
    i     = 0
    l     = len(items)
        
    # Initial call to print 0% progress
    printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
    for item in items:
        # Do stuff...
        sleep(1)
        # Update Progress Bar
        i += 1
        printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)



#-------------------------------------------------------------------------------
#              THREAD TO SHOW TEXT ABOUT WAITING FOR NEW REQUEST
#-------------------------------------------------------------------------------

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        show()
def show():
    os.system('clear')
    global exitFlag
    while exitFlag:
        time.sleep(1)
        print ("Waiting for new request... ")
        time.sleep(1)
        os.system('clear')
    accept(ip,port)

def accept(_ip, _port):
    print('Accepting connection from ' + _ip + ':' + _port+ ' Time:  '+ time.ctime())

#-------------------------------------------------------------------------------
#                   NGINX STATUS SEND TO CLIENT
#-------------------------------------------------------------------------------
def nginx_status_send(conn):
    p = os.popen('sudo service nginx status | grep "active " | cut -c -27',"r")
    out = ''
    while 1:
       line = p.readline()
       if not line: break
       out+=line

   # print("Result of processing {} is: {}".format(input_from_client, out))

    vysl = out.encode("utf8")  # encode the result string
    conn.sendall(vysl)  # send it to client
    
#-------------------------------------------------------------------------------
#                   QUIT SEND TO CLIENT
#-------------------------------------------------------------------------------
def quit_send(conn):
    end_message = "stop"
    encode = end_message.encode("utf8")  # encode the result string
    conn.sendall(encode)  # send it to client
    conn.close()  # close connection
    print('Connection ' + ip + ':' + port + " ended")
    time.sleep(5)

    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)

    # Start new Threads
    thread1.start()
    global exitFlag
    exitFlag = 1
#-------------------------------------------------------------------------------
#                         DATE SEND TO CLIENT
#-------------------------------------------------------------------------------

def date_send(conn):
    p = os.popen('date',"r")
    out = ''
    while 1:
       line = p.readline()
       if not line: break
       out+=line
   # print("Result of processing {} is: {}".format(input_from_client, out))

    vysl = out.encode("utf8")  # encode the result string
    conn.sendall(vysl)  # send it to client


#-------------------------------------------------------------------------------------
#          RESPOND TO CLIENT AND CLOSE TE CONNECTION AND RUN 'WAITING' TEXT
#-------------------------------------------------------------------------------------

def client_thread(conn, ip, port,  MAX_BUFFER_SIZE = 4096):
   
    welcome_message = "What do you want to do?? \n Select:\n 'N' => Nginx status. \n 'D' => Actual Date. \n 'Q' => Quit connect. \n : "
    encode = welcome_message.encode("utf8")  # encode the result string
    conn.sendall(encode)  # send it to client

    while True:

        # the input is in bytes, so decode it
        input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

        # MAX_BUFFER_SIZE is how big the message can be
        # this is test if it's sufficiently big
        siz = sys.getsizeof(input_from_client_bytes)
        if  siz >= MAX_BUFFER_SIZE:
            print("The length of input is probably too long: {}".format(siz))

        # decode input and strip the end of line
        input_from_client = input_from_client_bytes.decode("utf8").rstrip()
        if ((input_from_client == 'n') | (input_from_client == 'N')):
              nginx_status_send(conn)
        elif ((input_from_client == 'q') | (input_from_client == 'Q')):
            quit_send(conn)
            break
        elif ((input_from_client == 'd') | (input_from_client == 'D')):
               date_send(conn)
        else:
            message = "\n Wrong command!!! \n"
            encode = message.encode("utf8")  # encode the result string
            conn.sendall(encode)  # send it to client


         ######## start progress bar #####
       # start_bar() <-----
#--------------------------------------------------------------------------
#    START SERVER, CREATE SOCKET, BIND AND START LISTENING
#--------------------------------------------------------------------------
def start_server():

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        #SOCKET IP AND PORT
        soc.bind((IP_ADDRES, 12345))

        print('Socket bind complete')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    print('Socket now listening')

    # this will make an infinite loop needed for 
    # not reseting server for every client
    while True:  
        conn, addr = soc.accept()
        global ip, port, exitFlag
        ip, port = str(addr[0]), str(addr[1])
        exitFlag = 0
        if (port == '12345'):
            accept(ip, port)
            try:
               Thread(target=client_thread, args=(conn, ip, port)).start()
            except:
               print("Terible error!")
               import traceback
               traceback.print_exc()
    soc.close()


print ("Start : %s" % time.ctime())
start_server() 
    

