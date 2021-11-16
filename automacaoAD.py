import argparse
import rpyc 
from rpyc.utils.server import ThreadedServer
import datetime
import subprocess

data_tempo = datetime.datetime.now()

class monitService(rpyc.Service):
    def on_connect(self, conn):
        print('\nConectado em {}'.format(data_tempo))

    def on_disconnect(self, conn):
        print('Desconectado em {}\n'.format(data_tempo))

    def exposed_run_command(self, command):
        try: 
            output = subprocess.check_output(command, shell=True)
            print(output)
        except subprocess.CalledProcessError as Error:
                print(Error.returncode)
                print(Error.output)

def main():
    parser = argparse.ArgumentParser(description='Active Directory Bot')
    parser.add_argument('-port', type=int, help='Digite o numero da porta')
    args = parser.parse_args()
    port = args.port
    if not port:
        port = 19961

    t = ThreadedServer(monitService, port=port)
    t.start()

if __name__ == '__main__':
    main()