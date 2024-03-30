import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

# Sample data for the line plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a tkinter window
root = tkinter.Tk()
root.title("在Canvas中绘制Matplotlib漂亮的折线图")

# Create a frame to hold the canvas
canvas_frame = tkinter.Frame(root)
canvas_frame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

# Create a figure and axis for the plot
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Plot the lines on the axis
ax.plot(x, y1, label='sin(x)', color='b', linestyle='-', marker='o')
ax.plot(x, y2, label='cos(x)', color='r', linestyle='--', marker='s')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Beautiful Line Plot')
ax.legend()

# Create a canvas within the frame to display the plot
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the tkinter main loop
tkinter.mainloop()
