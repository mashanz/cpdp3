from django.shortcuts import render
from app_blog.utility import query

def view(request):
    result = None
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        result = query("insert into blog_post (title, content) values (%s, %s) returning *", [title, content])
        print(result)
    return render(request, "app_blog/create.html", {"result": result})