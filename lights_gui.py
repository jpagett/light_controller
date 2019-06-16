import sys
import os
import serial
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox,
    QPushButton, QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# Set COM port for arduino

ser = serial.Serial('COM3', 9600, timeout=1)

class Window(QWidget):

    def __init__(self,name):
        super().__init__()
        self.name = name
        self.initUI(name)

    def initUI(self,name):

        grid = QGridLayout()
        self.setLayout(grid)

        power_on_btn = QPushButton('On', self)
        power_on_btn.setToolTip('Turn on the lights.')
        power_on_btn.clicked.connect(self.power_on)
        grid.addWidget(power_on_btn, 0, 0)

        power_off_btn = QPushButton('Off', self)
        power_off_btn.setToolTip('Turn off the lights.')
        power_off_btn.clicked.connect(self.power_off)
        grid.addWidget(power_off_btn, 0, 2)

        dim_btn = QPushButton('Dim', self)
        dim_btn.setToolTip('Decrease the brightness..')
        dim_btn.clicked.connect(self.dim_light)
        grid.addWidget(dim_btn, 1, 0)

        brighten_btn = QPushButton('Brighten', self)
        brighten_btn.setToolTip('Increase the brightness.')
        brighten_btn.clicked.connect(self.brighten_light)
        grid.addWidget(brighten_btn, 1, 2)

        prev_color_btn = QPushButton('Previous Color', self)
        prev_color_btn.setToolTip('Switch to previous color.')
        prev_color_btn.clicked.connect(self.prev_color)
        grid.addWidget(prev_color_btn, 2, 0)

        next_color_btn = QPushButton('Next Color', self)
        next_color_btn.setToolTip('Switch to next color..')
        next_color_btn.clicked.connect(self.next_color)
        grid.addWidget(next_color_btn, 2, 2)

        slow_cycle_btn = QPushButton('Slow Cycle', self)
        slow_cycle_btn.setToolTip('Set to slow cycle mode.')
        slow_cycle_btn.clicked.connect(self.slow_cycle)
        grid.addWidget(slow_cycle_btn, 3, 0)

        mode_btn = QPushButton('Mode', self)
        mode_btn.setToolTip('Switch modes.')
        mode_btn.clicked.connect(self.mode)
        grid.addWidget(mode_btn, 3, 1)

        fast_cycle_btn = QPushButton('Fast Cycle', self)
        fast_cycle_btn.setToolTip('Set to fast cycle mode.')
        fast_cycle_btn.clicked.connect(self.fast_cycle)
        grid.addWidget(fast_cycle_btn, 3, 2)

        colors = ['RGB White', 'True White', 'Warm White',
          'Red', 'Blue', 'Green']
        positions = [(i,j) for i in range (5,8) for j in range(3)]

        for position, color in zip(positions, colors):
            if color == '':
                continue
            button = QPushButton(color)
            button.setToolTip(f'Sets the light to {color}.')
            button.clicked.connect(self.color_set)
            grid.addWidget(button, *position)

        self.resize(400,400)
        self.setWindowTitle(name)
        icon_name = 'light_white.png'
        self.setWindowIcon(QIcon(icon_name))

        self.show()

    def closeEvent(self, event):
        ser.close()
        print('The serial connection has been closed.')

        #reply = QMessageBox.question(self, 'Message',
        #    "Are you sure to quit?", QMessageBox.Yes |
        #    QMessageBox.No, QMessageBox.No)

        #if reply == QMessageBox.Yes:
        #    event.accept()
        #    ser.close()
        #else:
        #    event.ignore()

    @pyqtSlot()
    def power_on(self):
        print('The light has been turned on.')
        ser.write(b'lightOn')

    @pyqtSlot()
    def power_off(self):
        print('The light has been turned off.')
        ser.write(b'lightOff')

    @pyqtSlot()
    def dim_light(self):
        print('The brightness has been decreased.')
        ser.write(b'dim')

    @pyqtSlot()
    def brighten_light(self):
        print('The brightness has been increased')
        ser.write(b'bright')

    @pyqtSlot()
    def prev_color(self):
        print('Switched to previous color.')
        ser.write(b'prevColor')

    @pyqtSlot()
    def next_color(self):
        print('Switched to next color.')
        ser.write(b'nextColor')

    @pyqtSlot()
    def slow_cycle(self):
        print('Set to slow cycle mode.')
        ser.write(b'slowCycle')

    @pyqtSlot()
    def mode(self):
        print('Cycled the lighting mode.')
        ser.write(b'modeSwitch')

    @pyqtSlot()
    def fast_cycle(self):
        print('Set to fast cycle mode.')
        ser.write(b'fastCycle')

    @pyqtSlot()
    def color_set(self):
        color_clicked = self.sender()

        color = color_clicked.text()
        message = f'The light color has been changed to {color}.'

        colors = ['RGB White', 'True White', 'Warm White',
          'Red', 'Blue', 'Green']
        color_codes = ['rgbWhite', 'trueWhite', 'warmWhite',
         'red', 'blue', 'green']

        color_code = color_codes[colors.index(color)]
        ser.write(f'{color_code}'.encode())

        print(message)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window('Light Controller')
    sys.exit(app.exec_())
