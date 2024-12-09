import sys
from pymata4 import pymata4 as arduino

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPalette
from PySide6.QtCore import QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

colors = {
        'high': '#5bf2fa',
        'low': '#2c3e7f',
        'on': '#f75d54',
        'off': '#812b2d'
        }

SW = 2
JSX = 0
JSY = 1

class Canvas(FigureCanvas):
    def __init__(self):
        fig = Figure(facecolor=QPalette().color(QPalette.Window).name())
        fig.set_tight_layout(True)

        self.axes = fig.add_subplot(111, facecolor=QPalette().color(QPalette.Window).name())
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)
        
        for spine in self.axes.spines.values():
            spine.set_edgecolor(QPalette().color(QPalette.Window).name())

        super(Canvas, self).__init__(fig)

    def update(self, x = 512, y = 512):
        self.axes.clear()
        self.axes.scatter(512, 512, color=colors['on'])
        self.axes.scatter(x, y, color=colors['high'])
        self.axes.set_ylim(0, 1023)
        self.axes.set_xlim(0, 1023)

class Board():
    def __init__(self, sw, *args):
        self.board = arduino.Pymata4()
        self.jdata = [0, 0, 0]
        self.joystick = args
        self.switch = sw
        self.board.set_pin_mode_analog_input(args[0], self.xnew)
        self.board.set_pin_mode_analog_input(args[1], self.ynew)
        self.board.set_pin_mode_digital_input_pullup(sw, self.snew)
            
    def update(self, data, i):
        self.jdata[i] = data
            
    def xnew(self, data):
        self.update(data[2], 0)
        
    def ynew(self, data):
        self.update(data[2], 1)
        
    def snew(self, data):
        self.update(1 - data[2], 2)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.data = [0, 0, 0]
        
        self.graph = Canvas()
        self.ino = Board(SW, JSX, JSY)
        self.timer = QTimer()
        
        self.plot()
        
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        
    def plot(self):
        if self.ui.verticalLayout.count() > 1:
            self.ui.verticalLayout.removeWidget(self.graph)
        self.graph = Canvas()
        self.graph.update(self.data[0], self.data[1])
        
        self.ui.verticalLayout.addWidget(self.graph)
        
    def update(self):
        if self.ino.jdata[:3] != self.data:
            self.data = self.ino.jdata[:3]
            self.ui.ax.display(int(self.data[0] * 25 / 128) - 100)
            self.ui.ay.display(int(self.data[1] * 25 / 128) - 100)
            self.ui.di.display(self.data[2])
            self.plot()
        
    def closeEvent(self, event):
        self.ino.board.shutdown()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
