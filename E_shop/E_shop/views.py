from django.shortcuts import render
from app.models import Categroy

def master_view(request):
    return render(request,'master.html')

def index_view(request):
    categroy = Categroy.objects.all()
    context ={'categroy':categroy}
    return render(request,'index.html',context)


    