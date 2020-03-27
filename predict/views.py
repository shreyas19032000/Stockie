from django.shortcuts import render
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from .predictengine import algo
import pandas_datareader as web



# Create your views here.

def form(request):
    if request.method == 'POST':
        nasdaq = request.POST.get('nasdaq')
        date = datetime.today().strftime('%Y-%m-%d')
        
        daten = datetime.strptime(date,'%Y-%m-%d') - relativedelta(years=10)
        daten = daten.strftime('%Y-%m-%d')
        datenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
        # print(nasdaq)
        print(date)
        # print(daten)
        graph = algo(nasdaq,daten,date)
        oneday = web.DataReader(nasdaq, data_source = 'yahoo', start = datetime.today().strftime('%Y-%m-%d') , end = datetime.today().strftime('%Y-%m-%d'))
        oneday1 = oneday.head(1)
        print(oneday1)
        return render(request,'predict.html',{'data':graph, 'nasdaq':nasdaq, 'oneday1':oneday1, 'datenow':datenow})
    return render(request,'predict.html',{})  


    