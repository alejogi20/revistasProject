class Revista:
    def __init__(self, serial, titulo, precio, stock, enStock = True):
         self._serial = serial
         self._titulo = titulo
         self._precio = precio
         self._stock = stock
         self._enStock = enStock        
    
    def get_serial(self):
        return self._serial
      
    def set_serial(self, serialNumero):
        self._serial = serialNumero

    def get_titulo(self):
        return self._titulo
      
    def set_titulo(self, tituloRevista):
        self._titulo = tituloRevista

    def get_precio(self):
        return self._precio
      
    def set_precio(self, precioRevista):
        self._precio = precioRevista

    def get_stock(self):
        return self._stock

    def set_stock(self, stockRevista):
        self._stock = stockRevista
    
    def get_enStock(self):
        return self._enStock

    def set_enStock(self, stockRevista):
        self._enStock = stockRevista
