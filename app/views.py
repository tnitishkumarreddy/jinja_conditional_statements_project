from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'age':98}

    return render(request,'conditions.html',context=d)