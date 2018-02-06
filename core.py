#!/usr/bin/env python.
"""
File name: core.py
Author: Koldo Pina
Date created: 06/02/2018
Date last modified: 06/02/2018
Python Version: 3.5
"""

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from tools import usedComPorts, stepTH

#We check the COM port that we are using
print (usedComPorts())

#Load connection default parameters
method = stepTH()['default_config']['method']
stopbits = stepTH()['default_config']['stopbits']
bytesize = stepTH()['default_config']['bytesize']
parity = stepTH()['default_config']['parity']
baudrate = stepTH()['default_config']['baudrate']
timeout = stepTH()['default_config']['timeout']
