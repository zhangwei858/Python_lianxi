## --*-- coding=utf-8 --*--
import tkinter as tk
import threading
import paqu

strstr="";
root=tk.Tk()
root.title="数据爬取"
label=tk.Label(root,text='想要爬取吧名:',anchor='c').grid(row=0)
En=tk.Entry(root)
En.grid(row=0,column=1)

def get_shuju():
    global strstr
    strstr=En.get()
    root1=tk.Tk()
    tk.Label(root1,text="数据爬取过程中，请耐心等待。。。",fg="red",anchor="c").pack()
    tt=threading.Thread(target=paqu.main,args=(strstr,0))
    tt.start()
    tt.join()

tk.Button(root,text='确定',anchor='c',width=6,height=1,command=get_shuju).grid(row=2,column=1)
root.mainloop()
