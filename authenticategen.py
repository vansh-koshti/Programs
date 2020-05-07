import tkinter as tk                
from tkinter import font  as tkfont 

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="code/message generator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="code generate",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="message generate",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter message and then uid", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        entry1 = tk.Entry(self)
        entry1.pack()

        entry2 = tk.Entry(self)
        entry2.pack()

        def codegen():
            msg= entry1.get()
            x = entry2.get()

            uid = int(x)        
            
            msgar= list(msg)
            msgcode=[]
            for i in msgar:
                msgcode.append(ord(i))

            variable=[]
            carry=[]
            c=0
            for j in msgcode:
                c=int(j/uid)
                car = int(j - (uid*c))
                variable.append(c)
                carry.append(car)
                
            variable.extend(carry)
            listToStr = '.'.join([str(elem) for elem in variable])
            
            label1 = tk.Label(self, text = listToStr, font = controller.title_font)
            label1.pack(side = "top", fill = "x", pady = 10)

            label2 = tk.Label(self, text = int(len(variable)/2), font = controller.title_font)
            label2.pack(side = "top", fill = "x", pady = 20)

        button1 = tk.Button(self, text="Generate", command = codegen)
        button1.pack()
            
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter two numbers in the two boxes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        entry1 = tk.Entry(self)
        entry1.pack()

        entry2 = tk.Entry(self)
        entry2.pack()

        entry3 = tk.Entry(self)
        entry3.pack()

        def msggen():
        
            code=[]
            variable=[]
            carry=[]

            n = int(entry1.get())
            uid = int(entry2.get())
                 
            variable = list(map(int, (entry3.get()).strip().split(".")))[:n*2]


            l=int(len(variable)/2)

            for j in range(0,l):
                code.append(variable[j])

            for k in range(l, len(variable)):
                carry.append(variable[k])

            msg=""
            msgcode=[]
            for (l,m) in zip(code,carry):
                c=int ((l*uid)+ m)
                msgcode.append(chr(c))
            label1 = tk.Label(self, text= msg.join(msgcode), font=controller.title_font)
            label1.pack(side="top", fill="x", pady=10)
            

        button1 = tk.Button(self, text="Generate message", command = msggen)
        button1.pack()
            
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
