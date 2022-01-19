from tkinter import *

def read_csv():
    import csv
    file = open("D:\Skola\Infovis\\data1.csv")
    reader = csv.reader(file, delimiter = ',')
    data = []
    for idx, row in enumerate(reader):
        data.append((float(row[0]), float(row[1]), str(row[2])))

    min_x = min(data, key = lambda x: x[0])[0]
    max_x = max(data, key = lambda x: x[0])[0]
    min_y = min(data, key = lambda x: x[1])[0]
    max_y = max(data, key = lambda x: x[1])[0]

    return data, min_x, max_x, min_y, max_y

class StartWindow:
    def __init__(self, master):
        self.windowsize = (400, 400)
        self.master = master
        master.title("Start")
        master.geometry('400x400')

        # create menu bar
        menubar = Menu(master)
        menubar.add_command(label = "Load file", command = master.quit)
        menubar.add_command(label = "Clear plot", command = master.quit)
        master.config(menu = menubar)

        # create canvas 
        self.canvas_size = (self.windowsize[0] - 20, self.windowsize[1] - 20)
        self.canvas = Canvas(master, background = '#757575')
        self.offset = 20
        self.canvas.pack(expand = True, fill = BOTH, padx = 10, pady = 10)
        self.drawAxis()
        self.drawScatterData(read_csv())
        
        
    # helper function to draw a simple line
    def drawLine(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, width = 3)

    # called upon canvas creation and draws the basic 
    def drawAxis(self):
        self.drawLine(self.offset, self.canvas_size[1] - self.offset, self.canvas_size[0] - self.offset, self.canvas_size[1] - self.offset)
        self.drawLine(self.offset, self.canvas_size[1] - self.offset, self.offset, self.offset)

        # create ticks
        incrementer = self.offset*2
        for x in range(self.offset, self.canvas_size[0], incrementer):
            self.drawLine(x, self.canvas_size[1] - self.offset, x, self.canvas_size[1] - self.offset*1.25)
        for y in range(self.offset, self.canvas_size[1], incrementer):
            self.drawLine(self.offset, y, self.offset*1.25, y)

    # helper function to draw a simple circle
    def drawCircle(self, center_x, center_y, radius):
        self.canvas.create_oval(center_x-radius, center_y-radius, center_x+radius, center_y+radius, fill='red')
    
    def drawScatterData(self, data): 
        for entry in data[0]:
            #print(entry[0])
            self.drawCircle(entry[0], entry[1], 5)

    # x ->
    # y
    # |
    # |

if __name__ == '__main__':
    root = Tk()
    app = StartWindow(root)
    root.mainloop()


# Load csv, clear graph
# Legend
# grid
# Draw plot
# Clear plot