from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from report.forms import SignUpForm, ConfigForm
from report.models import Config


def home_page(request):
    return render(request, 'home_page.html')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('home_page')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def authorization(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    return redirect('login')


def account_page(request):
    show_all_config = Config.objects.filter(user=request.user)
    context = {
        'form': show_all_config
    }
    return render(request, 'user_account.html', context)


def create_config(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = ConfigForm(request.POST, {'user': request.user})

            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('home_page')
        else:
            form = ConfigForm()
    return render(request, 'create_config.html', {'form': form})


def show_config(request, user_id):
    post = get_object_or_404(Config.objects.filter(user=request.user, pk=user_id))
    context = {
        'post': post,
        'selected': post.user_id,

    }
    return render(request, 'show_config.html', context=context)


def edit(request, user_id):
    if request.method == "POST":
        edit_config = Config.objects.get(pk=user_id)
        form = ConfigForm(request.POST, instance=edit_config)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('account')
    else:
        edit_config = Config.objects.get(pk=user_id)
        form = ConfigForm(instance=edit_config)
    return render(request, "change_report.html", {"form": form})


def delete(request, user_id):
    config = Config.objects.get(id=user_id)
    config.delete()
    return redirect('account')


def choose_config_for_presentation(request):
    config = Config.objects.filter(user=request.user)
    context = {
        'form': config
    }
    return render(request, 'choose_config_for_presentation.html', context)