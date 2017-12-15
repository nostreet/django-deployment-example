from django.shortcuts import render

def index(request):
    context_dict = {'text':"hello world", "number":100}
    return render(request, "app_no1/index.html", context_dict)

def other(request):
    return render(request, "app_no1/other.html")

def relative(request):
    return render(request, "app_no1/relative_url_templates.html")
