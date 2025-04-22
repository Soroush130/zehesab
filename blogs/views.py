from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import BlogForm
from .models import Blog
from django.contrib import messages

@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            if form.cleaned_data['status'] == 'published':
                blog.published_at = timezone.now()
            blog.save()
            messages.success(request, 'مقاله با موفقیت ایجاد شد ✅')
            return redirect('blog_detail', pk=blog.pk)
        else:
            messages.error(request, 'لطفاً فرم را به درستی پر کنید ⚠️')
    else:
        form = BlogForm()
    return render(request, 'blogs/create_blog.html', {'form': form})


@login_required
def blog_update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.user != blog.author:
        return redirect('blog_detail', pk=blog.pk)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            updated_blog = form.save(commit=False)

            if form.cleaned_data['status'] == 'published' and not updated_blog.published_at:
                updated_blog.published_at = timezone.now()

            updated_blog.save()  # ذخیره بلاگ
            return redirect('blog_detail', pk=updated_blog.pk)

    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/edit_blog.html', {'form': form})
