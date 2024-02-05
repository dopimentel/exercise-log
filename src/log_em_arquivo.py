import os
from src.manipulador_de_log import ManipuladorDeLog

log_path = os.path.join("data", "log.txt")
print(log_path)
path = os.path.abspath(log_path)
print(path)


class LogEmArquivo(ManipuladorDeLog):

    @classmethod
    def log(cls, msg):

        with open(path, "a") as arquivo:

            print(msg, file=arquivo)
