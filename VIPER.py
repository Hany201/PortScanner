from tkinter import *
from tkinter import ttk,scrolledtext
import nmap
root=Tk()
root.geometry('800x800')
root.title("VIPER Tool - Port Scanning    By: Hany Shawky")
#root.iconbitmap(r'Viper.ico')

style=ttk.Style()
style.theme_use('classic')
style.configure("TButton",font=("tahoma",16,"bold"))
style.configure("TButton",foreground="Red")

style.configure("TLabel",font=("tahoma",12,"bold"))
style.configure("TLabel",foreground="Black")


ttk.Label(root,text="Enter Domain or IP address").grid(row=0,column=0)
entry1=ttk.Entry(root,width="30")
entry1.grid(row=0,column=1)

#result Scan
ttk.Label(root,text="Open Ports").grid(row=3,column=0)
ResultScan=Text(root,width="100",height="100")
ResultScan.grid(row=4,column=0,columnspan=3)
ResultScan.configure(state='disabled')


def OnClick():
    ResultScan.configure(state='normal')
    ns = nmap.PortScanner()
    ns.scan(entry1.get(), '1-1024', '-v')
    print(ns.scaninfo())
    print(ns.csv())
    ResultScan.delete(1.0,END)  # clear the outputtext text widget. 1.0 and tk.END are neccessary. tk implies the tkinter module. If you just want to add text dont incude that line
    ResultScan.insert(END, ns.scaninfo())  # insert the entry widget contents in the text widget. tk.END is necessary.
    ResultScan.insert(END, ns.csv())  # insert the entry widget contents in the text widget. tk.END is necessary.
    ResultScan.configure(state='disabled')

button1=ttk.Button(root,text="Scan")
button1.grid(row=0,column=2)
#button1.config(image=resized,compound=CENTER)
button1.config(command=OnClick)



root.mainloop()
