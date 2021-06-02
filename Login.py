from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Log in")
root.geometry("300x400")
root.config(bg="#969db0")
root.resizable(0, 0)

frame1 = Frame(root, width=260, height=220)
frame1.place(x=20, y=20)

frame2 = Frame(root, width=200, height=100, bg="black")
frame2.place(x=50, y=260)

ltitle = Label(frame1, text="Log in to your account")
ltitle.place(x=56, y=5)

lname = Label(frame1, text="Enter username")
lname.place(x=75, y=50)
name = Entry(frame1)
name.place(x=50, y=70)

lpassw = Label(frame1, text="Enter password")
lpassw.place(x=75, y=110)
passw = Entry(frame1, show="*")
passw.place(x=50, y=130)


def logginbutton():
    users = {"Zaid": "12345", "Aaliyah": "23456", "Lihle": "34567", "Thabo": "45678", "Zoe": "56789"}
    user = list(users.keys())
    passws = list(users.values())
    found = False
    for x in range(len(users)):
        if name.get() == user[x] and passw.get() == passws[x]:
            found = True
    if found is True:
        frame2.config(bg="#45fe39")
        access.config(bg="#45fe39", text="")
        messagebox.showinfo("Status", "Access Granted")
        root.destroy()
        import newscreen
    else:
        if name.get() not in users:
            frame2.config(bg="red")
            access.config(bg="red")
            messagebox.showerror("Access Denied", "Unknown user.")
        else:
            frame2.config(bg="red")
            access.config(bg="red")
            messagebox.showerror("Access Denied", "Invalid username or password.")

"""def loginbutton():
    usernames = ["Zaid", "Aaliyah", "Lihle", "Thabo", "Zoe"]
    passwords = ["0", "1", "2", "3", "4"]
    found = False
    for x1 in range(len(usernames)):
        if name.get() == usernames[x1] and passw.get() == passwords[x1]:
            found = True
    if found is True:
        frame2.config(bg="#45fe39")
        access.config(bg="#45fe39", text="")
        messagebox.showinfo("Status", "Access Granted")
        root.destroy()
        import newscreen

    elif found is False:
        if name.get() not in usernames:
            frame2.config(bg="red")
            access.config(bg="red", text="Username Unknown")
            access.place(x=30, y=40)
        else:
            frame2.config(bg="red")
            access.config(text="Access Denied", bg="red")
            access.place(x=50, y=40)
"""

login = Button(frame1, text="Log in", borderwidth="2", command=logginbutton)
login.place(x=100, y=170)


def clearbutton():
    frame2.config(bg="black")
    access.config(bg="black", text="")
    access.place(x=50, y=40)
    name.delete(0, END)
    passw.delete(0, END)


clear = Button(frame1, text="Clear", borderwidth="2", command=clearbutton)
clear.place(x=10, y=170)


def exitprogram():
    root.destroy()


exitt = Button(frame1, text="Exit", borderwidth="2", command=exitprogram)
exitt.place(x=195, y=170)

access = Label(frame2, bg="black")
access.place(x=50, y=40)
root.mainloop()
