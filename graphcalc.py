import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphingCalculator:
    #initializing the calculator
    def __init__(self, master):
        self.master = master
        self.master.title("Graphing Calculator")

        self.create_widgets()
    #creating the widgets for the calculator.
    def create_widgets(self):
        self.expression_label = ttk.Label(self.master, text="Enter Expression:")
        self.expression_label.grid(row=0, column=0, padx=10, pady=10)

        self.expression_entry = ttk.Entry(self.master, width=30)
        self.expression_entry.grid(row=0, column=1, padx=10, pady=10)

        self.plot_button = ttk.Button(self.master, text="Plot", command=self.plot_graph)
        self.plot_button.grid(row=0, column=2, padx=10, pady=10)

        self.graph_frame = ttk.Frame(self.master)
        self.graph_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    #get 
    def plot_graph(self):
        expression = self.expression_entry.get()
        x_values = list(range(-10, 11))
        y_values = [eval(expression) for x in x_values]

        self.plot_graph_on_canvas(x_values, y_values)

    def plot_graph_on_canvas(self, x_values, y_values):
        figure = Figure(figsize=(5, 4), dpi=100)
        subplot = figure.add_subplot(1, 1, 1)
        subplot.plot(x_values, y_values)

        canvas = FigureCanvasTkAgg(figure, self.graph_frame)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = ttk.Frame(self.graph_frame)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        toolbar_button = ttk.Button(toolbar, text="Quit", command=self.master.quit)
        toolbar_button.pack(side=tk.RIGHT)

        canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphingCalculator(root)
    root.mainloop()