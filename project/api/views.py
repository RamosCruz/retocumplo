
from django.http import HttpResponse
from django.shortcuts import render
from .form import HomeForm
import requests
import json


#from . import views
# Create your views here.

def Home(request):
    form = HomeForm()
    return render(request, 'home.html', {'form': form})

def Consultar(request):

    fechaIni = request.GET["fechaIni"]
    fechaFin = request.GET["fechaFin"]
    

    url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257,SF60653,SF43718/datos/'+fechaIni+'/'+fechaFin+'?token=f1e4844065a4abddf790de1f67f2416a79a5ba6149424d8f5ba737c05d899d6d'
  
    response = requests.get(url)
    print(response.url)

    if response.status_code == 200:
        respose_json = response.text
        diccionario = json.loads(respose_json)
        #SP68257 = Valor de UDIS
        #SF60653 = Tipo de cambio pesos por dólar E.U.A. Tipo de cambio para solventar obligaciones denominadas en moneda extranjera Fecha de liquidación"
        #SF43718 = Tipo de cambio Pesos por dólar E.U.A. Tipo de cambio para solventar obligaciones denominadas en moneda extranjera Fecha de determinación (FIX)

        if diccionario['bmx']['series'][0]['idSerie'] == 'SP68257':
            udis = diccionario['bmx']['series'][0]['datos']
        if diccionario['bmx']['series'][0]['idSerie'] == 'SF60653':
            liquidacion_dll = diccionario['bmx']['series'][0]['datos']
        if diccionario['bmx']['series'][0]['idSerie'] == 'SF43718':
            fix_dll = diccionario['bmx']['series'][0]['datos']

        if diccionario['bmx']['series'][1]['idSerie'] == 'SP68257':
            udis = diccionario['bmx']['series'][1]['datos']
        if diccionario['bmx']['series'][1]['idSerie'] == 'SF60653':
            liquidacion_dll = diccionario['bmx']['series'][1]['datos']
        if diccionario['bmx']['series'][1]['idSerie'] == 'SF43718':
            fix_dll = diccionario['bmx']['series'][1]['datos']

        if diccionario['bmx']['series'][2]['idSerie'] == 'SP68257':
            udis = diccionario['bmx']['series'][2]['datos']
        if diccionario['bmx']['series'][2]['idSerie'] == 'SF60653':
            liquidacion_dll = diccionario['bmx']['series'][2]['datos']
        if diccionario['bmx']['series'][2]['idSerie'] == 'SF43718':
            fix_dll = diccionario['bmx']['series'][2]['datos']
        

        #promedio, maximos y minimos de UDIS
        promedioUdi = 0
        minymaxUDI = []
        labelsUDI = []
        dataUDI = []
        for item in udis:
            fecha = item['fecha']
            dato = float(item['dato'])
            promedioUdi = promedioUdi + dato
            minymaxUDI.append(dato)
            labelsUDI.append(fecha)
            dataUDI.append(dato)

        minymaxUDI.sort()
        minimoUDI = minymaxUDI[0]
        maximoUDI = minymaxUDI.pop()

        promedioUdi = promedioUdi / len(udis)

        #promedio, maximos y minimos de  liquidacion dolar
        promedioLiq = 0
        minymaxLiq = []
        labelsLiq = []
        dataLiq = []
        for item in liquidacion_dll:
            fecha1 = item['fecha']
            dato1 = float(item['dato'])
            promedioLiq = promedioLiq + dato1
            minymaxLiq.append(dato1)
            labelsLiq.append(fecha1)
            dataLiq.append(dato1)

        minymaxLiq.sort()
        minimoLiq = minymaxLiq[0]
        maximoLiq = minymaxLiq.pop()

        promedioLiq = promedioLiq / len(liquidacion_dll)

        #promedio, maximos y minimos de  liquidacion dolar
        promedioFix = 0
        minymaxFix = []
        labelsFix = []
        dataFix = []
        for item in fix_dll:
            fecha2 = item['fecha']
            dato2 = float(item['dato'])
            promedioFix = promedioFix + dato2
            minymaxFix.append(dato2)
            labelsFix.append(fecha2)
            dataFix.append(dato2)

        minymaxFix.sort()
        minimoFix = minymaxFix[0]
        maximoFix = minymaxFix.pop()

        promedioFix = promedioFix / len(fix_dll)





        return render(request, 'consulta.html', 
        {
            'fechaIni':fechaIni,
            'fechaFin':fechaFin,
            'udis': udis,
            'promedioUdi':promedioUdi,
            'minimoUDI':minimoUDI,
            'maximoUDI':maximoUDI,
            'labelsUDI':labelsUDI,
            'dataUDI':dataUDI,
            'liquidacion_dll': liquidacion_dll,
            'promedioLiq': promedioLiq,
            'minimoLiq':minimoLiq,
            'maximoLiq':maximoLiq,
            'labelsLiq':labelsLiq,
            'dataLiq':dataLiq,
            'fix_dll': fix_dll,
            'promedioFix': promedioFix,
            'minimoFix':minimoFix,
            'maximoFix':maximoFix,
            'labelsFix':labelsFix,
            'dataFix':dataFix,
            
            })