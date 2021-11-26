class Registro:
    def __init__(self, rrc, valor, enStock = True):
        self._rrc = rrc
        self._valor = valor
        self._enStock = enStock 

    def get_rrc(self):
        return self._rrc
      
    def set_rrc(self, rrc):
        self._rrc = rrc

    def get_valor(self):
        return self._valor
      
    def set_valor(self, valor):
        self._valor = valor

    def get_enStock(self):
        return self._enStock

    def set_enStock(self, stockRevista):
        self._enStock = stockRevista