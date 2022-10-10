from tkinter import * 
import os

def logout():
    return os.system("shutdown -l")

def restart():
    return os.system("shutdown /r /t 1")

def shutdown():
    return os.system("shutdown /s /t 1")

tk = Tk()
tk.title("System Controller")
tk.geometry("300x100")

Button(tk, text = "Log out [사용자를 로그아웃합니다]", command = logout).place(x = 50, y = 10)
Button(tk, text = "Restart [전원을 껏다킵니다]", command = restart).place(x = 50, y = 40)
Button(tk, text = "Shudown [전원을 종료합니다]", command = shutdown).place(x = 50, y = 70)

mainloop()