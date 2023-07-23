from django.shortcuts import render,redirect
from products.models import Products
from django.views.generic import ListView,TemplateView,CreateView
from order.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Orders,OrderItem
# from django.contrib.auth.
from django.http import HttpResponse,HttpResponseRedirect
# from django.dispatch import 
# from django.urls import reverse,reverse_lazy

class CartView(LoginRequiredMixin,ListView):
    template_name='order/cart.html'
    def get(self,request):
        user= self.request.user
        cart= user.cart_set.all()
        grand_total = 0
        for items in cart:
            grand_total+=items.sub_total
        context={
            'carts':cart,
            'total':grand_total
        }
        return render(self.request,'order/cart_list.html',context)

class DeleteCart(LoginRequiredMixin,TemplateView):
    template_name = 'order/cart_list.html'

    def get(self, request, *args, **kwargs):
        cart_id = request.GET.get('product_obj')
        user = self.request.user
        user.cart_set.get(id=cart_id).delete()
        return redirect('cart')

class IncrementCart(LoginRequiredMixin,TemplateView):
    template_name='order/cart_list.html'
    def get(self,request,*args,**kwargs):
        cart_id = request.GET.get('product_obj')
        user=self.request.user
        cart_item = user.cart_set.get(id=cart_id)
        print("Increment Called")
        cart_item.quantity+=1
        cart_item.save()
        return redirect('cart')

class DecrementCart(LoginRequiredMixin,TemplateView):
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
    
class OrderCheckoutForm(LoginRequiredMixin,CreateView):
    model = Orders
    fields=['shipping_address','user_city','user_mobile']
    def form_valid(self, form):
        selected_products = Cart.objects.filter(user=self.request.user)
        form.instance.user = self.request.user
        form.instance.final_amount = 0  
        form.instance.save()
        order_instance = form.instance
        for cart_item in selected_products:
            order_item = OrderItem(
                order=order_instance,
                product=cart_item.product,
                quantity=cart_item.quantity
            )
            order_item.save()
            form.instance.final_amount += cart_item.sub_total
        form.instance.save()
        Cart.objects.all().delete()
        return super().form_valid(form)

class OrderStatus(LoginRequiredMixin,TemplateView):
    template_name='order/order_status.html'
    def get(self,request):
        user = self.request.user
        order = Orders.objects.filter(user=user)
        orders_list= []
        for order in order:
            order_item = OrderItem.objects.filter(order=order)
            for orders in order_item:
                orders_list.append(orders)
        context ={
            'order_list':orders_list
        }
        print(context)

        return render(request,'order/order_status.html',context)