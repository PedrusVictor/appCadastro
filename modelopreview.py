import pandas as pd

import pickle


        


class BuscTime():
    def InicializarRem(self):
        vitoriosos={}
        derrotas={}
        for a,b,res in self.dataset[["rem1","rem2","resultado"]].values:
            if res==1:
                vitoriosos[a]=vitoriosos.get(a,0)+1
    
                vitoriosos[b]=vitoriosos.get(b,0)+1
            else:
                derrotas[a]=derrotas.get(a,0)+1

                derrotas[b]=derrotas.get(b,0)+1
            
        
        rem={}
        for a in vitoriosos.keys():
            rem[a]=(vitoriosos[a]/(vitoriosos[a]+derrotas.get(a,0)))

        return (sorted(rem,key=rem.get,reverse=True))
    
    def BuscarRemovidos(self,lista):
        removidos=[]
        cont=0
        for r in self.RankRem:
            if cont>1:
                break
            if r in lista:
                cont+=1
                removidos.append(r)
                
        return removidos
    
    def Time():
        pickle_in = open("modelo.pickle","rb")
        preview = pickle.load(pickle_in)
        return(preview)


    def __init__(self,chaveNum,chaveNom,dataset,tree,ids):
        import pandas as pd
        from sklearn.neighbors import KDTree
        self.dataset=dataset
        self.chaveNum=chaveNum.copy();#retorna o numero
        self.chaveNom=chaveNom.copy();#retorna o nome
        self.ids=ids
        self.tree=tree
        self.RankRem=self.InicializarRem()
        
    
        #pd.concat([datasetcopy["rem1"],datasetcopy["rem2"]]).value_counts()
        
    def MontarTime(self,timeinimigo):
        
        
        alvo=self.ConverterCompNum(timeinimigo)
        alvoc=alvo.copy()
        
        resultado=self.dataset.loc[(self.dataset.p2pers1==alvo[0])&(self.dataset.p2pers2==alvo[1])&(self.dataset.p2pers3==alvo[2])&(self.dataset.p2pers4==alvo[3])&
               (self.dataset.p2pers5==alvo[4])&(self.dataset.p2pers6==alvo[5])&(self.dataset.p2pers7==alvo[6])&(self.dataset.p2pers8==alvo[7])
               ]
        if(resultado.shape[0]==0):
            
            dist, ind = self.tree.query([alvo], k=1)
            ind=self.ids[ind[0][0]]
            
            alvo=self.dataset.loc[self.dataset.index[ind]]
            alvo=alvo.values[6:-2]
           
            #print(alvo[0])
            resultado=self.dataset.loc[(self.dataset.p2pers1==alvo[0])&(self.dataset.p2pers2==alvo[1])
                &(self.dataset.p2pers3==alvo[2])&(self.dataset.p2pers4==alvo[3])&
               (self.dataset.p2pers5==alvo[4])&(self.dataset.p2pers6==alvo[5])
                &(self.dataset.p2pers7==alvo[6])&(self.dataset.p2pers8==alvo[7])]
            
        
        r=resultado[["p1pers1","p1pers2","p1pers3","p1pers4","petplayer","resultado"]]
        
        colunas=r[r.columns[:-1]].value_counts().to_dict()
        
        times={}
        timesVitoriosos=r.loc[r["resultado"]==1][r.columns[:-1]].value_counts().to_dict()
       
        for a in timesVitoriosos.keys():
            times[a]=timesVitoriosos[a]/colunas[a]
        
        
        timeRemovido=self.BuscarRemovidos(alvoc)
        
             
        
        timeescolhido=(sorted(times,key=times.get,reverse=True))[0]
        
        
        
        
        saida=[self.chaveNom[a] for a in timeescolhido]
        
        return [saida,self.ConverterNumComp(timeRemovido)]
        
        #return 5

    def ConverterCompNum(self,time):
        
        timec=list(map(lambda s: s.lower() if type(s) == str else s,time))
        
        saida=[self.chaveNum[a] for a in timec]
   
        return saida

    def ConverterNumComp(self,time):
        
        saida=[self.chaveNom[a] for a in time]
        
   
        return saida

