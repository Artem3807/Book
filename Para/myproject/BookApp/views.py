from urllib import request
from django.shortcuts import redirect, render
from myproject.BookApp.models import BookForm



def book_create_view(requesr):
    if request.method == "POST": 
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("form")
        else:
            form = BookForm()
    render  (request,  'forms.html', {'form': form})