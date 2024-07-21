from django.shortcuts import render,redirect
from .models import Profile,Friend,ChatMessage
from django.core.mail import send_mail
from .forms import ChatMessageForm
from django.http import JsonResponse
import json
import random

# Create your views here.
def index(request):  
    user=request.session['user']
    cur=Profile.objects.get(name=user)
    friends=cur.friends.all()
    context={"user":cur,"friends":friends}
    return render(request,"live_chat/index.html",context)

def detail(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    user=Profile.objects.get(name=request.session['user'])
    profile=Profile.objects.get(id=friend.profile.id)
    chats=ChatMessage.objects.all()
    rec_chats=ChatMessage.objects.filter(msg_sender=profile,msg_reciever=user)
    rec_chats.update(seen=True)
    form=ChatMessageForm()
    if request.method =="POST":
        form=ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message=form.save(commit=False)
            chat_message.msg_sender=user
            chat_message.msg_reciever=profile
            chat_message.save()
            return redirect("detail",pk=friend.profile.id)

    context={"friend":friend,"form":form,"user":user,"profile":profile,"chats":chats,"num":rec_chats.count()}
    return render(request,"live_chat/detail.html",context)

def sentMessages(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    user=Profile.objects.get(name=request.session['user'])
    profile=Profile.objects.get(id=friend.profile.id)
    data=json.loads(request.body)
    new_chat=data["msg"]
    new_chat_message=ChatMessage.objects.create(body=new_chat, msg_sender=user , msg_reciever=profile , seen=False)
    print(new_chat,"ee")
    return JsonResponse(new_chat_message.body , safe=False)

def recievedMessages(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    user=Profile.objects.get(name=request.session['user'])
    profile=Profile.objects.get(id=friend.profile.id)
    arr=[]
    chats=ChatMessage.objects.filter(msg_sender=profile,msg_reciever=user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse( arr , safe=False)

def chatNotification(request):
    user=Profile.objects.get(name=request.session['user'])
    # user=request.user.profile
    friends=user.friends.all()
    arr=[]
    for friend in friends:
        chats=ChatMessage.objects.filter(msg_sender__id =friend.profile.id, msg_reciever=user , seen=False)
        arr.append(chats.count())    
    return JsonResponse(arr , safe=False)

def login(request):
    if request.method=="POST":
        eMail=request.POST.get("logeMail")
        password1=request.POST.get("logpassword")
        user=Profile.objects.get(email=eMail)
        print("*************************************************")
        # print(eMail)
        # print(user)
        # print(type(user))
        name=user.name
        print("***********************************")
        if Profile.objects.filter(email=eMail).exists():
            if Profile.objects.filter(passwd=password1).exists():
                request.session['user']=name
                return redirect('index')
            else:
                return redirect('/live_chat/login/?error=Invalid_Password')
        else:
            return redirect('/live_chat/login/?error=Invalid_email')
    return render(request,'live_chat/login.html')

def handle_signup(request):
    data=json.loads(request.body)
    userName=data["userName"]
    eMail=data["eMail"]
    password1=data["password1"]
    password2=data["password2"]
    allu=Profile.objects.all()
    names=[]
    for i in allu:
        names.append(i)
    if "Hardik" in names:
        print ("***********************")
    for i in range(0,len(names)):
        temp=names[i]
        if userName== temp.name:
            return JsonResponse("Name Error",safe=False)
       
    if password1 != password2:
        return JsonResponse("password Error",safe=False)          
        
    print(len(names))
    new_user=Profile.objects.create(user=None, name=userName, email=eMail, passwd=password1) 
    
    f=Friend.objects.all()
    for i in f:
        new_user.friends.add(i)
    new_user.save()
    a=Friend.objects.create(profile=new_user)
    # print (Profile.objects.all())
    return JsonResponse("working" , safe=False)

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/login')

def about(request):
    return render(request,"live_chat/about.html")

def forgot(request):
    return render(request,"live_chat/forgot.html")

def ver_em(request):
    onetp=random.randint(1000,9999)
    data=json.loads(request.body)
    # eMail=request.POST.get("user_email")
    eMail=data['em']
    user=Profile.objects.get(email=eMail)
    request.session[user.id]=onetp
    request.session['eml']=eMail

    send_mail(
        'Forgot Password',
        f'Your OTP is : {request.session[user.id]}',
        'bolochatco@gmail.com',
        [eMail],
        fail_silently=False,
    )
    return JsonResponse(onetp , safe=False)

def reset(request):
    return render(request,'live_chat/reset.html')
def change_pass(request):
    print("*********************************************")
    user=Profile.objects.get(email=request.session['eml'])
    data=json.loads(request.body)
    user.passwd=data['pd']
    user.save()
    return JsonResponse("Success" , safe=False)
# bolochatco@gmail.com
# B0lo(hatco