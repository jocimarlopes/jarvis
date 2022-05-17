import bluetooth, subprocess

count = True

while count:
    nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True,
                                                          flush_cache=True, lookup_class=False)
    print("Encontrados {} dispositivos.".format(len(nearby_devices)))
    for addr, name in nearby_devices:

        print("{} - {}".format(addr, name))

        for services in bluetooth.find_service(address=addr):
            if "RFCOMM" in services['protocol']:
                print(services)

                 #subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)
                #status = subprocess.call("bluetoothctl " + passkey, shell=True)
                try:
                    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                    s.connect((services['host'], services['port']))
                    print('Você conectou com a TV')
                    count = False
                except bluetooth.btcommon.BluetoothError as err:
                    print(err)
                    pass