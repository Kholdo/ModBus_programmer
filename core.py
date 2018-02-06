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