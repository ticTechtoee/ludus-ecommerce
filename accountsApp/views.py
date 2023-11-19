from django.shortcuts import render, redirect
from .forms import WebUserRegistrationForm

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
