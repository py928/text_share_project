from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from .models import TXT
import random
def create_text(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            path = ''.join(random.choices('1234567890qwerasd',k=10))
            text = TXT(content=content,path=path)
            text.save()
            return HttpResponseRedirect(content, path=path)
    return render(request, 'text_sharing_app/create_text.html')

def view_text(request, path):
    text = TXT.objects.get(path=path)
    return HttpResponse(text.content, {'text': text})