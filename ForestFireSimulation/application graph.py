import tkinter as tk
from ForestFire import automateCellulaire
from copy import deepcopy

from matplotlib.figure import Figure
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class Application(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.initUI()

        
        
    def initUI(self):
        def plot():
            (self.d,self.p,self.t,self.x,self.y)=varUI()
            self.gridSize = [self.x,self.y]
            
            try:
                self.T
            except AttributeError:
                self.T = [[self.t for i in range(self.gridSize[0])] for j in range(self.gridSize[1])]
                startingPoint()
                self.Tab= deepcopy(self.T)
            
            for j in range(20):
                self.Tab= automateCellulaire(self.Tab,self.d,self.p)   
            try: 
                self.canvas.get_tk_widget().pack_forget()
            except AttributeError:
                self.button_start['text']="Next step"
                pass           
            self.fig = Figure( figsize=(5, 5), dpi=100)
            self.fig.add_subplot(111).matshow(self.Tab)
            self.canvas = FigureCanvasTkAgg(self.fig, master=Frame2)
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.canvas.draw()
            
            
        def varUI():
            choiceD=varChoiceD.get()
            choiceS=varChoiceS.get()
            if(choiceD == 1):
                d="N"
            elif(choiceD == 2):
                d="S"
            elif(choiceD == 3):
                d="W"
            elif(choiceD == 4):
                d="E"
            else:
                d=0
                
            if(choiceS == 1):
                p=1
            elif(choiceS == 2):
                p=15
            elif(choiceS == 3):
                p=30
            elif(choiceS == 4):
                p=45
            elif(choiceS == 5):
                p=60
            else:
                p=0

            t=temperature_value.get()
            x=gridx_value.get()
            y=gridy_value.get()
            
            return(d,p,t,x,y)
            
        def restart():
            try: 
                del self.T
                self.canvas.get_tk_widget().pack_forget()
                self.button_start['text']="Start simulation"
            except AttributeError: 
                pass     
        
        def startingPoint():
            n = np.random.randint(self.x, size=(start_value.get()))
            p = np.random.randint(self.y, size=(start_value.get()))
            
            for i in range(start_value.get()):
                self.T[n[i]][p[i]]=500
            
            

                
        Frame1 = tk.Frame(self , borderwidth = 2 , relief = tk.GROOVE)
        Frame1.pack(side=tk.LEFT , padx=30 , pady = 30)

        Frame2 = tk.Frame(self, width= 500 , height = 400, borderwidth=2, relief=tk.GROOVE)
        Frame2.pack(side=tk.RIGHT, padx=10, pady=10)
        
        Frame4 = tk.Frame(Frame1 , borderwidth = 2 , relief = tk.GROOVE)
        Frame4.pack(side=tk.BOTTOM , padx=30 , pady = 30)
        
        Frame3 = tk.Frame(Frame1 , borderwidth = 2 , relief = tk.GROOVE)
        Frame3.pack(side=tk.BOTTOM , padx=30 , pady = 30)
        
        champ_label1 = tk.Label(Frame1 ,text = "Wind direction")
        
        varChoiceD = tk.IntVar()
        varChoiceD.set(1)

        choiceD1 = tk.Radiobutton(Frame1, text="North", variable=varChoiceD, value=1)
        choiceD2 = tk.Radiobutton(Frame1, text="South", variable=varChoiceD, value=2)
        choiceD3 = tk.Radiobutton(Frame1, text="East", variable=varChoiceD, value=3)
        choiceD4 = tk.Radiobutton(Frame1, text="West", variable=varChoiceD, value=4)
        
        
        champ_label1.pack()
        choiceD1.pack(side=tk.TOP)
        choiceD2.pack(side=tk.TOP)
        choiceD3.pack(side=tk.TOP)
        choiceD4.pack(side=tk.TOP)

        
        champ_label2 = tk.Label(Frame1 ,text = "Wind Speed")
        
        varChoiceS = tk.IntVar()
        varChoiceS.set(1)

        choiceS1 = tk.Radiobutton(Frame1, text="1 Km/h", variable=varChoiceS, value=1)
        choiceS2 = tk.Radiobutton(Frame1, text="15 Km/h", variable=varChoiceS, value=2)
        choiceS3 = tk.Radiobutton(Frame1, text="30 Km/h", variable=varChoiceS, value=3)
        choiceS4 = tk.Radiobutton(Frame1, text="45 Km/h", variable=varChoiceS, value=4)
        choiceS5 = tk.Radiobutton(Frame1, text="60 Km/h", variable=varChoiceS, value=5)
        
        
        champ_label2.pack()
        choiceS1.pack()
        choiceS2.pack()
        choiceS3.pack()
        choiceS4.pack()
        choiceS5.pack()

        
        
        temperature_label = tk.Label(Frame1 , text = "Ambiant temperature")
        
        temperature_value = tk.IntVar()
        ligne_texte = tk.Entry(Frame1, textvariable = temperature_value, width=5)
        ligne_texte.insert(0,3)
        
        temperature_label.pack()
        ligne_texte.pack()
        
        
        start_label = tk.Label(Frame1 , text = "Number of starting points")
        
        start_value = tk.IntVar()
        start_text = tk.Entry(Frame1, textvariable = start_value, width=5)
        start_text.insert(0,1)
        
        start_label.pack()
        start_text.pack()
        
        
        self.button_start = tk.Button(Frame4, text="Start simulation", command=plot)
        
        self.button_start.pack()
        
        button_restart = tk.Button(Frame4, text="Restart", command=restart)
        
        button_restart.pack()
        
        grid_label = tk.Label ( Frame3, text= "Grid size")
        x_label = tk.Label( Frame3, text="x")
        
        gridx_value = tk.IntVar()
        gridx_field = tk.Entry(Frame3, textvariable = gridx_value, width = 3)
        gridx_field.insert(0,10)
        
        gridy_value = tk.IntVar()
        gridy_field = tk.Entry(Frame3, textvariable = gridy_value, width = 3)
        gridy_field.insert(0,10)
        
        grid_label.pack()
        gridx_field.pack(side = tk.LEFT)
        x_label.pack(side = tk.LEFT)
        gridy_field.pack(side = tk.RIGHT)
        
        
if __name__ == "__main__":
    app = Application()
    app.title("Forest Fire Simulation")
    app.mainloop()