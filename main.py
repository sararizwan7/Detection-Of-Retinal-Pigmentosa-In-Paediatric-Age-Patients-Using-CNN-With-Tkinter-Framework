import email
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import cv2
import imageio
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tkinter as tk, threading
from tkinter.filedialog import askopenfile 
from tkinter import messagebox
import tensorflow as tf
import glob
import numpy as np
from tensorflow.keras.preprocessing import image
import tkinter
import os
from tkinter import *
import matplotlib.pyplot as plt    
from PIL import Image, ImageTk


f = ('Times', 14)

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text, 
                    password text
                )
            ''')
con.commit()
            


from PIL import Image, ImageTk
path_to_model = r'A:/TechieYan projects/MIX/Completed/Detection of Retinal pigmentosa in paediatric age patients using CNN with Tkinter Framework/model/cnn_model.hdf5'
model = tf.keras.models.load_model(path_to_model)
print(model)


ws = Tk()
ws.title('Login Page')
ws.geometry('940x500')
ws.config(bg='#0B5A81')
Label(text="Detection of Genetic Retinal Diseases in Pidiatric age using CNN", bg="green",fg="white", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()


def insert_record():
    check_counter=0
    warn = ""
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1
    
    print(check_counter)
    if check_counter == 5:        
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            print(register_name.get(), register_email.get(), register_pwd.get())
            cur.execute("INSERT INTO record VALUES (:name, :email, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'password': register_pwd.get()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('deks', ep) 
    else:
        messagebox.showerror('Error', warn)



def login_response():

    global username
    global pwd

    uname = email_tf.get()
    upwd = pwd_tf.get()

    
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        c.execute("SELECT * FROM record where name=? AND password=?",(uname, upwd))
        row = c.fetchone()
        username = row[0]
        print(username)
        pwd = row[2]
        print(pwd)
        
    except Exception as ep:
        messagebox.showerror('Wrong Entry', 'invalid username or password')

    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            global doc_login_sucess_screen 
            doc_login_sucess_screen = Toplevel(ws)
            doc_login_sucess_screen.title("Success")
            doc_login_sucess_screen.geometry("150x100")
            Label(doc_login_sucess_screen, text="Login Success").pack()
            Button(doc_login_sucess_screen, text="OK", command=doc_final_login).pack()
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('Please Enter Correct Details', warn)



file_path = ""
def open_file():
    global file_path
    file_path = askopenfile(mode='r', filetypes=[('Files', '*.*')])
    #print(file_path.name)
    if file_path is not None:
        pass



def uploadFiles():
    pb1 = Progressbar(
            doc_final_login_screen, 
            orient=HORIZONTAL, 
            length=300, 
            mode='determinate'
            )
    pb1.pack()
    for i in range(5):
        doc_final_login_screen.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(doc_final_login_screen, text='File Uploaded Successfully!', foreground='green').pack()
    
    
def save_file():
    #print(file_path.name)
    _dRawMap = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}

    def getRawGotStr(s):
        return r''.join( [ _dRawMap.get( ord(c), c ) for c in s ] )

    path = getRawGotStr(file_path.name) #This is your image file path
    #print("os ",path) 

    image_path = path
    #print(image_path)
    imagee = imageio.get_reader(image_path)
    #print(video)

    def stream(label):
        for image in imagee.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

    if __name__ == "__main__":

        my_label = tk.Label(doc_final_login_screen)
        my_label.pack()
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()


    #print("Final", path)

    #test_image = image.load_img(path)
    test_image = plt.imread(path)
    test_image = cv2.resize(test_image, (64, 64))
    test_image = img_to_array(test_image)
    #print(test_image)
    test_image = np.expand_dims(test_image, axis = 0)


    
    prediction = model.predict(test_image)
    if int(prediction[0][0]) == 0:
        print("NO")
        messagebox.showinfo("Result","The Person is not having Retinitis Pigmentosa")
    else:
        print("YES")
        messagebox.showerror("Result","The Person is affected with Retinitis Pigmentosa")




def doc_final_login():
    global doc_final_login_screen
    doc_login_sucess_screen.destroy()
    doc_final_login_screen = Toplevel(ws)
    doc_final_login_screen.title("User's Screen") 
    doc_final_login_screen.geometry("1600x900")
    photo = PhotoImage(file = r'A:/TechieYan projects/MIX/Completed/Detection of Retinal pigmentosa in paediatric age patients using CNN with Tkinter Framework/bg.png')
    label1 = tkinter.Label(doc_final_login_screen,image=photo)
    label1.image = photo
    label1.place(x=10, y=10)


    Label(doc_final_login_screen, text="Please choose from the option below").pack()
    Label(doc_final_login_screen, text="").pack()
     
    Button(doc_final_login_screen, text="Choose File", width=10, height=1, command =open_file).pack()
    Label(doc_final_login_screen, text="").pack()
    
    Button(doc_final_login_screen, text="Upload", width=10, height=1,command=uploadFiles).pack()
    Label(doc_final_login_screen, text="").pack()
    
    Button(doc_final_login_screen, text="Click for Prediction", width=15, height=1, command = save_file).pack()
    Label(doc_final_login_screen, text="").pack()




# widgets
left_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    left_frame, 
    text="Enter Username", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame, 
    font=f
    )

pwd_tf = Entry(
    left_frame, 
    font=f,
    show='*'
    )

login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=login_response
    )




right_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    right_frame, 
    text="Enter Name", 
    bg='#CCCCCC',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)


Label(
    right_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)



register_name = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f
    )



register_pwd = Entry(
    right_frame, 
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)


# widgets placement
email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)


# infinite loop
ws.mainloop()