import subprocess
import os
import sys
import asyncio
HEADER=1024
ENCODE='utf-8'
HOST = 'localhost'
async def query(command, wr):
    
    path = os.getcwd()
    path2 = path.encode()
    wr.write(path2)
    print(path2)
    await wr.drain()
    
    while True:
        comando = await command.read(HEADER)
        comando2 = comando.decode()
        if comando2.lower() == "exit":
            print("Desconectado")
            break
        else:
            try:
                show = subprocess.getshow(comando2)
                reponse = f"{show}"
            except:
                reponse = f"{show}"
            wr.write(reponse.encode(ENCODE))
            await wr.drain()
    wr.close()
    
if __name__=='__main__':
    async def main():
        PUERTO = int(sys.argv[1])
        servidor = await asyncio.start_server(query, HOST, PUERTO)
        async with servidor:
            await servidor.serve_forever()
    asyncio.run(main())