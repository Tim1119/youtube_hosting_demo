from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages


def index(request):
    form = ContactForm()  
    return render(request, 'core/index.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('core:index')  # Redirect to prevent resubmission on page refresh
        else:
            messages.error(request, 'There was an error submitting the form. Please try again.')
    else:
        form = ContactForm()
    
    return render(request, 'create_contact.html', {'form': form})
