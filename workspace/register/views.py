from django.shortcuts import render, redirect
from .forms import RegisterForm
from Bank.models import Account

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process form data and create a new user
            new_user = form.save()  # Save the user object from the form

            # Create an Account instance for the new user
            new_account = Account(user=new_user, balance=0.0)
            new_account.save()  # This will trigger generate_account_number() if account_number is empty

            # Redirect to a success page or login page
            return redirect('login')  # Replace 'login' with your URL name for the login page

    else:
        form = RegisterForm()

    # Render the registration form
    return render(request, 'register.html', {'form': form})
