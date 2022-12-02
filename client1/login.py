 #import modules
 
from tkinter import *
import os
import pwreset

name=""
t=[0,name]

# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global usermail
    global password
    global username
    
    global usermail_entry
    global password_entry
    global username_entry
    
    usermail = StringVar()
    password = StringVar()
    username = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="cyan").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    usermail_lable = Label(register_screen, text="Email id(without domain name) * ")
    usermail_lable.pack()
    usermail_entry = Entry(register_screen, textvariable=usermail)
    usermail_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="cyan", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login",bg="cyan").pack()
    Label(login_screen, text="").pack()
 
    global usermail_verify
    global password_verify
 
    usermail_verify = StringVar()
    password_verify = StringVar()
 
    global usermail_login_entry
    global password_login_entry
 
    Label(login_screen, text="Email id(without domain name) * ").pack()
    usermail_login_entry = Entry(login_screen, textvariable=usermail_verify)
    usermail_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,bg="cyan", command = login_verify).pack()
    Button(login_screen, text="Forgot Password", width=15, height=1,command = forgot_password).pack()
 
# Implementing event on register button
 
def register_user():
 
    usermail_info = usermail.get()
    password_info = password.get()
    username_info = username.get()
    isFile = os.path.isfile("C:\\Users\\****\\Desktop\\python gui chatroom\\"+usermail_info)
    if isFile:
        mail_already_exists()
    else:
        file = open(usermail_info, "w")
        file.write(usermail_info + "\n")
        file.write(password_info + "\n")
        file.write(username_info )
        file.close()
        file = open("C:\\Users\\****\\Desktop\\python gui chatroom\\"+usermail_info, "w")
        file.write(usermail_info + "\n")
        file.write(password_info + "\n")
        file.write(username_info )
        file.close()
     
        usermail_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.delete(0, END)
     
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def mail_already_exists():
    global mail_already_exist_screen
    mail_already_exist_screen = Toplevel(register_screen)
    mail_already_exist_screen.title("Mail Exists")
    mail_already_exist_screen.geometry("200x100")
    Label(mail_already_exist_screen, text="This Email is already registered ", bg="cyan").pack()
    Button(mail_already_exist_screen, text="OK", command=mail_already_exist_screens).pack()
 

def pwres_user():
    
    global tomail
    global otp
    tomail=usermailpwr.get()
    isFile = os.path.isfile("C:\\Users\\****\\Desktop\\python gui chatroom\\"+tomail)
    if isFile:
        otp=pwreset.main(tomail)
        pwres_screen.destroy()
        
        global otp_screen
        otp__screen = Toplevel(main_screen)
        otp__screen.title("Enter OTP")
        otp__screen.geometry("300x250")
        
        global compareotp   
        global compareotp_entry

        compareotp  = StringVar()
     
        Label(otp__screen, text="Enter OTP:", bg="cyan").pack()
        Label(otp__screen, text="").pack()
        
        compareotp_lable = Label(otp__screen, text="OTP:")
        compareotp_lable.pack()
        compareotp_entry = Entry(otp__screen, textvariable=compareotp)
        compareotp_entry.pack()
        
        Label(otp__screen, text="").pack()
        Button(otp__screen, text="Reset Password", width=10, height=1, bg="cyan", command = getnewpw).pack()
    else:
        global wrmail_screen
        wrmail__screen = Toplevel(main_screen)
        wrmail__screen.title("Email not Registerd")
        wrmail__screen.geometry("300x150")
        
        global wrmail   
        global wrmail_entry

        wrotp= StringVar()
     
        Label(wrmail__screen, text="The Email you have entered is not Registered.", bg="cyan").pack()
        Label(wrmail__screen, text="").pack()
    
    
    
def getnewpw(): 
    newotp=compareotp.get()
    if(otp==newotp):
        global reset_screen
        reset__screen = Toplevel(main_screen)
        reset__screen.title("Password Reset")
        reset__screen.geometry("300x250")
        
        global newpw   
        global newpw_entry

        newpw = StringVar()
     
        Label(reset__screen, text="Enter New password:", bg="cyan").pack()
        Label(reset__screen, text="").pack()
        
        newpw_lable = Label(reset__screen, text="New Password")
        newpw_lable.pack()
        newpw_entry = Entry(reset__screen, textvariable=newpw)
        newpw_entry.pack()
        
        Label(reset__screen, text="").pack()
        Button(reset__screen, text="Reset Password", width=10, height=1, bg="cyan", command = newpw_user).pack()
    else:
        global wrotp_screen
        wrotp__screen = Toplevel(main_screen)
        wrotp__screen.title("Wrong OTP")
        wrotp__screen.geometry("300x250")
        
        global wrotp   
        global wrotp_entry

        wrotp= StringVar()
     
        Label(wrotp__screen, text="The OTP you have entered is wrong.", bg="cyan").pack()
        Label(wrotp__screen, text="").pack()
    
        
def newpw_user():
    newpassword=newpw.get()

    # open file in read mode
    file = open(tomail, "r")
    replaced_content = ""
    line_number = 2
    i = 1
    # looping through the file
    for line in file:
        
        # stripping line break
        line = line.strip()
        # replacing the text if the line number is reached
        if i == line_number:
            new_line = line.replace(line, newpassword)
        else:
            new_line = line
        # concatenate the new string and add an end-line break
        replaced_content = replaced_content + new_line + "\n"
        # Increase loop counter
        i = i + 1
        
    # close the file
    file.close()
    # Open file in write mode
    write_file = open(tomail, "w")
    # overwriting the old file contents with the new/replaced content
    write_file.write(replaced_content)
    # close the file
    write_file.close()
    ########reset_screen.destroy()
   
    
# Implementing event on login button 
 
def login_verify():
    usermail1 = usermail_verify.get()
    password1 = password_verify.get()
    usermail_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if usermail1 in list_of_files:
        file1 = open(usermail1, "r")
        verify = file1.readlines()
        if password1+"\n" ==verify[1]:
            global name
            name=verify[2]
            login_sucess()
            file1.close()
            
        else:
            password_not_recognised()
 
    else:
        user_not_found()
        
def forgot_password():
    global pwres_screen
    pwres_screen = Toplevel(main_screen)
    pwres_screen.title("Password Reset")
    pwres_screen.geometry("300x250")
    global usermailpwr
    
    global usermailpwr_entry

    usermailpwr = StringVar()
 
    Label(pwres_screen, text="Please enter details below", bg="cyan").pack()
    Label(pwres_screen, text="").pack()
    
    usermailpwr_lable = Label(pwres_screen, text="Email id(without domain name) * ")
    usermailpwr_lable.pack()
    usermailpwr_entry = Entry(pwres_screen, textvariable=usermailpwr)
    usermailpwr_entry.pack()
    
    Label(pwres_screen, text="").pack()
    Button(pwres_screen, text="Send OTP", width=10, height=1, bg="cyan", command = pwres_user).pack()
    
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    global t
    t=[1,name]
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("200x100")
    Label(user_not_found_screen, text="Enter valid EmailId ").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
    
def mail_already_exist_screens():
    mail_already_exist_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
def main():
    main_account_screen()
    return t