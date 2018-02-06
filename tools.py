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

def stepTH():
    '''Devuelve un diccionario con el mapa de memoria ModBus del equipo y su configuracion de fabrica
    '''
    memo_Integers = {'identificador': 4000,
                     'nper': 4001,
                     'velocidad': 4002,
                     'datos comunication': 4003,
                     'validar datos com': 4004,
                     'tiempo promedio medidas': 4005,
                     'borrado max y min': 4006}
    memo_Floats = {'identificador 2': 7000,
                   'temperatura': 7002,
                   'humedad relativa': 7004,
                   'punto de rocio': 7006,
                   'humedad absoluta': 7008,
                   'temp minima': 7010,
                   'temp maxima': 7012,
                   'humedad relativa minima': 7014,
                   'humedad relativa maxima': 7016,
                   'punto rocio minimo': 7018,
                   'punto rocio maximo': 7020,
                   'humedad absoluta minima': 7022,
                   'humedad absoluta maxima': 7024}
    default_config = {'method': 'rtu',
                      'stopbits': 1,
                      'bytesize': 8,
                      'parity': 'N',
                      'baudrate': 9600,
                      'timeout': 1000}
    return {'memo_Integers': memo_Integers, 'memo_Floats': memo_Floats, 'default_config': default_config}