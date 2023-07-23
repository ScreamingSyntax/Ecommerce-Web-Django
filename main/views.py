from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from main.models import Profile
from django.views.generic import UpdateView,TemplateView
# from django.contrib.auth.
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from main.forms import UserUpdateForm,ProfileUpdateForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
class UserRegisterView(FormView):
    template_name = 'main/register.html'
    form_class = UserRegistrationForm
    success_url= reverse_lazy('login')
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('category-list')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # data = form.instance
        username = form.cleaned_data.get('username')
        messages.success(self.request, 'Your account has been created! You are now able to login')
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# class UserProfileView(TemplateView):
#     model=Profile
#     template_name='main/profile_form.html'

#     def post(self,request):
#         u_form = UserUpdateForm(instance=self.request.user)
#         p_form = ProfileUpdateForm(self.request.POST,self.request.FILES,instance=self.request.user.profile)
#         print("Hello Word")
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('profile')
#         else:
#             context= {
#                 'u_form':u_form,
#                 'p_form':p_form
#             }
#             return render(request,'main/profile_form.html',context)
#     def get_context_data(self,**kwargs):
#         u_form = UserUpdateForm(instance=self.request.user)
#         p_form = ProfileUpdateForm(self.request.POST,self.request.FILES,instance=self.request.user.profile)
#         print(u_form)
#         context = super().get_context_data(**kwargs)
#         context['u_form'] = u_form
#         context['p_form'] = p_form
#         return context

    # model = Profile.objects.
    # template_name='main/profile.html'
    # model = Profile
    # template_name= 'main/profile.html'
    # # def get(self,request,*args,**kwargs):
    # #     profile = Profile.objects.get(user=self.request.user)
    # #     context['profile']= profile
    # #     return render(request,'main/profile.html',context)
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     profile = Profile.objects.get(user=self.request.user)
    #     context['profile']=profile
    #     return context

@login_required
def profile(request):  
    if(request.method == 'POST'):
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        # if(p_form.is_valid() || u_form.is_va)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Your profile is updated successfully")
            redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    context= {
        'u_form':u_form,
        'p_form':p_form 
    }
    return render(request,'main/profile_form.html',context)