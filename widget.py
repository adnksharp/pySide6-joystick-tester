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
        self.axes.scatter(512, 512, color=colors['on'])
        self.axes.scatter(x, y, color=colors['high'])
        self.axes.set_ylim(0, 1023)
        self.axes.set_xlim(0, 1023)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.graph = Canvas()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
