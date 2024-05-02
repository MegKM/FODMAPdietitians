from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserCreationForm
from user.models import User
from .models import Practice

def home(request):
  return render(request, 'home.html')

def dietitians_index(request):
    dietitians = User.objects.filter(is_superuser=False)
    return render(request, 'dietitians/index.html', {
        'dietitians' : dietitians
    })

def dietitians_practices(request):
    dietitians = User.objects.filter(is_superuser=False)
    practices = Practice.objects.all()
    return render(request, 'dietitians_practices.html', {
        'dietitians' : dietitians,
        'practices': practices      
    })

#------------------- Manage Dietitian accounts ---------------------#
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup_request_confirmed')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def signup_request_confirmed(request):
    return render(request, 'signup_request_confirmed.html')


def pending_requests(request):
    dietitians = User.objects.all()
    any_pending_requests = any(not dietitian.is_active for dietitian in dietitians)
    return render(request, 'pending_requests.html', {
        'dietitians' : dietitians,
        'any_pending_requests': any_pending_requests
    })

def approve_dietitian(request, dietitian_id):
    dietitian = get_object_or_404(User, id=dietitian_id)
    dietitian.is_active = True
    dietitian.save()
    return redirect("pending_requests")

def delete_request(request, dietitian_id):
    dietitian = get_object_or_404(User, id=dietitian_id)
    dietitian.delete()
    return redirect("pending_requests")


#-----------------Manage practice accounts---------------#

class PracticeList(ListView):
    model = Practice

class PracticeCreate(LoginRequiredMixin, CreateView):
    model = Practice
    fields = ['email', 'addressStreetNumberName', 'addressSuburb', 'addressCity', 'addressState', 'addressCountry', 'addressPostCode', 'phone', 'website']
    success_url = reverse_lazy('practice_list')

    def form_valid(self, form):
        form.instance.dietitian = self.request.user
        return super().form_valid(form)
    
class PracticeUpdate(LoginRequiredMixin, UpdateView):
    model = Practice
    fields = '__all__'

class PracticeDelete(LoginRequiredMixin, DeleteView):
    model = Practice
    success_url = '/practice'
    
    

# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         user_form = UserCreationForm(request.POST)
#         if user_form.is_valid():
#             user_form = user_form.save()
#             login(request, user_form)
#             return redirect('home')
#         else:
#             if 'username' in user_form.errors:
#                 username_errors = user_form.errors['username']
#                 if 'This field may only contain letters, numbers, and @/./+/-/_ characters.' in username_errors:
#                     error_message = 'Invalid characters in username. Please use only letters, numbers, and @/./+/-/_ characters.'
#                 elif 'A user with that username already exists.' in username_errors:
#                     error_message = 'Username is already taken. Please choose a different one.'
#                 else:
#                     error_message = 'Invalid username. Please choose a different one.'
#             if 'password1' in user_form.errors or 'password2' in user_form.errors:
#                 error_message = 'Invalid password - passwords do not match or are weak.'
#             else:
#                 error_message = 'Invalid sign up - try again'
#     user_form = UserCreationForm()
#     context = {
#         'user_form': user_form, 
#         'error_message': error_message}
#     return render(request, 'registration/signup.html', context)
