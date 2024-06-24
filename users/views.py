from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in
            authenticated_user = authenticate(username=form.cleaned_data['username'],
                                              password=form.cleaned_data['password1'])
            login(request, authenticated_user)
            # Redirect to home page or any desired page
            return redirect('learning_logs:index')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)


