from django.shortcuts import render,redirect
from products.models import Products
from django.views.generic import ListView,TemplateView
from order.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.
from django.http import HttpResponse,HttpResponseRedirect
# from django.dispatch import 
# from django.urls import reverse,reverse_lazy

class CartView(LoginRequiredMixin,ListView):
    template_name='order/cart.html'
    # model = Cart
    # context_object_name='carts'
    def get(self,request):
        # Cart.objects.filter()
        user= self.request.user
        cart= user.cart_set.all()
        context={
            'carts':cart
        }
        return render(self.request,'order/cart_list.html',context)
        # return HttpResponse(self.request,"Hello")

class DeleteCart(TemplateView):
    # template_name='order/cart_list.html'
    template_name = 'order/cart_list.html'

    def get(self, request, *args, **kwargs):
        cart_id = request.GET.get('product_obj')
        # print(self.request.user)
        user = self.request.user
        user.cart_set.get(id=cart_id).delete()
        return redirect('cart')
    # def post(self,request,pk):
    # product_id = request.POST.get(pk=pk)
    # print(f'thsi si product_id {pk}')
    # return reverse_lazy('cart_list')

class IncrementCart(TemplateView):
    template_name='order/cart_list.html'
    def get(self,request,*args,**kwargs):
        cart_id = request.GET.get('product_obj')
        user=self.request.user
        cart_item = user.cart_set.get(id=cart_id)
        print("Increment Called")
        cart_item.quantity+=1
        cart_item.save()
        return redirect('cart')

class DecrementCart(TemplateView):
    template_name='order/cart_list.html'
    def get(self,request,*args,**kwargs):
        cart_id = request.GET.get('product_obj')
        print("Decrement Called")
        user=self.request.user
        cart_item = user.cart_set.get(id=cart_id)
        # print('this is cart', cart_item.quantity)
        if(cart_item.quantity==1):
            cart_item.delete()
        else:    
            cart_item.quantity-=1
            cart_item.save()
        return redirect('cart')