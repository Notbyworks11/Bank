from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate ,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import UserProfile, Account

# Create your views here.
def index(response):
    return render (response,'base.html')
def home(response):
    return render(response,'home.html')
@login_required
def dashboard(request):
    username = request.user.username
    
    try:
        user_account = get_object_or_404(Account, user=request.user)
        account_number = user_account.account_number
        balance = user_account.balance  # Retrieve balance from the Account model
    except Account.DoesNotExist:
        account_number = None
        balance = None

    context = {
        'name': username,
        'account_number': account_number,
        'balance':balance
    }

    return render(request, "dashboard.html", context)
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('dashboard')  # Redirect to dashboard or any other page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/home')