from django.shortcuts import render

def landing_view(request):
    template = "index.html"
    contexts = {}
    return render(request, template, contexts)