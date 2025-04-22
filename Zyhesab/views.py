from django.shortcuts import render, redirect
from accounts.forms import ContactUsForm
from blogs.models import Blog


def home(request):
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    context = {
        'blogs': blogs,
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