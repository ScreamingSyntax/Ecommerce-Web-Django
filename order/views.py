from django.shortcuts import render,redirect
from products.models import Products
from django.views.generic import ListView,TemplateView,CreateView
from order.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Orders
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
    
class OrderCheckoutForm(CreateView):
    model = Orders
    fields=['shipping_address','user_city','user_mobile','final_amount']
    # cart = Cart
    def form_valid(self,form):
        # form.instance.save()
        address = form.cleaned_data.get('shipping_address')
        city = form.cleaned_data.get('user_city')
        mobile = form.cleaned_data.get('user_mobile')
        print(f"{address} {city} {mobile}")
        # order = Orders.objects.create(user=self.request.user,shipping_address=address,user_city=city,user_mobile=mobile)
        selected_products = Cart.objects.filter(user=self.request.user).values_list('product', flat=True)
        print(selected_products)
        # order.products.set(selected_products)
        # order.save()
        return super().form_valid(form)
        # for cart in cart:
        #     print(cart)

# class OrderCustomerView(ListView):
#     model= Order
#     context_object_name='objects'