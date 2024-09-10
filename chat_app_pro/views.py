from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import login as auth_login, get_user_model
from .forms import CustomAuthUserCreationForm, CustomAuthUserLoginForm


@login_required
def home_view(request):
    User = get_user_model()  # Get the user model

    # Get all messages involving the current user
    messages = Message.objects.filter(
        models.Q(from_user=request.user) | models.Q(to_user=request.user)
    ).distinct()

    # Create a dictionary to store chats
    chats = {}
    for message in messages:
        other_user = message.to_user if message.from_user == request.user else message.from_user
        if other_user not in chats:
            chats[other_user] = {
                'messages': Message.objects.filter(
                    (models.Q(from_user=request.user) & models.Q(to_user=other_user)) |
                    (models.Q(from_user=other_user) & models.Q(to_user=request.user))
                ).order_by('timestamp'),
                'last_message': Message.objects.filter(
                    (models.Q(from_user=request.user) & models.Q(to_user=other_user)) |
                    (models.Q(from_user=other_user) & models.Q(to_user=request.user))
                ).last()
            }

    return render(request, 'chat/home.html', {'chats': chats})


def create_chat(request):
    User = get_user_model()  # Get the user model
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user from the list

    if request.method == 'POST':
        to_user_id = request.POST.get('to_user')
        content = request.POST.get('content')
        if to_user_id and content:
            to_user = User.objects.get(id=to_user_id)
            # Create the initial message
            Message.objects.create(from_user=request.user, to_user=to_user, content=content)
            return redirect('home')  # Redirect to home or any other page after creating the chat

    return render(request, 'chat/create_chat.html', {'users': users})


@login_required
def chat_detail(request, user_id):
    User = get_user_model()  # Use get_user_model to get the custom user model
    chat_user = User.objects.get(id=user_id)

    # Fetch messages between the current user and the chat user
    messages = Message.objects.filter(
        (models.Q(from_user=request.user) & models.Q(to_user=chat_user)) |
        (models.Q(from_user=chat_user) & models.Q(to_user=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # Create a new message
            Message.objects.create(from_user=request.user, to_user=chat_user, content=content)
            return redirect('chat_detail', user_id=chat_user.id)

    return render(request, 'chat/chat_detail.html', {'chat_user': chat_user, 'messages': messages})

def signup_view(request):
    if request.method == 'POST':
        form = CustomAuthUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomAuthUserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomAuthUserLoginForm()
    return render(request, 'chat/login.html', {'form': form})