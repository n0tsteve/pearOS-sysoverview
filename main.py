#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Form
from cpuinfo import get_cpu_info as cpu
from psutil import virtual_memory as ram
from psutil import disk_usage as disk
import sys, subprocess

#Init
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#Hook logic
#Processor
ui.proc.setText(cpu()['brand_raw'])

#RAM
ui.mem.setText(str(round(ram().total / 1073741824))+ " GB")

#GPU
output = subprocess.check_output("lspci | grep VGA | cut -d' ' -f 5-", shell=True, universal_newlines=True)
output2 = output.replace("\n", "")
ui.gpu.setText(str(output2))

#Serial Number
ui.sernum.setText("C02PGR98GFWM")

#Display
size = app.primaryScreen().size()
ui.disp.setText(str(size.width()) + "x" + str(size.height()))

#HDD
hdd = disk('/')
ui.hddbar.setValue(int(hdd.percent))

#Main loop
Form.show()
sys.exit(app.exec_())
