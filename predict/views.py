from django.shortcuts import render
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from .predictengine import algo



# Create your views here.

def form(request):
    if request.method == 'POST':
        nasdaq = request.POST.get('nasdaq')
        date = request.POST.get('date')
        daten = datetime.strptime(date,'%Y-%m-%d') - relativedelta(years=10)
        print(nasdaq)
        print(daten)
        graph = algo(nasdaq,daten,date)
        return render(request,'predict.html',{'data':graph})
    return render(request,'predict.html',{})        
    
    