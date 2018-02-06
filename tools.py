def usedComPorts():
    '''Devuelve la lista de los puertos COM que se están utilizando
    '''
    import serial.tools.list_ports
    comPorts = [portNum for portNum, description,
                address in list(serial.tools.list_ports.comports())]
    usedComPorts = 'noPorts'
    if len(comPorts) > 0:
        usedComPorts = comPorts[0]
    return usedComPorts