from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .models import Lead
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from datetime import timedelta, datetime
from django.utils import timezone
from .forms import LeadForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            # Handle failed login attempt (e.g., display error message)
            pass
    return render(request, 'login.html')

def user_action(request):
    action = request.GET.get('action', '')
    if action == 'register':
        return user_register(request)
    elif action == 'logout':
        return user_logout(request)
    else:
        return
    
def user_register(request):
    result = {
        'code':0,
        'msg':''
    }
    if request.method == 'GET':
        return render(request, 'register.html')
    
    username = request.POST.get('username', '')
    password1 = request.POST.get('password', '')

    user = User.objects.create_user(username,None,password1)
    result['msg'] = str(user)
    result['code'] = 1
    return HttpResponseRedirect('/')

def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')

@login_required(login_url='/login')
def home(request, view_type):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    time = datetime.now()
    lead_data = user.lead_set.all()
    if view_type == 'all':
        flag = False
    else:
        data = [lead for lead in lead_data]
        lead_data = data
        flag = True
    return render(request, 'home.html', {'lead_data':lead_data, 'view_type':view_type})

@login_required(login_url='/login')
def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            data = {}
            data['company'] = form.cleaned_data['company']
            data['contact'] = form.cleaned_data['contact']
            data['date'] = form.cleaned_data['date']
            data['installed'] = form.cleaned_data['installed']
            data['verbal'] = form.cleaned_data['verbal']
            data['invoice'] = form.cleaned_data['invoice']
            data['paid'] = form.cleaned_data['paid']
            data['phone'] = form.cleaned_data['phone']
            data['address'] = form.cleaned_data['address']
            data['notes'] = form.cleaned_data['notes']
            data['stale'] = form.cleaned_data['stale']
            data['probable'] = form.cleaned_data['probable']
            data['trial'] = form.cleaned_data['trial']
            data['trial_expiration'] = form.cleaned_data['trial_expiration']
            lead = Lead()
            lead.add_lead(data, user)
            return HttpResponseRedirect('/')
    form = LeadForm()
    return render(request, 'add_lead.html', {'form': form})

@login_required(login_url='/login')
def edit_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            id = request.POST.get('id')
            lead = Lead.objects.get(id=id,user=user)
            lead.company = form.cleaned_data['company']
            lead.contact = form.cleaned_data['contact']
            lead.date = form.cleaned_data['date']
            lead.installed = form.cleaned_data['installed']
            lead.verbal = form.cleaned_data['verbal']
            lead.invoice = form.cleaned_data['invoice']
            lead.paid = form.cleaned_data['paid']
            lead.phone = form.cleaned_data['phone']
            lead.address = form.cleaned_data['address']
            lead.notes = form.cleaned_data['notes']
            lead.stale = form.cleaned_data['stale']
            lead.probable = form.cleaned_data['probable']
            lead.trial = form.cleaned_data['trial']
            lead.trial_expiration = form.cleaned_data['trial_expiration']
            lead.save()
            return HttpResponseRedirect('/')
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    id = request.GET.get('id','')
    lead = Lead.objects.get(id=id,user=user)
    initial_data = {
        'company': lead.company,
        'contact': lead.contact,
        'date': lead.date,
        'installed': lead.installed,
        'verbal': lead.verbal,
        'invoice': lead.invoice,
        'paid': lead.paid,
        'phone': lead.phone,
        'address': lead.address,
        'notes': lead.notes,
        'stale': lead.stale,
        'probable': lead.probable,
        'trial': lead.trial,
        'trial_expiration': lead.trial_expiration
    }
    form = LeadForm(initial=initial_data)
    return render(request, 'edit_lead.html', {'form': form, 'data': lead, 'id': lead.id})
