from django.shortcuts import render,redirect
from book_app.forms import BookForm
from book_app.models import BookData
from django.contrib import messages     
from django.contrib.auth.decorators import login_required
# Create your views here.  
  
def homebook(request):
    return render(request,'book_app/home.html')
   
@login_required
def book_list(request):
    genre = request.GET.get('genre')
    if genre:
        book_data= BookData.objects.filter(genre=genre).order_by('-created_at')
    else:
        book_data = BookData.objects.all().order_by('-created_at')
    return render(request,'book_app/booklist.html',{'book_data':book_data})
 
@login_required
def addbooks(request):
    if (request.method == 'POST'):   
        bookf=BookForm(request.POST)
        if bookf.is_valid():
            bookf.save() 
            messages.success(request," Success! Your Book review has been added successfully.")
            return redirect('addbook')
    else:
        bookf=BookForm()
    return render(request,'book_app/addbooks.html',{'form':bookf})

@login_required
def viewbooks(request, pk):
    view_data = BookData.objects.get(pk=pk)
    return render(request,'book_app/viewbooks.html',{'view_data' : view_data})

@login_required
def updatebook(request,pk):
    view_data = BookData.objects.get(pk=pk)
    if (request.method == 'POST'):   
        bookf=BookForm(request.POST,instance=view_data)
        if bookf.is_valid():
            bookf.save() 
            messages.success(request," Success! Your Book review has been updated successfully.")
            return redirect('booklist')
    else:
        bookf=BookForm(instance=view_data)
    return render(request,'book_app/addbooks.html',{'form':bookf})

@login_required
def deletebook(request,pk):
    view_data = BookData.objects.get(pk=pk)
    view_data.delete()
    messages.success(request,"Success! Your Book review has been deleted successfully.")
    return redirect('booklist')

