from django.shortcuts import render, redirect
from questions.models import users

def signup(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        user = request.POST.get('user')
        upass = request.POST.get('upass')
        
        # Check if username already exists
        if users.objects.filter(user=user).exists():
            return render(request, 'signup.html', {'msg': 'This username is already taken!'})
        
        # Create new user
        q = users.objects.create(sname=sname, user=user, upass=upass)
        q.save()
        return render(request, 'signup.html', {'msg': 'Account created successfully!'})
    
    return render(request, 'signup.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('/questions/')
    else:
        return redirect('index')


