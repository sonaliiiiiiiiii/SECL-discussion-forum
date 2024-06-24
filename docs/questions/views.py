from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import users, post_q, qna_db, Vote

def questions(request):
    user = request.session.get('user')
    if user:
        return redirect('home')
    else:
        return render(request, 'login.html')

def login(request):
    user = request.POST['user']
    upass = request.POST['upass']
    
    res = users.objects.filter(user=user, upass=upass)
    
    if len(res) == 1:
        request.session['user'] = res[0].user
        return redirect('home')
    else:
        return render(request, 'login.html', {'error': 'Username or password is incorrect!!!'})
        
def home(request):
    user = request.session.get('user')
    if user:
        return render(request, 'home.html', {'user': user})
    else:
        return redirect('/questions/')
        
def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('/questions/')
    else:
        return redirect('home')

def post_question(request):
    user = request.session.get('user')
    if user:
        return render(request, 'post_question.html', {'user': user})
    else:
        return redirect('/questions/')

def post_que(request):
    pquestion = request.POST['pquestion']
    puser = request.session.get('user')
    
    res = post_q(pquestion=pquestion, puser=puser)
    res.save()
    
    return render(request, 'post_question.html', {'msg': 'Your question is posted successfully!!!', 'user': puser})

def check_qna(request):
    user = request.session.get('user')
    if user:
        res = post_q.objects.all()
        return render(request, 'questions.html', {'res': res, 'user': user})
    else:
        return redirect('/questions/')

def answers(request):
    user = request.session.get('user')
    if user:
        qid = request.GET['qid']
        k = post_q.objects.filter(id=qid)
        if k.exists():
            que = k[0]
            ans = qna_db.objects.filter(qid=qid)
            return render(request, 'qna.html', {'que': que, 'ans': ans, 'user': user})
        else:
            return redirect('/questions/')
    else:
        return redirect('/questions/')

def new_ans(request):
    qid = request.POST['qid']
    answr = request.POST['answr']
    auser = request.session.get('user')
    
    res = qna_db(qid=qid, answr=answr, auser=auser)
    res.save()
    
    return redirect('check_qna')

def upvote_answer(request):
    if request.method == 'POST' and request.session.get('user'):
        user = users.objects.get(user=request.session.get('user'))
        answer_id = request.POST['answer_id']
        answer = get_object_or_404(qna_db, id=answer_id)
        
        if answer.auser == user.user:
            return JsonResponse({'error': 'You cannot vote your own answer'}, status=400)
        
        vote, created = Vote.objects.get_or_create(user=user, answer=answer)
        
        if created:
            answer.upvotes += 1
        else:
            if vote.vote_type == 'downvote':
                answer.downvotes -= 1
                answer.upvotes += 1
            elif vote.vote_type == 'upvote':
                return JsonResponse({'error': 'You have already upvoted this answer'}, status=400)

        vote.vote_type = 'upvote'
        vote.save()
        answer.save()
        
        return JsonResponse({'upvotes': answer.upvotes, 'downvotes': answer.downvotes})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def downvote_answer(request):
    if request.method == 'POST' and request.session.get('user'):
        user = users.objects.get(user=request.session.get('user'))
        answer_id = request.POST['answer_id']
        answer = get_object_or_404(qna_db, id=answer_id)
        
        if answer.auser == user.user:
            return JsonResponse({'error': 'You cannot vote your own answer'}, status=400)
        
        vote, created = Vote.objects.get_or_create(user=user, answer=answer)
        
        if created:
            answer.downvotes += 1
        else:
            if vote.vote_type == 'upvote':
                answer.upvotes -= 1
                answer.downvotes += 1
            elif vote.vote_type == 'downvote':
                return JsonResponse({'error': 'You have already downvoted this answer'}, status=400)

        vote.vote_type = 'downvote'
        vote.save()
        answer.save()
        
        return JsonResponse({'upvotes': answer.upvotes, 'downvotes': answer.downvotes})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def signup(request):
    return render(request, 'signup.html')
