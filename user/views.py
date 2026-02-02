from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm # You'll need to create this

@login_required
def profile_view(request):
    # This keeps the logic simple for your starter
    context = {
        'user': request.user,
        'profile': request.user.profile,
        'page_title': f"{request.user.username}'s Profile"
    }
    return render(request, 'user/profile.html', context)

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')  # Adjust this to your profile URL name
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'user/profile_edit.html', {'form': form})