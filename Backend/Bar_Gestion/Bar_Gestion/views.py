from django.shortcuts import render

def frontend(request):
    return render(request,'Bar_Gestional_Manager/FrontEnd/myapp/src/index.html')