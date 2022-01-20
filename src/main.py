from tkinter import *
import os

def read_csv():
    import csv
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data1.csv')
    file = open(filename, "r")
    reader = csv.reader(file, delimiter = ',')
    data = []
    for idx, row in enumerate(reader):
        data.append((float(row[0]), float(row[1]), str(row[2])))

    min_x = min(data, key = lambda x: x[0])[0]
    max_x = max(data, key = lambda x: x[0])[0]
    min_y = min(data, key = lambda x: x[1])[1]
    max_y = max(data, key = lambda x: x[1])[1]

    return data, min_x, max_x, min_y, max_y

class Application:
    def __init__(self, master):
        self.windowsize = (600, 800)
        self.master = master
        master.title("Start")
        master.geometry(str(self.windowsize[0]) + "x" + str(self.windowsize[1]))

        # create menu bar
        menubar = Menu(master)
        menubar.add_command(label = "Load file", command = master.quit)
        menubar.add_command(label = "Clear plot", command = master.quit)
        master.config(menu = menubar)

        # create canvas 
        self.canvas_size = (self.windowsize[0] - 20, self.windowsize[1] - 200)
        print(self.canvas_size[0], self.canvas_size[1])
        self.canvas = Canvas(master, background = '#757575')
        self.offset = 20
        self.axis_length = self.canvas_size[0] - 2 * self.offset
        self.canvas.pack(expand = True, fill = BOTH, padx = 10, pady = 0)
        # label stuff
        self.label_canvas = Canvas(self.master, background="#ffffff", width=self.windowsize[0], height=200)
        self.label_canvas.pack()
        self.available_colors = []
        self.label_dict = {}
        # render some stuff
        # render label
        self.loadNewData()
        # render grid
        self.drawAxis()

    def drawLegend(self):
        self.label_canvas.create_text(self.windowsize[0]/2, 30, fill="darkblue",font="Times 20 italic bold",
                        text="Click the", tags='text')
                        
        for value, t, x in enumerate(self.label_dict):
            print(x)
        
    def loadNewData(self):
        # data points
        self.data = read_csv()
        # TODO: clear points from canvas

        # reset label stuff
        self.available_colors = ['red', 'blue', 'green', 'yellow']
        self.label_dict = {}
        self.label_canvas.delete('text')
        # fill label dictionary
        for point in self.data[0]:
            # label check
            if point[2] not in self.label_dict:
                self.label_dict[point[2]] = self.available_colors.pop()

        self.drawLegend()
        self.drawScatterData()

    # helper function to draw a simple line
    def drawLine(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, width = 3)

    # called upon canvas creation and draws the basic 
    def drawAxis(self):
        center = (self.canvas_size[0]/2, self.canvas_size[1]/2)
        # x-axis
        self.drawLine(self.offset, center[1], self.canvas_size[0] - self.offset, center[1])
        # y-axis
        self.drawLine(center[0], self.canvas_size[1] - self.offset, center[0], self.offset)

        # create ticks
        incrementer = int(self.axis_length / 30) 

        for x in range(self.offset, self.canvas_size[0], incrementer):
            self.drawLine(x, center[1]-5, x, center[1]+5)
        for y in range(self.offset, self.canvas_size[1], incrementer):
            self.drawLine(center[0]-5, y, center[0]+5, y)

    # helper function to draw a simple circle
    def drawCircle(self, center_x, center_y, radius, color):
        self.canvas.create_oval(center_x-radius, center_y-radius, center_x+radius, center_y+radius, fill=color)
    
    def drawScatterData(self): 
        for point in self.data[0]:
            self.drawPoint(point)

    def drawPoint(self, point):
        min_x = self.data[1]
        max_x = self.data[2]
        min_y = self.data[3]
        max_y = self.data[4]

        tx = (point[0] - min_x) / (max_x - min_x)
        ty = (point[1] - min_y) / (max_y - min_y)

        draw_x = self.offset + self.axis_length * tx
        draw_y = self.offset + self.axis_length * ty
        self.drawCircle(draw_x, draw_y, 4, self.label_dict[point[2]])

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()


# Load csv, clear graph
# Legend
# grid
# Draw plot
# Clear plot