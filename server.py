# server.py
import Pyro4

@Pyro4.expose
class Server(object):
    def say_hello(self, name):
        return f"Hello, {name}!"

daemon = Pyro4.Daemon()                # crea un daemon Pyro4
uri = daemon.register(Server)   # registra la clase Greeter como un objeto Pyro

print(f"Ready. Object uri = {uri}")    # imprime la URI del objeto

daemon.requestLoop()                    # comienza el bucle del servidor
