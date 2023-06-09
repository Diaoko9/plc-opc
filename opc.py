from asyncua import Client

async with Client(url='opc.tcp://localhost:4840/freeopcua/server/') as client:
    while True:
        #Do
        node = client.get_node('i=85')
        value = await node.read_value()

