from datetime import datetime


class Log:

    def __init__(self, manipuladores):
        self.__manipuladores = set(manipuladores)

    def adicionar_manipulador(self, manipulador):
        self.__manipuladores.add(manipulador)

    def info(self, message):
        self.__log("INFO", message)

    def alerta(self, message):
        self.__log("ALERTA", message)

    def erro(self, message):
        self.__log("ERRO", message)

    def debug(self, message):
        self.__log("DEBUG", message)

    def __log(self, level, message):
        for manipulador in self.__manipuladores:
            manipulador.log(self.__formatar(level, message))

    def __formatar(self, level, message):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"[{level} - {date}]: {message}"
