import asyncio
from bleak import discover

devices = []
services = []
async def scan():
    dev = await discover()
    for i in range(0,len(dev)):
        print("["+str(i)+"]"+str(dev[i]))
        devices.append(dev[i])

from bleak import BleakClient

async def connect(address, loop):
    async with BleakClient(address, loop=loop) as client:
        char_uuid = "0000180d-0000-1000-8000-00805f9b34fb"
        print("Getting client services")
        services = await client.get_services()
        for service in services:
            print(service)
            if service.uuid == char_uuid:
                print(service.uuid, " service was found!")
                break
        notifications = await client.start_notify(char_uuid, callback)
        print("Notifications: ", notifications)
        # for service in services:
        #     print(service)

def callback(sender, data):
        print(f"{sender}: {data}")

loop = asyncio.get_event_loop()
loop.run_until_complete(scan())
for indexed, device in enumerate(devices):
    # print(device.address)
    if device.address == "F5:D2:A7:12:62:5A":
        print(device.address, " was found!")
        index = indexed
        break
loop.run_until_complete(connect(devices[index].address, loop))
