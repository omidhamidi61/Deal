from django.shortcuts import render,redirect
import http
import django
import json
from app1.models import WorkersTable , MessagesTable , TeamMembersTable , ShiftsTable
from app1.forms import WorkersForm, MessagesForm
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models import Count

# Create your views here.
allnames = TeamMembersTable.objects.all()
mainworker = None
inbox = None
outbox = None
unread = None
idid = None
shifts = None
canc = False

def checkusername(request):
    ajax1 = request.GET.get('workerfullname')
    data={'usr':WorkersTable.objects.get(name = ajax1).username}
    return JsonResponse(data)

def checkpassword(request):
    global mainworker
    usr = request.GET.get('user')
    psw = request.GET.get('pss')
    worker = WorkersTable.objects.get(username = usr)
    r = (worker.pssword == psw)
    mainworker = worker
    data={'res':r}
    return JsonResponse(data)

def login(request):
    frm = WorkersForm
    allw = WorkersTable.objects.all()
    return render(request,'app1/login.html',{'n':allw , 'frm':frm})

def receivednewmail(request):
    inbox = MessagesTable.objects.filter(receiver = mainworker)
    outbox = MessagesTable.objects.filter(sender = mainworker)
    unread = (inbox.isUnread.count())
    data = {'inbox':inbox , 'outbox':outbox , 'unread':unread}
    return JsonResponse(data)

def home(request):
    allreceivers = allnames.exclude(member = mainworker)
    allreceivers2 = WorkersTable.objects.all().exclude(name = mainworker)
    global inbox, outbox, unread
    inbox = MessagesTable.objects.filter(receiver = mainworker)
    outbox = MessagesTable.objects.filter(sender = mainworker)
    unread = MessagesTable.objects.filter(receiver = mainworker, isUnread = True)
    member1 = allnames.get(member = mainworker)
    memteam = member1.teamnumber
    if request.method == 'POST' and 'SendMessageBtn' in request.POST:
        if canc == False:
            rw = request.POST.get('ReceiversList')
            if rw == None :
                if member1.isSupervisor:
                    rw = allreceivers.filter(isSupervisor = True)
                    rw = rw.exclude(teamnumber = memteam + 2)
                    rw = rw.exclude(teamnumber = memteam - 2)
                    rw = rw.exclude(teamnumber = memteam + 3)
                    rw = rw.exclude(teamnumber = memteam - 3)
                else:
                    if member1.isRated:
                        rw = allreceivers.exclude(isSupervisor = True)
                        rw = rw.exclude(teamnumber = memteam + 2)
                        rw = rw.exclude(teamnumber = memteam - 2)
                        rw = rw.exclude(teamnumber = memteam + 3)
                        rw = rw.exclude(teamnumber = memteam - 3)
                for r in rw:
                    message=MessagesTable()
                    message.sender = mainworker
                    message.receiver= r.member
                    message.title = request.POST.get('MessageTitle')
                    message.content = request.POST.get('MessageContent')
                    message.isUnread = True
                    message.isAccepted = False
                    message.save()
                    for s in shifts.split(','):
                        shift = ShiftsTable()
                        shift.massagekey = message
                        shift.date = s.split(':')[0]
                        if s.split(':')[1] == 'Day': shift.isDay = True
                        else: shift.isDay = False
                        shift.save()

            else:
                message=MessagesTable()
                message.sender = mainworker
                message.receiver= WorkersTable.objects.get(name = rw)
                message.title = request.POST.get('MessageTitle')
                message.content = request.POST.get('MessageContent')
                message.isUnread = True
                message.isAccepted = False
                message.save()
                for s in shifts.split(','):
                    shift = ShiftsTable()
                    shift.massagekey = message
                    shift.date = s.split(':')[0]
                    if s.split(':')[1] == 'Day': shift.isDay = True
                    else: shift.isDay = False
                    shift.save()
    return render(request,'app1/home.html',{'worker':mainworker,'member':member1,'n1':allreceivers2,'unreadcount':unread.count()})

def inbox(request):
    unread = MessagesTable.objects.filter(receiver = mainworker, isUnread = True)
    inbox = MessagesTable.objects.filter(receiver = mainworker)
    return render (request,"app1/inbox.html",{'inbox':inbox , 'unreadcount':unread.count() , 'worker':mainworker})

def outbox(request):
    outbox = MessagesTable.objects.filter(sender = mainworker)
    unread = MessagesTable.objects.filter(receiver = mainworker, isUnread = True)
    qry =MessagesTable.objects.filter(sender = mainworker).aggregate(Count('title'))
    return render (request,"app1/outbox.html",{'outbox':outbox , 'worker':mainworker , 'unreadcount':unread.count()})

def checksendermails(request):
    sen = request.GET.get('send')
    sende = WorkersTable.objects.get(name = sen)
    sendermails = MessagesTable.objects.filter(sender = sende , receiver = mainworker)
    datasender = serializers.serialize('json',list(sendermails))
    data = {'datasender':datasender}
    return JsonResponse(data, safe= False)

def checkreceivermails(request):
    rec = request.GET.get('reci')
    receive = WorkersTable.objects.get(name = rec)
    receivermails = MessagesTable.objects.filter(sender = mainworker , receiver = receive)
    datareceiver = serializers.serialize('json',list(receivermails))
    data = {'datareceiver':datareceiver}
    return JsonResponse(data, safe= False)

def unreadmessages(request):
    unread = MessagesTable.objects.filter(receiver = mainworker, isUnread = True)
    return render (request,"app1/unreadmessages.html",{'unreadmessages':unread , 'unreadcount':unread.count() , 'worker':mainworker})

def showcontent(request):
    global idid
    idid = request.GET.get('idid')
    msg = MessagesTable.objects.get(id = idid)
    msg.isUnread=False
    msg.save()
    data = {'contnt':msg.content, 'commnt':msg.comment, 'rec':msg.receiver.name}
    return JsonResponse(data)

def deal(request):
    try:
        idid = request.GET.get('idid')
        tr = request.GET.get('tr')
        msg = MessagesTable.objects.get(id = idid)
        msg.isAccepted=True
        msg.save()
        data = {'status': True , 'tr':tr}
    except:
        data = {'status':False , 'tr':tr}
    return JsonResponse(data)

def logout(request):
    try:
        mainworker = None
        data = {'status':True}
    except:
        data = {'status':False}
    return JsonResponse(data)
    
def sendcomm(request):
    try:
        comm = request.GET.get('comm')
        msg = MessagesTable.objects.get(id = idid)
        content = msg.content
        msg.comment = comm 
        msg.save()
        data = {'status':True,'contnt':content}
    except:
        data = {'status':False}
    return JsonResponse(data)

def getcomm(request):
    try:
        msg = MessagesTable.objects.get(id = idid)
        data = {'status':True, 'commnt':msg.comment, 'contnt':msg.content}
    except:
        data = {'status':False}
    return JsonResponse(data)
def delcomm(request):
    try:
        msg = MessagesTable.objects.get(id = idid)
        msg.comment = None
        msg.save();
        data = {'status':True, 'commnt':msg.comment,'contnt':msg.content}
    except:
        data = {'status':False}
    return JsonResponse(data)

def sendshifts(request):
    global canc
    canc = True
    try:
        global shifts
        shifts = request.GET.get('shifts')
        canc = False
        data = {'status': True}
    except:
        data = {'status':False}
    return JsonResponse