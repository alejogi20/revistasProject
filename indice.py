#define la estructura de datos indice
from registro import Registro

class Indice:

    #el atributo tablaPrincipal es un bool que es false si no es la tabla principal, es decir,
    # no es la tabla donde guardaremos las revistas. Si es true entonces es la tabla principal y
    # por ello no le aplicamos ningun algoritmo search ni sort 
    #  
    def __init__(self, tabla = [], tablaPrincipal=False):
        self._tabla = tabla
        self._tablaPrincipal = tablaPrincipal

    def get_tabla(self):
        return self._tabla
      
    def set_tabla(self, newTabla):
        self._tabla = newTabla
    
    def get_tablaPrincipal(self):
        return self._tablaPrincipal
      
    def set_tablaPrincipal(self, tablaPrincipal):
        self._tablaPrincipal = tablaPrincipal


    def sort(self):
        if not self.get_tablaPrincipal():
            self.set_tabla(self.quickSort(self.get_tabla()))    

    def quickSort(self, arreglo) -> list:
        if len(arreglo) == 1:
            return arreglo
        if len(arreglo) < 2:
            return arreglo
        indicePivote = len(arreglo)//2
        listaPivote = list()
        pivote = arreglo[indicePivote]
        menores = list()
        mayores = list()
        for element in arreglo:
            if str(element.get_valor()) < str(pivote.get_valor()):
                menores.append(element)
            elif str(element.get_valor()) > str(pivote.get_valor()):
                mayores.append(element)
            else:
                listaPivote.append(element)
                
       
        arreglo = self.quickSort(menores) + listaPivote + self.quickSort(mayores)
        
        return arreglo

    def busquedaBinaria(self, valor, arreglo = None): 
        if(arreglo is None):
            arreglo = self.get_tabla()
        
        rrc = []
        if len(arreglo) == 0:
            return rrc

        
        indice = len(arreglo)//2
        
        if valor == arreglo[indice].get_valor():
            auxIndex = indice
            
            if arreglo[indice].get_enStock():    
                rrc.append(arreglo[indice].get_rrc())

            while indice - 1 >= 0:
                indice -= 1
                if valor == arreglo[indice].get_valor() and arreglo[indice].get_enStock():
                    rrc.append(arreglo[indice].get_rrc())
            
            indice = auxIndex

            while indice + 1 <= len(arreglo) - 1:
                indice += 1
                if valor == arreglo[indice].get_valor() and arreglo[indice].get_enStock():
                    rrc.append(arreglo[indice].get_rrc())
            
        elif len(arreglo) == 1:
            return rrc

        elif str(valor) < str(arreglo[indice].get_valor()):
            arreglo = arreglo[:indice]
            rrc = self.busquedaBinaria(valor, arreglo)
        elif str(valor) > str(arreglo[indice].get_valor()):
            arreglo = arreglo[(indice + 1):]
            rrc = self.busquedaBinaria(valor, arreglo)
       

        return rrc   

    


