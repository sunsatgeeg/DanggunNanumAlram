from ppadb.client import Client

adb = Client()
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

device.shell('input touchscreen swipe 500 500 500 500 2000')