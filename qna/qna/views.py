from django.shortcuts import redirect, render
from django.http import JsonResponse

#Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('/questions/')
    else:
        return redirect('index')