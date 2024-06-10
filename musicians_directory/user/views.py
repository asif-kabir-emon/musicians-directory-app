from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UpdateUserProfileDataForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created successfully. Please login.')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login successful.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Login failed. Please try again.')
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

@login_required 
def user_profile(request):
    if request.method == 'POST':
        form = UpdateUserProfileDataForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = UpdateUserProfileDataForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully. Please login.')
        user_logout(self.request)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Password change failed. Please try again.')
        return super().form_invalid(form)
