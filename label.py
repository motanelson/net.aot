import tkinter as tk

class myapp:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("tk")
        self.root.configure(background="black")
        self.mn= tk.Label(root,text="hello world",background="black",foreground="white",width=300)
        self.mn.pack()
        self.root.config()
    def hello(self):
        print("hello world...")        







root=tk.Tk()
apps=myapp(root)
root.mainloop()

