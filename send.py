import sys
sys.path.append('./gen-py')
 
from client import Service
from client.ttypes import Usuario 
 

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
 
#  Funcion para realizar comunicacion con el servidor
#  metodoRemoto : metodo que se va a ejecutar dentro del servidor
# *args parametro de funcion a invocar
def enviar(metodoRemoto, *args):
  try:
    print "Iniciando Comunicacion Server..."
    transport = TSocket.TSocket('127.0.0.1', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Service.Client(protocol)
    transport.open()
    respuesta= metodoRemoto(client, *args)
  
    transport.close()

    return respuesta
  
  except Thrift.TException, tx:
    print "Ocurrio un Error: "
    print  "Codigo: ", tx.codigo, "Descripcion: ", tx.descripcion 