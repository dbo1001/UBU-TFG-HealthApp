# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:50:40 2018

@author: Jesus
"""
import pandas as pd;
import numpy as np;
import AdminBase as ab;
import vista as vs;
from tkinter import messagebox
import datetime
"""
Calcula el número de calorias que el usuario ha de gastar en base a:
   altura, peso, edad,sexo, actividad realizada y sus objetivos(bjar,subir o mantener peso)
"""
def calculoTMB(usuario):
    #Formula para calcular la tasa de metabolismo basal
    registroUsr = ab.cargaRegistroUsuario(usuario[0])
    TMB = (10*usuario[7])+(6.25*usuario[6])-(5*usuario[5])
    #Difrencia entre mujery ho,bre
    if(usuario[4] == 'H'):
        TMB=TMB+5
    else:
        TMB=TMB-161
    #Calculamos el TBM en base a la actividad que haga el usuario
    if(usuario[8]==1):
        TMB = TMB*1.2;
    elif(usuario[8]==2):
        TMB = TMB*1.375;
    elif(usuario[8]==3):
        TMB = TMB*1.55;
    elif(usuario[8]==4):
        TMB = TMB*1.725;
    elif(usuario[8]==5):
        TMB = TMB*1.9;
    else:
        TMB = "ERROR"
    #Por ultimo, el TBM son las calorias que el usuario gasta al dia aproximadas,
    #si quiere subir y bajar el restamos o sumamos el resto de calorias
    TMB=TMB+int(registroUsr['valor']);
    return TMB
def distribuciónDeMacronutrientes(kcal,tipoDieta):
    if (tipoDieta == 'normal'):
        '''
        En una dieta normal la distribución es:
            Hidratos = 50%
            Proteinas = 25%
            Grasas = 25%
        '''
        hidratos = kcal*0.55 
        proteinas = kcal*0.25
        grasas = kcal*0.20
        listMacDiarios = [kcal,hidratos,proteinas,grasas]
    elif (tipoDieta == 'baja en grasa'):
        hidratos = kcal*0.55
        proteinas = kcal*0.30
        grasas = kcal*0.15
        listMacDiarios = [kcal,hidratos,proteinas,grasas]
    elif (tipoDieta == 'alta en proteina'):
        hidratos = kcal*0.50
        proteinas = kcal*0.35
        grasas = kcal*0.15
        listMacDiarios = [kcal,hidratos,proteinas,grasas]
    elif (tipoDieta == 'baja en proteina'):
        hidratos = kcal*0.57
        proteinas = kcal*0.20
        grasas = kcal*0.23
        listMacDiarios = [kcal,hidratos,proteinas,grasas]
    elif (tipoDieta == 'alta en grasa'):
        hidratos = kcal*0.55
        proteinas = kcal*0.20
        grasas = kcal*0.25
        listMacDiarios = [kcal,hidratos,proteinas,grasas]
    return listMacDiarios
    
'''
Crear Función que te devuelva en diferentes arrays, las kcal, 
y gramos de comida correspondientes al desayuno, almuerzo, comida, merienda y cena
'''
def repartoDeKcal (kcalDiaria):
    desayuno = kcalDiaria*0.2475;
    almuerzo = kcalDiaria*0.135;
    comida = kcalDiaria*0.305;
    merienda = kcalDiaria*0.115;
    cena = kcalDiaria*0.1975;
    kcalDesAlmComMerCen = [desayuno,almuerzo,comida,merienda,cena];
    return kcalDesAlmComMerCen;
'''
Función que crea 5 listas con los alimentos que son desayunos, almuerzos, comidas, meriendas o cena respectivamente
RECORDATORIO: un alimento puede pertenecer perfectamente a varios grupos de comida a la vez.
'''
def listasPorTipo(listaDeAlimentos):
    desayuno = pd.DataFrame();
    almuerzo = pd.DataFrame();
    comida = pd.DataFrame();
    comida2  = pd.DataFrame();
    merienda = pd.DataFrame();
    cena = pd.DataFrame();
    for indice, comida in listaDeAlimentos.iterrows():
        if(int(comida["Tipo"])==31 or int(comida["Tipo"])==30 or int(comida["Tipo"])==29 or int(comida["Tipo"])==28 or int(comida["Tipo"])==27 or int(comida["Tipo"])==26 or int(comida["Tipo"])==25 or int(comida["Tipo"])==24 or int(comida["Tipo"])==23 or int(comida["Tipo"])==22 or int(comida["Tipo"])==21 or int(comida["Tipo"])==20 or int(comida["Tipo"])==19 or int(comida["Tipo"])==18 or int(comida["Tipo"])==17 or int(comida["Tipo"])==16):
            desayuno = desayuno.append(listaDeAlimentos.loc[indice]);
        if(int(comida["Tipo"])==8 or int(comida["Tipo"])==9 or int(comida["Tipo"])==10 or int(comida["Tipo"])==11 or int(comida["Tipo"])==12 or int(comida["Tipo"])==13 or int(comida["Tipo"])==14 or int(comida["Tipo"])==15 or int(comida["Tipo"])==24 or int(comida["Tipo"])==25 or int(comida["Tipo"])==26 or int(comida["Tipo"])==27 or int(comida["Tipo"])==28 or int(comida["Tipo"])==29 or int(comida["Tipo"])==30 or int(comida["Tipo"])==31):
            almuerzo = almuerzo.append(listaDeAlimentos.loc[indice]);
        if(int(comida["Tipo"])==4 or int(comida["Tipo"])==5 or int(comida["Tipo"])==6 or int(comida["Tipo"])==7 or int(comida["Tipo"])==12 or int(comida["Tipo"])==13 or int(comida["Tipo"])==14 or int(comida["Tipo"])==15 or int(comida["Tipo"])==20 or int(comida["Tipo"])==21 or int(comida["Tipo"])==22 or int(comida["Tipo"])==23 or int(comida["Tipo"])==28 or int(comida["Tipo"])==29 or int(comida["Tipo"])==30 or int(comida["Tipo"])==31):
            comida2 = comida2.append(listaDeAlimentos.loc[indice]);
        if(int(comida["Tipo"])==2 or int(comida["Tipo"])==3 or int(comida["Tipo"])==6 or int(comida["Tipo"])==7 or int(comida["Tipo"])==10 or int(comida["Tipo"])==11 or int(comida["Tipo"])==14 or int(comida["Tipo"])==15 or int(comida["Tipo"])==18 or int(comida["Tipo"])==19 or int(comida["Tipo"])==22 or int(comida["Tipo"])==23 or int(comida["Tipo"])==26 or int(comida["Tipo"])==27 or int(comida["Tipo"])==30 or int(comida["Tipo"])==31):
            merienda = merienda.append(listaDeAlimentos.loc[indice]);
        if(int(comida["Tipo"])==1 or int(comida["Tipo"])==3 or int(comida["Tipo"])==5 or int(comida["Tipo"])==7 or int(comida["Tipo"])==9 or int(comida["Tipo"])==11 or int(comida["Tipo"])==13 or int(comida["Tipo"])==15 or int(comida["Tipo"])==17 or int(comida["Tipo"])==19 or int(comida["Tipo"])==21 or int(comida["Tipo"])==23 or int(comida["Tipo"])==25 or int(comida["Tipo"])==27 or int(comida["Tipo"])==29 or int(comida["Tipo"])==31):
            cena = cena.append(listaDeAlimentos.loc[indice]);

    return desayuno, almuerzo, comida2, merienda, cena;

'''
Ordena la comida en base a la minima diferencia entre lo que debo comer y el 
objetivo que tengo para esta comida especifica
MEJORAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hay una función para que según el tipo de dieta te distribuya las kcalorias entre grasas. carbohidratos y proteinas.
Esa función no se usa en ningun momento, queda pendiente URGENTE de arreglar
En xxxDeber, debo hacer los calculos multiplicando las kilocalorias del macrinutriente especifico (Halladas en la función hablada antes) 
y multiplicarlo por el tanto por ciento  de grasas (por ejemplo) que he de comer en el desayuno (Y hacer el sumatorio como se hace hasta ahora)
además
El objetivo son las kcalorias por comida especifica, y se le multiplica el % del macronutriente que le corresponda.
'''
def OrdMinimaDiferencia(listComida,objetivo,tipoComida,dat,kcaldiarias,listMacDiarios):
    dif=0;
    listComida.loc[:,"dif"]=0;
    if(tipoComida == "desayuno"):
      #Es el tanto por ciento correspondiente a cada macronutriente en base al objetivo de la comida
      # Se calcula = %pesoMacronutrienteSobreKcalDiarias*100/%pesodelacomidadelmomentocar
      graDeber = listMacDiarios[3]*0.15
      carDeber = listMacDiarios[1]*0.3
      protDeber = listMacDiarios[2]*0.24
      #Objetivo = kcalorias que deberia comer en el desayuno (comida concretra)
      carb = graDeber
      gra = carDeber
      prot = protDeber
    #PENDIENTE DE CALCULAR EL RESTO DE COMIDAS EMPEZANDO POR AQUI
    elif(tipoComida == "almuerzo"):
      graDeber = listMacDiarios[3]*0.25
      carDeber = listMacDiarios[1]*0.55
      protDeber = listMacDiarios[2]*0.28
      #deber = objetivo+kcaldiarias*0.135
      carb = listMacDiarios[3]*0.10
      gra = listMacDiarios[1]*0.25
      prot = listMacDiarios[2]*0.14
    elif(tipoComida == "comida"):
      graDeber = listMacDiarios[3]*0.45
      carDeber =listMacDiarios[1]*0.80
      protDeber = listMacDiarios[2]*0.62
      #deber = objetivo+kcaldiarias*0.135+kcaldiarias*0.305
      carb = listMacDiarios[3]*0.2
      gra = listMacDiarios[1]*0.25
      prot = listMacDiarios[2]*0.24
    elif(tipoComida == "merienda"):
      graDeber = listMacDiarios[3]*0.65
      carDeber = listMacDiarios[1]*0.9
      protDeber = listMacDiarios[2]*0.76
      #deber = objetivo+kcaldiarias*0.135+kcaldiarias*0.305+kcaldiarias*0.115
      carb = listMacDiarios[3]*0.2
      gra = listMacDiarios[1]*0.1
      prot = listMacDiarios[2]*0.14
    else:
      #Acumulado
      graDeber = listMacDiarios[3]
      carDeber = listMacDiarios[1]
      protDeber = listMacDiarios[2]
      #Propio de esta comida
      carb = listMacDiarios[3]*0.35
      gra = listMacDiarios[1]*0.10
      prot = listMacDiarios[2]*0.24
    for i,comida in listComida.iterrows():        
        dif = np.abs(formulDif(dat,carb,prot,gra,comida,objetivo,carDeber,graDeber,protDeber))
        #dif = abs(objetivo-int(comida["Calorias"]))
        listComida["dif"].loc[i]=dif
    listComida = listComida.sort_values(by=['dif'],ascending=False)
    return listComida;

def formulDif(loQueLlevo,carb,prot,gras,comida,deboComida,carDeber,graDeber,protDeber):
    if ((carDeber-loQueLlevo[1]*4) >= 0 ):
        comidaCarb = (carDeber-loQueLlevo[2]*4)/(carb-(comida["Hidratos"]*4)+(deboComida-(comida["Calorias"])))
    else:
        comidaCarb=0;
    if ((protDeber-loQueLlevo[2]*4) >= 0 ):
        comidaPro = (protDeber-loQueLlevo[3]*4)/(prot-(comida["Proteina"]*4)+(deboComida-(comida["Calorias"])))
    else:
        comidaPro=0;
    if ((graDeber-loQueLlevo[3]*8)>= 0 ):
        comidaGra = (graDeber-loQueLlevo[1]*8)/(gras-(comida["Grasa"]*8)+(deboComida-(comida["Calorias"])))
    else:
        comidaGra=0;
    return (comidaCarb+comidaPro+comidaGra)/3
'''
Funcion que te reparte lo sobrante entre las comidas que quedan
POSIBLE MEJORA: Que te reparta de manera proporcional a la importancia de la comida
es decir si sobran 40 kcal en el desayuno, que no se repartan equitativamente sino que la comida
tenga 15 y el almuerzo 5 (por ejemplo)
'''
def repartoKcalSobrantes(kcal,listakcalcomidas, comida):
    cont=0;
    if(comida == "desayuno"):
        cont = (int(listakcalcomidas[0])-int(kcal))/4;
        listakcalcomidas[1] = listakcalcomidas[1] + cont
        listakcalcomidas[2] = listakcalcomidas[2] + cont
        listakcalcomidas[3] = listakcalcomidas[3] + cont
        listakcalcomidas[4] = listakcalcomidas[4] + cont
    elif (comida == "almuerzo"):
        cont = (int(listakcalcomidas[1])-int(kcal))/3;
        listakcalcomidas[2] = listakcalcomidas[2] + cont
        listakcalcomidas[3] = listakcalcomidas[3] + cont
        listakcalcomidas[4] = listakcalcomidas[4] + cont
    elif(comida == "comida"):
        cont = (int(listakcalcomidas[2])-int(kcal))/2
        listakcalcomidas[3] = listakcalcomidas[3] + cont
        listakcalcomidas[4] = listakcalcomidas[4] + cont
    elif(comida == "merienda"):
        cont = (int(listakcalcomidas[3])-int(kcal))
        listakcalcomidas[4] = listakcalcomidas[4] + cont       
    return listakcalcomidas
'''
Función que realiza los calculos necesarios para mostrarte por pantalla tu mejoría 
en cuanto a la media del día de calidad entre todas las comidas
'''
def graficoTotal(selfi,hojaAlimentos):

    fechas = [];
    medias = [];
    mes = 0
    for index,dias in selfi.histUA.iterrows():
        if (mes == 30):
            exit
        mes+=1
        fecha = datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d')
        fechas.append(fecha.strftime("%m-%d"))
        container =0;
        contador = 0;
        if not (pd.isnull(dias['Desayuno'])):
            fila=ab.getFilaAlimento(dias['Desayuno'],hojaAlimentos)
            container+=hojaAlimentos["Calidad"].loc[fila]
            contador+=1
        if not (pd.isnull(dias['Almuerzo'])):
            fila=ab.getFilaAlimento(dias['Almuerzo'],hojaAlimentos)
            container+=hojaAlimentos["Calidad"].loc[fila]
            contador+=1
        if not (pd.isnull(dias['Comida'])):
            fila=ab.getFilaAlimento(dias['Comida'],hojaAlimentos)
            container+=hojaAlimentos["Calidad"].loc[fila]
            contador+=1
        if not (pd.isnull(dias['Merienda'])):
            fila=ab.getFilaAlimento(dias['Merienda'],hojaAlimentos)
            container+=hojaAlimentos["Calidad"].loc[fila]
            contador+=1
        if not (pd.isnull(dias['Cena'])):
            fila=ab.getFilaAlimento(dias['Cena'],hojaAlimentos)
            container+=hojaAlimentos["Calidad"].loc[fila]
            contador+=1
        medias.append(container/contador)
        
    vs.gráfico(selfi,fechas,medias,-1)
'''
Función que te muestra por pantalla los gráficos en base a la calidad y los días, de una 
comida concreta del usuario, para ver mas al detalle los avances.
Coge como parametros selfi (Tronco o raiz de la clase padre con todos sus argumentos), hoja de alimentos (para buscar sus caracteristicas), 
y bandera para ver que tipo de comida es
'''
def graficoMejoraComida(selfi,hojaAlimentos, bandera):
    
    fechas = [];
    medias = [];
    mes = 0
    for index,dias in selfi.histUA.iterrows():
        if (mes == 30):
            exit
        mes+=1
        #fecha = datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d')
        
        if(bandera == 0):
            if not (pd.isnull(dias['Desayuno'])):
                #fechas.append(datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d').day)
                fecha = datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d')
                fechas.append(fecha.strftime("%m-%d"))
                fila=ab.getFilaAlimento(dias['Desayuno'],hojaAlimentos)
                container=hojaAlimentos["Calidad"].loc[fila]
                medias.append(container)
        elif(bandera == 1):
            if not (pd.isnull(dias['Almuerzo'])):
                fecha = datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d')
                fechas.append(fecha.strftime("%m-%d"))
                fila=ab.getFilaAlimento(dias['Almuerzo'],hojaAlimentos)
                container=hojaAlimentos["Calidad"].loc[fila]
                medias.append(container)
        elif(bandera == 2):
            if not (pd.isnull(dias['Comida'])):
                fecha = datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d')
                fechas.append(fecha.strftime("%m-%d"))
                fila=ab.getFilaAlimento(dias['Comida'],hojaAlimentos)
                container=hojaAlimentos["Calidad"].loc[fila]
                medias.append(container)
        elif(bandera == 3):
            if not (pd.isnull(dias['Merienda'])):
                fecha = datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d')
                fechas.append(fecha.strftime("%m-%d"))
                fila=ab.getFilaAlimento(dias['Merienda'],hojaAlimentos)
                container=hojaAlimentos["Calidad"].loc[fila]
                medias.append(container)
        elif(bandera == 4):
            if not (pd.isnull(dias['Cena'])):
                fecha = datetime.datetime.strptime(dias['Fecha'], '%Y-%m-%d')
                fechas.append(fecha.strftime("%m-%d"))
                fila=ab.getFilaAlimento(dias['Cena'],hojaAlimentos)
                container=hojaAlimentos["Calidad"].loc[fila]
                medias.append(container)
    vs.gráfico(selfi,fechas,medias,bandera)
'''
Hace los calculos correspondientes a la hora de añadir un nuevo menu, sumando todos los macronutrientes y los alimentos, 
creando el plato completo y llevando a cabo los calculos para identificar la calidad en base a NUTRISCORE.
'''
def AñadirMenuCalculos(selfi):
    bandera=0
    error=False;
    nAlimento = [False, False, False, False, False]
    proporcion1=0;proporcion2=0; proporcion3=0;proporcion4=0;
    kcal1=0;kcal2=0;kcal3=0;kcal4=0;
    grasas1=0;grasas2=0;grasas3=0;grasas4=0;
    saturadas1=0;saturadas2=0;saturadas3=0;saturadas4=0
    hidratos1=0;hidratos2=0;hidratos3=0;hidratos4=0;
    fibra1=0;fibra2=0;fibra3=0;fibra4=0;
    azucar1=0;azucar2=0;azucar3=0;azucar4=0;
    proteinas1=0;proteinas2=0;proteinas3=0;proteinas4=0;
    sodio1=0.0;sodio2=0.0;sodio3=0.0;sodio4=0.0;
    cal1=0;cal2=0;cal3=0;cal4=0;
    arrayCalidad=[]
    kcalTotal=0;
    grasasTotal=0;
    saturadasTotal=0;
    hidratosTotal=0;
    fibraTotal=0;
    azucarTotal=0;
    proteinasTotal=0;
    sodioTotal=0;
    nombre="";
    tipo=None;
    #ALIMENTO #1
    if(len(selfi.entry_Nom.get()) != 0 or len(selfi.entry_Gram.get()) !=0 or len(selfi.entry_kcal.get()) != 0 or len(selfi.entry_gras.get()) != 0 or len(selfi.entry_sat.get()) != 0 or len(selfi.entry_Hid.get()) != 0 or len(selfi.entry_Azuc.get()) != 0 or len(selfi.entry_Pro.get()) != 0  ):
        if(len(selfi.entry_Nom.get()) ==0 or len(selfi.entry_Gram.get()) ==0 or len(selfi.entry_kcal.get()) == 0 or len(selfi.entry_gras.get()) == 0 or len(selfi.entry_sat.get()) == 0 or len(selfi.entry_Hid.get()) == 0 or len(selfi.entry_Azuc.get()) == 0 or len(selfi.entry_Pro.get()) == 0 ):
            selfi.label_Error.config(text="ERROR: Algun dato erroneo del alimento #1")
            error=True;
        else:
            nAlimento[0]= True
            bandera = 1;
    #ALIMENTO #2
    if(len(selfi.entry_Nom2.get()) != 0 or len(selfi.entry_Gram2.get()) !=0 or len(selfi.entry_kcal2.get()) != 0 or len(selfi.entry_gras2.get()) != 0 or len(selfi.entry_sat2.get()) != 0 or len(selfi.entry_Hid2.get()) != 0 or len(selfi.entry_Azuc2.get()) != 0 or len(selfi.entry_Pro2.get()) != 0):
        if(len(selfi.entry_Nom2.get()) ==0 or len(selfi.entry_Gram2.get()) ==0 or len(selfi.entry_kcal2.get()) == 0 or len(selfi.entry_gras2.get()) == 0 or len(selfi.entry_sat2.get()) == 0 or len(selfi.entry_Hid2.get()) == 0 or len(selfi.entry_Azuc2.get()) == 0 or len(selfi.entry_Pro2.get()) == 0):
            selfi.label_Error.config(text="ERROR: Algun dato erroneo del alimento #2")
            error=True;
        else:
            nAlimento[1]= True
            bandera = 1;
    #ALIMENTO #3
    if(len(selfi.entry_Nom3.get()) != 0 or len(selfi.entry_Gram3.get()) !=0 or len(selfi.entry_kcal3.get()) != 0 or len(selfi.entry_gras3.get()) != 0 or len(selfi.entry_sat3.get()) != 0 or len(selfi.entry_Hid3.get()) != 0 or len(selfi.entry_Azuc3.get()) != 0 or len(selfi.entry_Pro3.get()) != 0):
        if(len(selfi.entry_Nom3.get()) ==0 or len(selfi.entry_Gram3.get()) ==0 or len(selfi.entry_kcal3.get()) == 0 or len(selfi.entry_gras3.get()) == 0 or len(selfi.entry_sat3.get()) == 0 or len(selfi.entry_Hid3.get()) == 0 or len(selfi.entry_Azuc3.get()) == 0 or len(selfi.entry_Pro3.get()) == 0):
            selfi.label_Error.config(text="ERROR: Algun dato erroneo del alimento #3")
            error=True;
        else:
            nAlimento[2]= True
            bandera = 1;
    #ALIMENTO #4
    if(len(selfi.entry_Nom4.get()) != 0 or len(selfi.entry_Gram4.get()) !=0 or len(selfi.entry_kcal4.get()) != 0 or len(selfi.entry_gras4.get()) != 0 or len(selfi.entry_sat4.get()) != 0 or len(selfi.entry_Hid4.get()) != 0 or len(selfi.entry_Azuc4.get()) != 0 or len(selfi.entry_Pro4.get()) != 0 ):
        if(len(selfi.entry_Nom4.get()) ==0 or len(selfi.entry_Gram4.get()) ==0 or len(selfi.entry_kcal4.get()) == 0 or len(selfi.entry_gras4.get()) == 0 or len(selfi.entry_sat4.get()) == 0 or len(selfi.entry_Hid4.get()) == 0 or len(selfi.entry_Azuc4.get()) == 0 or len(selfi.entry_Pro4.get()) == 0 ):
            selfi.label_Error.config(text="ERROR: Algun dato erroneo del alimento #4")
            error=True;                         
        else:
            nAlimento[3]= True
            bandera = 1;
    if(bandera==0):
        selfi.label_Error.config(text="ERROR: Rellene algún alimento")
        error=True;
    elif(selfi.varDes.get() == 0 and selfi.varAlm.get() == 0 and selfi.varCom.get() == 0 and selfi.varMer.get() == 0 and selfi.varCen.get() == 0 ):
        selfi.label_Error.config(text="ERROR: Seleccione que tipo de comida es")
        error=True;
    else:
        try:
            if(nAlimento[0]):
                float(selfi.entry_kcal.get())
                float(selfi.entry_Gram.get())
                float(selfi.entry_gras.get())
                float(selfi.entry_sat.get())
                float(selfi.entry_Hid.get())
                float(selfi.entry_Azuc.get())
                float(selfi.entry_Pro.get())
            if(nAlimento[1]):
                float(selfi.entry_kcal2.get())
                float(selfi.entry_Gram2.get())
                float(selfi.entry_gras2.get())
                float(selfi.entry_sat2.get())
                float(selfi.entry_Hid2.get())
                float(selfi.entry_Azuc2.get())
                float(selfi.entry_Pro2.get())
            if(nAlimento[2]):
                float(selfi.entry_kcal3.get())
                float(selfi.entry_Gram3.get())
                float(selfi.entry_gras3.get())
                float(selfi.entry_sat3.get())
                float(selfi.entry_Hid3.get())
                float(selfi.entry_Azuc3.get())
                float(selfi.entry_Pro3.get())
            if(nAlimento[3]):
                float(selfi.entry_kcal4.get())
                float(selfi.entry_Gram4.get())
                float(selfi.entry_gras4.get())
                float(selfi.entry_sat4.get())
                float(selfi.entry_Hid4.get())
                float(selfi.entry_Azuc4.get())
                float(selfi.entry_Pro4.get())  
            selfi.label_Error.config(text="")
            #FIN DE LAS PRUEBAS DE ERROR
            #############################
            #INICIO DE LOS CALCULOS
            if(nAlimento[0]):
                proporcion1 = float(selfi.entry_Gram.get())/100
                kcal1=float(selfi.entry_kcal.get())*proporcion1;
                gramos1 = selfi.entry_Gram;
                nombre+=str(gramos1.get())+" gr de "+selfi.entry_Nom.get()
                grasas1=float(selfi.entry_gras.get())*proporcion1;
                saturadas1=float(selfi.entry_sat.get())*proporcion1;
                hidratos1=float(selfi.entry_Hid.get())*proporcion1;
                fibra1=float(selfi.entry_Fibra.get())*proporcion1
                azucar1=float(selfi.entry_Azuc.get())*proporcion1;
                proteinas1=float(selfi.entry_Pro.get())*proporcion1;
                sodio1=float(selfi.entry_Sod.get())*proporcion1;
            if(nAlimento[1]):
                proporcion2 = float(selfi.entry_Gram2.get())/100
                kcal2=float(selfi.entry_kcal2.get())*proporcion2;
                gramos2 = selfi.entry_Gram2;
                nombre+=" + "+str(gramos2.get())+" gr de "+selfi.entry_Nom2.get()
                grasas2=float(selfi.entry_gras2.get())*proporcion2;
                saturadas2=float(selfi.entry_sat2.get())*proporcion2;
                hidratos2=float(selfi.entry_Hid2.get())*proporcion2;
                fibra2=float(selfi.entry_Fibra2.get())*proporcion2
                azucar2=float(selfi.entry_Azuc2.get())*proporcion2;
                proteinas2=float(selfi.entry_Pro.get())*proporcion2;
                sodio2=float(selfi.entry_Sod2.get())*proporcion2;
            if(nAlimento[2]):
                proporcion3 = float(selfi.entry_Gram3.get())/100
                kcal3 = float(selfi.entry_kcal3.get())*proporcion3;
                gramos3 = selfi.entry_Gram3;
                nombre+=" + "+str(gramos3.get())+" gr de "+selfi.entry_Nom3.get()
                grasas3 = float(selfi.entry_gras3.get())*proporcion3;
                saturadas3=float(selfi.entry_sat3.get())*proporcion3;
                hidratos3=float(selfi.entry_Hid3.get())*proporcion3;
                fibra3=float(selfi.entry_Fibra3.get())*proporcion3
                azucar3=float(selfi.entry_Azuc3.get())*proporcion3;
                proteinas3=float(selfi.entry_Pro3.get())*proporcion3;
                sodio3=float(selfi.entry_Sod3.get())*proporcion3;
            if(nAlimento[3]):
                proporcion4 = float(selfi.entry_Gram4.get())/100
                kcal4=float(selfi.entry_kcal4.get())*proporcion4;
                gramos4 = selfi.entry_Gram4;
                nombre+=" + "+str(gramos4.get())+" gr de "+selfi.entry_Nom4.get()
                grasas4=float(selfi.entry_gras4.get())*proporcion4;
                saturadas4=float(selfi.entry_sat4.get())*proporcion4;
                hidratos4=float(selfi.entry_Hid4.get())*proporcion4;
                fibra4=float(selfi.entry_Fibra4.get())*proporcion4
                azucar4=float(selfi.entry_Azuc4.get())*proporcion4;
                proteinas4=float(selfi.entry_Pro4.get())*proporcion4;
                sodio4=float(selfi.entry_Sod4.get())*proporcion4;
            #Llamada a la función del calculo nutriscore
            if(nAlimento[0]):
                cal1=algoritmoNutriscore(float(selfi.entry_kcal.get()),float(selfi.entry_Azuc.get()),float(selfi.entry_sat.get()),float(selfi.entry_Fibra.get()),float(selfi.entry_Pro.get()),float(selfi.entry_Sod.get()))
                arrayCalidad.append(cal1)
            if(nAlimento[1]):
                cal2=algoritmoNutriscore(float(selfi.entry_kcal2.get()),float(selfi.entry_Azuc2.get()),float(selfi.entry_sat2.get()),float(selfi.entry_Fibra2.get()),float(selfi.entry_Pro2.get()),float(selfi.entry_Sod2.get()))
                arrayCalidad.append(cal2)
            if(nAlimento[2]):
                cal3=algoritmoNutriscore(float(selfi.entry_kcal3.get()),float(selfi.entry_Azuc3.get()),float(selfi.entry_sat3.get()),float(selfi.entry_Fibra3.get()),float(selfi.entry_Pro3.get()),float(selfi.entry_Sod3.get()))
                arrayCalidad.append(cal3)
            if(nAlimento[3]):
                cal4=algoritmoNutriscore(float(selfi.entry_kcal4.get()),float(selfi.entry_Azuc4.get()),float(selfi.entry_sat4.get()),float(selfi.entry_Fibra4.get()),float(selfi.entry_Pro4.get()),float(selfi.entry_Sod4.get()))
                arrayCalidad.append(cal4)
            #Sumatorio de los resultados recogidos a lo largo de la funcion:
            tipo= stringTipoToNumber(selfi.varDes.get(),selfi.varAlm.get(),selfi.varCom.get(),selfi.varMer.get(),selfi.varCen.get())
            kcalTotal=kcal1+kcal2+kcal3+kcal4;
            grasasTotal=grasas1+grasas2+grasas3+grasas4;
            saturadasTotal=saturadas1+saturadas2+saturadas3+saturadas4;
            hidratosTotal=hidratos1+hidratos2+hidratos3+hidratos4;
            fibraTotal=fibra1+fibra2+fibra3+fibra4;
            azucarTotal=azucar1+azucar2+azucar3+azucar4;
            proteinasTotal=proteinas1+proteinas2+proteinas3+proteinas4;
            #calidad=(cal1+cal2+cal3+cal4)/4
            sodioTotal=sodio1+sodio2+sodio3+sodio4
            
            return nombre, kcalTotal,grasasTotal, saturadasTotal,hidratosTotal, fibraTotal,azucarTotal,proteinasTotal,sodioTotal,tipo, arrayCalidad, error
        except ValueError:
            selfi.label_Error.config(text="ERROR: Inserte un valor numerico válido")
            error=True;
        except:
            selfi.label_Error.config(text="ERROR INESPERADO")
            error=True;

'''
Función que toma un "conjunto de bits" y te los transforma a un número entero, para
ser almacenados y procesados por la base de datos.
'''
def stringTipoToNumber(des,alm,com,mer,cen):
    intTipo=0;
    if(des == 1):
        intTipo+=16
    if(alm==1):
        intTipo+=8
    if(com==1):
        intTipo+=4
    if(mer==1):
        intTipo+=2
    if(cen==1):
        intTipo+=1
    return intTipo;
'''
Función que coge como parametros la información nutricional necesaria para realizar
el algoritmo Nutriscore del semaforo y lo realiza, dando como resultado un número del 1 al 5 
que seria el color del semaforo como tal.
Esto se realiza haciendo una criba de las difetentes caracteristicas
'''
def algoritmoNutriscore(kcal, azucar, saturadas,fibra, proteina,sodio):
    #1 kilocaloria = 4,19 kilojulios
    kj = float(kcal) * 4.18;
    #Variable de los resultados negativos
    A=0;
    #Variable para los nutrientes buenos
    C=0;
    #Puntuación kilojulios
    if(kj <= 335):
        A+=0
    elif(kj > 3350):
        A+=10
    elif(kj > 3015):
        A+=9
    elif(kj > 2680):
        A+=8
    elif(kj > 2345):
        A+=7
    elif(kj > 2010):
        A+=6
    elif(kj > 1675):
        A+=5
    elif(kj > 1340):
        A+=4
    elif(kj > 1005):
        A+=3
    elif(kj > 670):
        A+=2
    elif(kj > 335):
        A+=1
    #Puntuación azucares
    if(azucar <= 4.5):
        A+=0
    elif(azucar > 45):
        A+=10
    elif(azucar > 40):
        A+=9
    elif(azucar > 36):
        A+=8
    elif(azucar > 31):
        A+=7
    elif(azucar > 27):
        A+=6
    elif(azucar > 22.5):
        A+=5
    elif(azucar > 18):
        A+=4
    elif(azucar > 13.5):
        A+=3
    elif(azucar > 9):
        A+=2
    elif(azucar > 4.5):
        A+=1
    #Putuacion Grasas saturadas
    if(saturadas > 10):
        A+=10
    elif(saturadas > 9):
        A+=9
    elif(saturadas > 8):
        A+=8
    elif(saturadas > 7):
        A+=7
    elif(saturadas > 6):
        A+=6
    elif(saturadas > 5):
        A+=5
    elif(saturadas > 4):
        A+=4
    elif(saturadas > 3):
        A+=3
    elif(saturadas > 2):
        A+=2
    elif(saturadas > 1):
        A+=1
    #Puntuacion SODIO
    if(sodio>900):
        A+=10
    elif(sodio>810):
        A+=9
    elif(sodio>810):
        A+=8
    elif(sodio>720):
        A+=7
    elif(sodio>630):
        A+=6
    elif(sodio>540):
        A+=5
    elif(sodio>450):
        A+=4
    elif(sodio>360):
        A+=3
    elif(sodio>270):
        A+=2
    elif(sodio>180):
        A+=1
    #### PUNTUACION BUENA ####
    #PROTEINA
    if(proteina>8):
        C+=5
    elif(proteina>6.4):
        C+=4
    elif(proteina>4.8):
        C+=3
    elif(proteina>3.2):
        C+=2
    elif(proteina>1.6):
        C+=1
    #FIBRA
    if(fibra>3.5):
        C+=5
    elif(fibra>2.8):
        C+=4
    elif(fibra>2.1):
        C+=3
    elif(fibra>1.4):
        C+=2
    elif(fibra>0.7):
        C+=1
    #Ponderación final del resultado
    if(A<11):
        total= A-C
    else:
        total= A-C
    if(total < 0 ):
        calidad=1;
    elif(total >=0 and total <=2):
        calidad=2;
    elif(total > 2 and total <=10):
        calidad=3;
    elif(total>10 and total <=18):
        calidad=4;
    else:
        calidad=5;
    return calidad;
        