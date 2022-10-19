from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm, ProfilePictureForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} is registered')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {'form': form, }
    return render(request, 'register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        data_form = UserProfileForm(request.POST, instance=request.user)
        picture_form = ProfilePictureForm(
            request.POST, request.FILES, instance=request.user.profile)
        if data_form.is_valid() and picture_form.is_valid():
            data_form.save()
            picture_form.save()
            username = data_form.cleaned_data.get('username')
            first_name = data_form.cleaned_data.get('first_name')
            last_name = data_form.cleaned_data.get('last_name')
            email = data_form.cleaned_data.get('email')
            messages.success(
                request, f'profile: {username} is updated \nFirstname: {first_name} \nLastname: {last_name} \nEmail: {email}')
            return redirect('profile')

    else:
        data_form = UserProfileForm(instance=request.user)
        picture_form = ProfilePictureForm()
        # picture_form = ProfilePictureForm(instance=request.user.profile)  # laedt vom DB
    return render(request, 'profile.html', {'data_form': data_form, 'picture_form': picture_form})
