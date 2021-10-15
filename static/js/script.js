
playerpers=[0,0]
var banlist=[]
function ban_dban(obj){

    if(obj.getAttribute("ban")){
        let ban=document.getElementById("ban")
        let dban=document.getElementById("dban")
        ban.hidden=true
        dban.hidden=false
    }
    else{
        let ban=document.getElementById("ban")
        let dban=document.getElementById("dban")
        ban.hidden=false
        dban.hidden=true
        }
}
function mudarslot(player,obj){
    slot=document.getElementById("op"+player+playerpers[player])
    slot.removeAttribute("selected")
    playerpers[player]=obj.getAttribute("value")
    slot=document.getElementById("op"+player+playerpers[player])
    slot.setAttribute("selected",true)
    var painel1=document.getElementById("slots"+player+"pers")
    var painel2=document.getElementById("slots"+player+"pet")
    if(playerpers[player]<((1+player)*4)){
        esconder(painel1,painel2)
        if(player>0){
            ban_dban(obj)
        }
    } 
    else{
        esconder(painel2,painel1)
    }
}
esconder=function(visible,hidden){
    visible.hidden=false
    hidden.hidden=true
}
function atribuirvalor(player,obj){
    if(!document.getElementById("op"+player+playerpers[player]).getAttribute("ban")){
        valor=obj.getAttribute("value")
            if( valor=="0"){
                valor=parseInt(valor)
            }
            src=obj.children[0].getAttribute("src")
            //console.log("p"+player+playerpers[player])
            inpP=document.getElementById("p"+player+playerpers[player])
            valorAnt=inpP.getAttribute("value")
            inpP.setAttribute("value",valor)
            slot=document.getElementById("op"+player+playerpers[player])
            slot.children[0].src=src
            
            //escondendo e mostrando
            
            if(valor!=0){
                let obj=document.getElementById("persIc"+player+valor);
                obj.setAttribute("disabled",true)   
                
                
            }
            let obj2=document.getElementById("persIc"+player+valorAnt);
                if(obj2&&obj2!=null){
                    obj2.removeAttribute("disabled")
                }
    }
    
           
}
function ban(){
    inpP=document.getElementById("op1"+playerpers[1])
    inputP=document.getElementById("p1"+playerpers[1])
    if(!inpP.getAttribute("ban") && playerpers[1]<8){
        let valor=inputP.getAttribute("value")
        if(valor!=0&&banlist.length<2 && banlist.indexOf(valor)<0){
            inpP.removeAttribute("selected")
            inpP.setAttribute("ban", true)
            banlist.push(valor)
            let ban=document.getElementById("ban")
            let dban=document.getElementById("dban")
            ban.hidden=true
            dban.hidden=false
        }
        inputBan=$("#p110")[0]
        inputBan.setAttribute("value",banlist.toString())
    }
    
    
}
function desban(){
    inpP=document.getElementById("op1"+playerpers[1])
    inputP=document.getElementById("p1"+playerpers[1])
    if(inpP.getAttribute("ban")){
        let valor=inputP.getAttribute("value")
    
        inpP.removeAttribute("ban")
        inpP.setAttribute("selected",true)
        
        let id=banlist.indexOf(valor)
        if(id>0){
            banlist.pop()
        }
        else{
            banlist.shift()
        }
        let ban=document.getElementById("ban")
        let dban=document.getElementById("dban")
        
        ban.hidden=false
        dban.hidden=true
        inputBan=$("#p110")[0]
        inputBan.setAttribute("value",banlist.toString())
    }
    
}
function filtrar(local,valor){
    
    var desativados=$("#slots"+local+"pet")[0].children
    
    for(var a =0;a<desativados.length;a++){
        
        desativados[a].hidden=true
        
        if(desativados[a].className==valor){
            desativados[a].hidden=false
        }
        
    }
     var desativados=$("#slots"+local+"pers")[0].children
    
    for(var a =0;a<desativados.length;a++){
        
        desativados[a].hidden=true
        
        if(desativados[a].className==valor){
            desativados[a].hidden=false
        }
    }
   
}