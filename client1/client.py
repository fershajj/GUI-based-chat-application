import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
import login
import sys
import os
from tkinter import *

HOST='***********'
PORT=9999

class Client:
    
    def __init__(self,host,port):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))
        
        #messge box popup to enter username
        msg=tkinter.Tk()
        msg.withdraw()
        
        self.nickname=name
        
        self.gui_done=False
        self.running= True
        self.file="filename"
        gui_thread=threading.Thread(target=self.gui_loop)
        receive_thread=threading.Thread(target=self.receive)
        #file_thread=threading.Thread(target=self.file)
        gui_thread.start()
        receive_thread.start()
        #file_thread.start()
        
    def gui_loop(self):
        self.win=tkinter.Tk()
        self.win.configure(bg="black")
        self.win.title('           ~~~CHITTER-CHATTER~~~')
        self.win.geometry('400x800')
        
        #check users online
        self.send_button=tkinter.Button(self.win,text="users online*",command=self.online,bg="lightgreen")
        self.send_button.config(font=("Comic Sans MS",9))
        self.send_button.pack(padx=17,pady=4)
        #delete chat
        self.del_button=tkinter.Button(self.win,text="Clear Chat",command=self.deltext,bg="lightgreen")
        self.del_button.config(font=("Comic Sans MS",9))
        self.del_button.pack(padx=17,pady=4)
        
        self.chat_label=tkinter.Label(self.win,text="CHAT",width=70,bg='navajowhite')
        self.chat_label.config(font=("Verdana",13))
        self.chat_label.pack(padx=22,pady=7)
        
        #for textbox with chat history
        self.text_area=tkinter.scrolledtext.ScrolledText(self.win,height=16,bg="lemonchiffon")
        self.text_area.pack(padx=20,pady=5)
        #disabled mode so that chat history cannot be edited
        self.text_area.config(state='disabled')
        isfile=os.path.isfile('chat_history.txt')
        if isfile:
            file=open('chat_history.txt','r')
            for i in file:
                self.text_area.config(state='normal')
                #to append message at the end
                self.text_area.insert('end',i)
                #to keep the msg view to the end/last msg
                self.text_area.yview('end')
                self.text_area.config(state='disabled')
            file.close()
        
        
        self.msg_label=tkinter.Label(self.win,text="SEND MESSAGE",width=70,bg='navajowhite')
        self.msg_label.config(font=("Verdana",13))
        self.msg_label.pack(padx=22,pady=7)
        
        #for text area with input
        self.input_area=tkinter.Text(self.win,height=3,bg='gainsboro')
        self.input_area.pack(padx=20,pady=5)
        
        #send message button
        self.send_button=tkinter.Button(self.win,text="Send Message->",command=self.write,bg="cyan")
        self.send_button.config(font=("Comic Sans MS",10))
        self.send_button.pack(padx=17,pady=5)
        
        self.msg_label=tkinter.Label(self.win,text="SEND FILE",width=70,bg='navajowhite')
        self.msg_label.config(font=("Verdana",13))
        self.msg_label.pack(padx=22,pady=7)
        
        #send file button
        self.send_button=tkinter.Button(self.win,text="Send file->",command=self.filewrite,bg="cyan")
        self.send_button.config(font=("Comic Sans MS",10))
        self.send_button.pack(padx=17,pady=5)
        
        #indicates creating gui is done
        self.gui_done=True
        
        #to terminate program on closing chat window
        self.win.protocol("WM_DELETE_WINDOW",self.stop)
        
        self.win.mainloop()
       
    def deltext(self):
        self.text_area.config(state='normal')
        self.text_area.delete('1.0','end')
        self.text_area.config(state='disabled')
        isfile=os.path.isfile("chat_history.txt")
        if isfile:
            os.remove("chat_history.txt")
        
    def online(self):
        l=open(r'C:/Users/FERSHA/Desktop/python gui chatroom/server/online.txt')
        onln=l.readlines()
        t=[]
        for k in onln:
            t.append(k)
        self.win2=tkinter.Tk()
        self.win2.configure(bg="black")
        self.win2.title('           ~~~Users Online~~~')
        self.win2.geometry('300x200')
        self.text1_area=tkinter.scrolledtext.ScrolledText(self.win2,bg="#DFF6FF")
        self.text1_area.pack(padx=20,pady=5)
        self.text1_area.config(state='disabled')
        self.text1_area.config(state='normal')
        for i in t:
            self.text1_area.insert('end',i)
        self.text1_area.config(state='disabled')
        
    def write(self):
        #get text from message box and send it to server and clear message box
        #to go through the start till end of text
        message=f"{self.nickname}:{self.input_area.get('1.0','end')}"
        print(message)
        self.sock.send(message.encode('utf-8'))
        #to clear text box
        self.input_area.delete('1.0','end')
        
    def filewrite(self):
        self.win1=tkinter.Tk()
        self.win1.configure(bg="black")
        self.win1.title('           ~~~sendfile~~~')
        self.win1.geometry('300x200')
        self.sfinput_area=tkinter.Text(self.win1,height=3,bg="#DFF6FF")
        self.sfinput_area.pack(padx=20,pady=5)
        
        #send file button
        self.sendfile_button=tkinter.Button(self.win1,text="Send file->",command=self.filewrites,bg="cyan")
        self.sendfile_button.config(font=("Comic Sans MS",12))
        self.sendfile_button.pack(padx=20,pady=5)
   
    def filewrites(self):
        t=self.sfinput_area.get("1.0",'end-1c')
        isfile=os.path.isfile(t)
        if isfile:
            file=open(t)
            data = file.read()
         
            """ Sending the filename to the server. """
    #        self.sock.send("yt.txt".encode('utf-8'))
            message=f"{self.nickname}:"+data+"\n"
            """ Sending the file data to the server. """
            self.sock.send(message.encode('utf-8'))
            """ Closing the file. """
            file.close()
        else:
            self.mail_already_exist_screen=tkinter.Tk()
            self.mail_already_exist_screen.title("File not found")
            self.mail_already_exist_screen.geometry("200x100")
            Label(self.mail_already_exist_screen, text="The given file is not found", bg="cyan").pack()
        
    def stop(self):
        self.running=False
        self.win.destroy()
        self.sock.close()
        exit(0)
        
    def receive(self):
        while self.running:
            try:
                message=self.sock.recv(1024).decode('utf-8')
                if message =="NICK":
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        file=open('chat_history.txt','a')
                        file.write(message + "\n")
                        file.close()
                        self.text_area.config(state='normal')
                        #to append message at the end
                        self.text_area.insert('end',message)
                        #to keep the msg view to the end/last msg
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break


    
t=login.main()
global name
name=t[1]
if t[0]==1:
    client=Client(HOST,PORT)

