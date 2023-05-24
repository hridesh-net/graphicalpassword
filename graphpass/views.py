from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Perform any additional actions
            return HttpResponse('registration_success')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})