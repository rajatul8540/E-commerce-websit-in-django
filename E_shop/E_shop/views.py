from django.shortcuts import render

def master_view(request):
    return render(request,'master.html')

def index_view(request):
        return render(request,'index.html')

    