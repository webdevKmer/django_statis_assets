from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'form_app/index.html')

def message_success(request):
    return render(request, 'form_app/contact-success.html')

def contact(request):
    if (request.method == 'POST'):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('success')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'form_app/contact-form.html', context)