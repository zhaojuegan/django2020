from django.shortcuts import render

# Create your views here.

def if_view(request,name):
    return render(request,'if.html',context={
        'name':name,
    })
def for_view(request,name):
    return render(request,'for.html',context={
        'name':[n for n in range(10)]
    })
def base_view(request):
    return render(request,'super.html')