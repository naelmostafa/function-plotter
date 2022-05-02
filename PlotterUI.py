from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
import Plotter


class PlotterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.function_input = None
        self.x_max_input = None
        self.x_min_input = None
        self.step_input = None
        self.initUI()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                               "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.plot()
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def errorMessage(self, error_message):
        QtWidgets.QMessageBox.about(self, 'Error', 'Error: ' + error_message)

    def plot(self):
        try:
            if self.function_input.text() == '':
                self.errorMessage('Enter function')
                return
            if self.x_min_input.text() == '':
                self.errorMessage('Enter x min')
                return
            if self.x_max_input.text() == '':
                self.errorMessage('Enter x max')
                return
            if self.step_input.text() == '':
                self.errorMessage('Enter step')
                return
            if not self.isFloat(self.x_min_input.text()):
                self.errorMessage('X min not valid'
                                  '\nEnter float number')
                return
            if not self.isFloat(self.x_max_input.text()):
                self.errorMessage('X max not valid'
                                  '\nEnter float number')
                return
            if not self.isFloat(self.step_input.text()) or float(self.step_input.text()) <= 0:
                self.errorMessage('Step not valid'
                                  '\nEnter float number > 0')
                return
            if float(self.x_min_input.text()) >= float(self.x_max_input.text()):
                self.errorMessage('x min must be less than x max')
                return

            Plotter.plot(self.function_input.text(), float(self.x_min_input.text()), float(self.x_max_input.text()),
                         float(self.step_input.text()))
        except Exception as e:
            self.errorMessage(str(e))

    def initUI(self):
        self.setWindowTitle('Plotter')
        self.resize(800, 600)
        grid_layout = QtWidgets.QGridLayout()

        function_label = QtWidgets.QLabel('Function:')
        grid_layout.addWidget(function_label, 0, 0)
        self.function_input = QtWidgets.QLineEdit()
        self.function_input.setPlaceholderText('Enter function here')
        grid_layout.addWidget(self.function_input, 0, 1)

        x_min_label = QtWidgets.QLabel('X min:')
        grid_layout.addWidget(x_min_label, 1, 0)
        self.x_min_input = QtWidgets.QLineEdit()
        self.x_min_input.setPlaceholderText('Enter x min here')
        grid_layout.addWidget(self.x_min_input, 1, 1)

        x_max_label = QtWidgets.QLabel('X max:')
        grid_layout.addWidget(x_max_label, 2, 0)
        self.x_max_input = QtWidgets.QLineEdit()
        self.x_max_input.setPlaceholderText('Enter x max here')
        grid_layout.addWidget(self.x_max_input, 2, 1)

        step_label = QtWidgets.QLabel('Step:')
        grid_layout.addWidget(step_label, 3, 0)
        self.step_input = QtWidgets.QLineEdit()
        self.step_input.setPlaceholderText('Enter step here')
        grid_layout.addWidget(self.step_input, 3, 1)

        plot_button = QtWidgets.QPushButton('Plot')
        plot_button.clicked.connect(self.plot)
        grid_layout.addWidget(plot_button, 4, 0, 1, 2)

        self.setLayout(grid_layout)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @staticmethod
    def isFloat(string):
        try:
            float(string)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ex = PlotterUI()
    app.exec_()
