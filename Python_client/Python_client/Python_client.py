import socket
import random
from tkinter import *

def send_request():

    clients_input=E1.get()
    soc.send(clients_input.encode("utf8"))
    B2['state']='normal'

    pass

def recive_request():
    result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
    result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode
    var.set(result_string)
    B2['state']='disabled'
    pass


def exit_button():
    top.destroy()

def enterB(event):
    B.configure( bg="#313a43")

def leaveB(event):
    B.configure(bg="#0bb697")


IP_ADDRES = '89.40.126.143'
PORT = 12345

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind(('',PORT))
soc.connect((IP_ADDRES, 12345))

welcom_message = soc.recv(4096) # the number means how the response can be in bytes  
result_string = welcom_message.decode("utf8") # the return will be in bytes, so decode

top = Tk()
top.resizable(width=False, height=False)
top.geometry("500x500")
background_image = PhotoImage(file ="seigaiha.png")
bg_image = Label( top,image=background_image, bd="0px" )
bg_image.pack()
bg_image.place(x=0,y=0)
var = StringVar()
label = Label( top, textvariable=var, relief=RAISED, bd="0px" )
label.pack()
label.place(x=70,y=300)

message = StringVar()
label2 = Label( top, textvariable=message, relief=RAISED, bd="0px" )
message.set(result_string)
label2.pack()
label2.place(x=300,y=20)



L1 = Label(top, text="Input")
L1.pack( side = LEFT)
L1.place(x=40,y=20)

E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
E1.insert(END, 'N')
E1.place(x=80,y=20)

B = Button(top,font="Arial 8 bold ",foreground="white", text ="Send Request",highlightcolor="red",bd=1,highlightbackground="red",activebackground="#313a43", bg="#0bb697",command =send_request)
B.place(x=100,y=100)
B2 = Button(top, text ="Show answer", command = recive_request)
B2.place(x=200,y=100)
B3 = Button(top,font="Arial 12 bold", text ="Exit", command = exit_button, padx=10, pady=1)
B3.place(x=400,y=400)

B.bind('<Enter>', enterB)
B.bind('<Leave>', leaveB)
if (result_string == 'stop'):
    soc.close()


#while (result_string != 'stop'):
#    clients_input = input(format(welcom_message.decode("utf8")))  
#    soc.send(clients_input.encode("utf8")) # we must encode the string to bytes  
#    result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
#    result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode
    

#    print("Result from server is \n {}".format(result_string))  
#    if(result_string == 'stop'):
#        soc.close()
top.mainloop()

