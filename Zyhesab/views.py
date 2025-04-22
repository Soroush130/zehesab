from django.shortcuts import render, redirect
from accounts.forms import ContactUsForm

def home(request):

    context = {
    }
    return render(request, 'home.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactUsForm()

    return render(request, 'contact_us.html', {'form': form})


def about_us(request):
    return render(request, 'about_us.html', {})