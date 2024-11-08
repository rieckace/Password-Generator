from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 12))
    
    characters = ''
    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase
    if request.GET.get('lowercase'):
        characters += string.ascii_lowercase
    if request.GET.get('numbers'):
        characters += string.digits
    if request.GET.get('special'):
        characters += string.punctuation
    
    if not characters:  # Ensure there's at least one character type selected
        characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return render(request, 'generator/password.html', {'password': generated_password})
