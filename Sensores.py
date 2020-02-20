import time
class Sensores:
        def __init__(self,aux1,aux2,chicas,medianas,grandes):
                self.aux1=aux1
                self.aux2=aux2
                self.chicas=chicas
                self.medianas=medianas
                self.grandes=grandes
        def sensor(self):
                print("***INGRESA***\nP.-Mostrar linea de produccion\nC.-Insertar Caja chica\nM.-Insertar Caja mediana\nG.-Insertar Caja grande\nX.-Cerrar programa")
                while(self.aux2!=0):
                        self.aux1='Z'
                        while(self.aux1!='P' and self.aux1!='C' and self.aux1!='M' and self.aux1!='G' and self.aux1!='X'):
                                self.aux1=input("Ingresa con letra mayusucula\n")
                        if(self.aux1=='C'):
                                self.chicas=self.chicas+1
                        if(self.aux1=='M'):
                                self.medianas=self.medianas+1
                        if(self.aux1=='G'):
                                self.grandes=self.grandes+1
                        if(self.aux1=='P'):
                                print("Datos adquiridos")
                                print("Numero Cajas chicas\t",self.chicas)
                                print("Numero Cajas medianas\t",self.medianas)
                                print("Numero Cajas grandes\t",self.grandes,"\n\n")
                        if(self.aux1=='X'):
                                self.aux2=0
 


