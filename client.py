# client.py
import Pyro4

uri = input("Enter the uri of the server object: ").strip()   # pide al usuario la URI del objeto
server = Pyro4.Proxy(uri)                                      # obtén una instancia proxy del servidor

print(server.say_hello("World"))                               # llama al método say_hello en el objeto remoto
