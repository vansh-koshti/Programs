import tkinter as tk

ch= int(input("enter 1 for code generation and 0 for message generation : "))
if ch == 1:
    r = tk.Tk()

    canvas1 = tk.Canvas(r, width = 400, height = 500)
    canvas1.pack()

    entry1 = tk.Entry(r)
    canvas1.create_window(200, 140, window=entry1)

    entry2 = tk.Entry(r)
    canvas1.create_window(200, 180, window=entry2)

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
        label1 = tk.Label(r, text= listToStr )
        canvas1.create_window(200, 260, window=label1)
        label2 = tk.Label(r, text= int(len(variable)/2) )
        canvas1.create_window(200, 290, window=label2) 
            
    button1 = tk.Button(text = 'Generate code', command = codegen)
    canvas1.create_window(200, 230, window=button1)
    button2 = tk.Button(text = 'Close', command= r.destroy)
    canvas1.create_window(200, 320, window=button2)

    r.mainloop()
    
elif ch == 0:
    r = tk.Tk()

    canvas1 = tk.Canvas(r, width = 400, height = 500)
    canvas1.pack()

    entry1 = tk.Entry(r)
    canvas1.create_window(200, 140, window=entry1)

    entry2 = tk.Entry(r)
    canvas1.create_window(200, 180, window=entry2)

    entry3 = tk.Entry(r)
    canvas1.create_window(200, 220, window=entry3)

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

        label1 = tk.Label(r, text= msg.join(msgcode) )
        canvas1.create_window(200, 260, window=label1)

    button3 = tk.Button(text = 'Generate message', command = msggen)
    canvas1.create_window(200, 300, window=button3)
    button4 = tk.Button(text = 'Close', command= r.destroy)
    canvas1.create_window(200, 340, window=button4)

    r.mainloop()

else:
    print("wronge input")











          





    

    
                 
    
    
