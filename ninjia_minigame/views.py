from django.shortcuts import render, redirect
import random
from time import localtime, strftime
context={
        'gold':0,
        'activities':[],
        }
def minigame(request):
    print('*'*50)
    print('minigame_loading')
    print(request)
    return render(request,'index.html',context)

def process_money(request):
    print('*'*50)
    print('processing money')
    print(request.session)
    currentime=strftime("%Y-%m-%d %H:%M %p", localtime())
    if request.POST['location']=='farm':
        r_numb=random.randint(10,20)
    elif request.POST['location']=='cave':
        r_numb=random.randint(5,10)
    elif request.POST['location']=='house':
        r_numb=random.randint(2,5)
    elif request.POST['location']=='casino':
        r_numb=random.randint(-50,50)
    
    if r_numb==0 or r_numb==1:
            gold='gold'
    else:
            gold='golds'
    if r_numb<0:
        comment=f"Entered {request.POST['location']} and lost {r_numb} {gold}... Ouch... ({currentime})"
        act_class="lost"
    else:
        comment=f"Earned {r_numb} {gold} in the {request.POST['location']}! ({currentime})"   
        act_class="gain"
    request.session=context
    request.session['gold']+=r_numb
    request.session['activities'].append({'class':act_class,'log':comment})
    print(currentime)
    return redirect('/')

# Create your views here.
