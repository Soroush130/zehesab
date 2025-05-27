from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse
from meta.views import Meta

from .forms import BlogForm
from .models import Blog


@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    meta = Meta(
        title=blog.get_meta_title(),
        description=blog.get_meta_description(),
        keywords=blog.get_meta_keywords(),
        url=request.build_absolute_uri(blog.get_absolute_url()),
        image=blog.get_meta_image() if hasattr(blog, 'get_meta_image') else None,
        object_type='article',
        use_og=True,
        use_twitter=True,
        use_schemaorg=True,
    )

    return render(request, 'blogs/blog_detail.html', {
        'blog': blog,
        'meta': meta
    })


@login_required
def blog_delete(request, blog_id):
    url = request.META.get("HTTP_REFERER")
    try:
        blog = get_object_or_404(Blog, pk=blog_id)
        if blog.author == request.user:
            blog.delete()
            return redirect(url)
    except Blog.DoesNotExist:
        return redirect(url)


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
        else:
            pass
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
            updated_blog.save()
            return redirect('blog_detail', pk=updated_blog.pk)

    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/edit_blog.html', {'form': form, 'blog': blog})


@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image_file = request.FILES['file']
        file_path = default_storage.save(f'uploads/{image_file.name}', ContentFile(image_file.read()))
        file_url = default_storage.url(file_path)
        return JsonResponse({'location': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)