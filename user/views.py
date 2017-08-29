from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import FormView
from user.forms import SignUpForm,SettingsForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from user.forms import SignUpForm,SettingsForm



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('news:index')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

class UpdateView(FormView):
    template_name = 'user/updateprofile.html'
    form_class = SettingsForm
    success_url = '/'

    def form_valid(self,form):
        form = form.cleaned_data
        ret = super(UpdateView,self).form_valid(form)
        if(ret):
            self.request.user.first_name = form['first_name']
            self.request.user.last_name = form['last_name']
            self.request.user.email = form['email']
            self.request.user.save()
        return ret


#change password
@login_required(login_url='/')
def change_password(request):
 if request.method == 'POST':
     form = PasswordChangeForm(request.user, request.POST)
     if form.is_valid():
         user = form.save()
         update_session_auth_hash(request, user)  # Important!
         messages.success(request, 'Your password was successfully updated!')
         return redirect('/')
     else:
         messages.error(request, 'Please correct the error below.')
 else:
     form = PasswordChangeForm(request.user)
 return render(request, 'user/update_password.html', {
     'form': form
 })
