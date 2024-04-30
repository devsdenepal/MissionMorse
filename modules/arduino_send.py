def arduino_send(command):

    import serial.tools.list_ports

    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portsList = []

    for one in ports:
        portsList.append(str(one))
        print(str(one))

    com = input("Select Com Port for Arduino #: ")

    for i in range(len(portsList)):
        if portsList[i].startswith("COM" + str(com)):
            use = "COM" + str(com)
            print(use)

    serialInst.baudrate = 9600
    serialInst.port = use
    serialInst.open()

    while True:
        command = command.encode('utf-8')
        serialInst.write(command)

        if command == 'exit':
            exit()
