import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

helpwindow = tk.Tk()
helpwindow.title("Help")
helpwindow.geometry("500x200")
helplabel=tk.Label(helpwindow,text='''
                  John's Graphing Calculator v1.0
                  1. enter function into "enter equation", and then click on "plot"
                  2. for multiplication, use "*" and for exponents, use "**"
                  3. multiplication example: 5*x
                  4. exponent example: 2**x ''')
helplabel.pack()

class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Graphing Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.expression_label = ttk.Label(self.master, text="Enter Expression:")
        self.expression_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.expression_entry = ttk.Entry(self.master, width=30)
        self.expression_entry.grid(row=0, column=1, padx=10, pady=10)
        self.plot_button = ttk.Button(self.master, text="Plot", command=self.plot_graph)
        self.plot_button.grid(row=0, column=2, padx=10, pady=0)
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        

    def plot_graph(self):
        expression = self.expression_entry.get()
        self.ax.clear()
        x = np.linspace(-10, 10, 400)
        
        try:
            y = eval(expression, {'np': np, 'x': x})
            self.ax.plot(x, y, label=expression)
            self.ax.legend()
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.set_title("Graph of {}".format(expression))
            self.canvas.draw()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid expression: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = GraphingCalculator(root)
    root.mainloop()