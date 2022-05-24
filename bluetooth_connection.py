import bluetooth, subprocess
import polly_aws
import time

count = True
addressList = []
connect = [
    'conecte ao dispositivo ',
    'conecta ao dispositivo ',
    'conecte ao celular ',
    'conecte ao smartphone ',
    'conecte a ',
    'conecta ao ', 
    'conecta a TV',
    'conecte no dispositivo',
    'conecte ao dispositivo',
    'conecte no celular ',
    'conecte no celular',
    'conecta no celular ',
    'conecta no celular',
    'conectar no celular ',
    'connect no celular ',
    'conecta no bluetooth'
]

find = [
    'procure os dispositivos',
    'procure o bluetooth',
    'procure bluetooth',
    'busque o bluetooth',
    'busque bluetooth',
    'busque os bluetooth',
    'procura o bluetooth',
    'busca o bluetooth',
    'busca bluetooth',
    'buscar bluetooth',
    'liste bluetooth',
    'liste o bluetooth',
    'lista o bluetooth',
    'lista bluetooth',
    'lista os dispositivos',
    'lista o dispositivo',
    'liste o dispositivo',
    'liste os dispositivos',
]

def finding():
    while count:
        nearby_devices = bluetooth.discover_devices(duration=4,lookup_names=True,
                                                              flush_cache=True, lookup_class=False)
        if len(nearby_devices) < 1:
            return polly_aws.text_to_audio('Nenhum dispositivo encontrado senhor.')

        if len(nearby_devices) == 1:
            polly_aws.text_to_audio("Encontrado {} dispositivo senhor, ele é:".format(len(nearby_devices)))
            for addr, name in enumerate(nearby_devices):
                addressList.append(
                    {'addr': name[0], 'name': name[1]}
                )
                polly_aws.text_to_audio("{}".format(name[1]))
            if len(addressList) == 1:
                polly_aws.text_to_audio('vou conectar nele.')
                connectDevice(name[1])
                return 
            return
        
        polly_aws.text_to_audio("Encontrados {} dispositivos senhor, eles são:".format(len(nearby_devices)))
        for addr, name in enumerate(nearby_devices):
            addressList.append(
                {addr: addr, name: name[1]}
            )
            polly_aws.text_to_audio("{}".format(name[1]))
        return

def findDevices(text):
    try:
        for item in find:
            if item in text:
                text
                text = text.replace(item, "")
                finding()
    except Exception as err:
        print(err)
            

def connectDevice(text):
    if len(addressList) == 0:
        polly_aws.text_to_audio('vamos procurar os dispositivos, um momento')
        finding()
        return
    time.sleep(1)
    for item in addressList:
        if addressList[0]['name'] in text:
            for services in bluetooth.find_service(address=item['addr']):
                    if "RFCOMM" in services['protocol']:
                        try:
                            s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                            s.connect((services['host'], services['port']))
                            count = False
                            return polly_aws.text_to_audio('Você está conectado senhor')
                        except bluetooth.btcommon.BluetoothError as err:
                            return polly_aws.text_to_audio('Tive problemas ao conectar senhor')
                            
def run(text):
    connectDevice(text)
    findDevices(text)