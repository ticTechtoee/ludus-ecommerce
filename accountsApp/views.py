from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import WebUserRegistrationForm, WebUserLoginForm

def ViewSignUpPage(request):
    if request.method == 'POST':
        form = WebUserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            user = form.save(commit=False)  # Use commit=False to avoid saving the user immediately
            user.set_password(form.cleaned_data['password1'])  # Set the password separately
            user.save()  # Now save the user with the password

            print("User registered successfully")
            #return redirect('login')  # Redirect to the login page or any other desired page after successful registration
    else:
        form = WebUserRegistrationForm()

    context = {'form': form}
    return render(request, 'accountsApp/signup.html', context)

def ViewLoginPage(request):
    if request.method == 'POST':
        form = WebUserLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            print('Login Successful')
            # return redirect('home')  # Redirect to the home page or any other desired page after successful login
        else:
            print('Form is not valid')
            form = WebUserLoginForm(request, data=request.POST)
            print('Form errors:', form.errors)
            print('Submitted data:', request.POST)
    else:
        form = WebUserLoginForm()

    context = {'form': form}
    return render(request, 'accountsApp/login.html', context)