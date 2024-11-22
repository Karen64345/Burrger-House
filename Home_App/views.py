from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Book_Table  # Import the corrected model

# Define your views here

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')  # This serves the contact page

def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')
        person = request.POST.get('person')

        if name and email and phone_number and date and person:
            data = Book_Table(name=name, email=email, phone_number=phone_number, date=date, person=person)
            data.save()
            return redirect('home')  # Redirect after saving the data

    return render(request, 'home.html')


def show_text(request):
    # Open the file and read its contents
    with open('static/files/django.txt', 'r') as file:
        content = file.read()

    # Pass the content to the template
    return render(request, 'show_text.html', {'content': content})

def order(request):
    return render(request, 'order.html')  # Add this line to serve the order page
