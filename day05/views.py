from django.shortcuts import render

# Create your views here.
def view_filter(request):
    return render(request,'filters.html')
def view_lable(request):
    return render(request,'filters.html')
def view_lable_s(request):
    return render(request,'label.html',context={
        'persion':{
            'name':request.GET.get('name'),
            'age':request.GET.get('age'),
        }
    })