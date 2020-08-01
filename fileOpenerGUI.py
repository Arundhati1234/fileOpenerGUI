import tkinter as tk
import tkfilebrowser as filedialog
import os
import sys

root = tk.Tk()
apps = []
flag = 0

def delAppList():
    os.remove('appslist.txt')
    py = sys.executable
    os.execl(py, py, * sys.argv)
    apps = []



delSavedApps = tk.Button(root, text="Delete List", padx=10, pady=10, bg="white", fg="#123456", command =delAppList)
if os.path.isfile('appslist.txt'):
    with open('appslist.txt', 'r') as txtf:
        tempApps = txtf.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        if len(apps) > 0:
            delSavedApps.pack(padx=80, ipadx=10,  fill=tk.X)



def openApp():

    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="white")
        label.pack()



def runApp():
    for app in apps:
        os.startfile(app)



canvas = tk.Canvas(root, height= 500, width= 500, bg = "#123456")
canvas.pack(fill=tk.Y)

frame = tk.Frame(root, bg = "#1ABC12")
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=10, bg="white", fg="#123456", command=openApp)
openFile.pack(padx=20, ipadx=10, fill=tk.X)
runApps = tk.Button(root, text="Run Apps", padx=10, pady=10, bg="white", fg="#123456", command=runApp)
runApps.pack(padx = 20, ipadx = 10, fill=tk.X)

for app in apps:
    applbl = tk.Label(frame, text=app, bg="white")
    applbl.pack()

root.mainloop()

with open('appslist.txt', 'w') as txtfile:
    for app in apps:
        txtfile.write(app + ',')
