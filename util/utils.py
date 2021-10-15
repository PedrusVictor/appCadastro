import os
def buscaricones(caminho):
    #print(caminho)
    listaobj=[a for a in os.walk(caminho)]
    
    
    return [a.split(".")[0] for a in listaobj[0][2]]