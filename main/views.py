from django.shortcuts import redirect, render
from main.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# from django.contrib.auth.
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

class UserRegisterView(FormView):
    template_name = 'main/register.html'
    form_class = UserRegistrationForm
    success_url= reverse_lazy('login')
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('category-list')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, 'Your account has been created! You are now able to login')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
