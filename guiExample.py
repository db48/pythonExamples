import Tkinter
import tkMessageBox

colors = ['red','orange','yellow','green','blue','magenta4','darkorchid4']

class App:

    def __init__(self, root):
        self.root = root
        self.cidx = Tkinter.IntVar()
        self.cidx.set(0)
        self.cycleDuration = Tkinter.StringVar()
        self.cycleDuration.set("10")

        self.hlo = Tkinter.Button(root, text ="Hello", command = self.helloCallBack)
        self.hlo.grid(row=1, column=2)
        self.ex = Tkinter.Button(root, text ="Quit", command = self.quitCallback)
        self.ex.grid(row=4, column=2)
        self.tbLabel = Tkinter.Label(root, text="Timer Duration")
        self.tbLabel.grid(row=2, column=1)
        self.timeBox = Tkinter.Entry(root, textvariable=self.cycleDuration)
        self.timeBox.grid(row=2, column=2)
        self.colorButton = Tkinter.Button(root,text="change color", command = self.colorChangeCB)
        self.colorButton.grid(row=3, column=1)
        self.colorBox = Tkinter.Entry(root, bg=colors[self.cidx.get()])
        self.colorBox.grid(row=3, column=2)
        self.colorButton2 = Tkinter.Button(root,text="cycle colors", command = self.runColors)
        self.colorButton2.grid(row=3, column=3)

    def helloCallBack(self):
        if len(self.timeBox.get()) == 0:
            tkMessageBox.showinfo( "Hello Python", "Hello World!")
        else:
            tkMessageBox.showinfo( "Hello Python", "Hello World: " + self.cycleDuration.get())

    def quitCallback(self):
        self.root.destroy()

    def colorChangeCB(self):
        self.cidx.set(self.cidx.get() + 1)
        self.colorBox.config(bg=colors[self.cidx.get()%len(colors)])

    def runColors(self):
        self.colorChangeCB()
        timeLeft = int(self.cycleDuration.get())-1
        self.cycleDuration.set(str(timeLeft))
        if timeLeft != 0:
            self.colorBox.after(1000, self.runColors)
        else:
            tkMessageBox.showinfo( "Done!", "Done Counting!")


root = Tkinter.Tk()
app = App(root)
root.mainloop()
