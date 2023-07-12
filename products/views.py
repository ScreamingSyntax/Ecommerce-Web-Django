from django.shortcuts import render,redirect

from django.views.generic import CreateView,ListView,DetailView,TemplateView
from products.models import Products,Category
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Cart
from django.contrib import messages
class ProductForm(CreateView):
    model = Products
    fields = ['name','sub_title','description','quantity','image','category','price']

class ProductsListView(ListView):
    model = Products
    context_object_name='products'

  
class CategoryListView(ListView):
    model = Category
    context_object_name='categories'
    template_name='products/category_list.html'
    # ordering[]
    def get_context_data(self,**kwargs):
       context = super().get_context_data(**kwargs)
       most_viwed=Products.objects.order_by('-viwed_times')[:3]
       most_sold = Products.objects.order_by('-sold_times')[:3]
       context['categories']= Category.objects.all()
       context['most_viwed']= most_viwed
       context['most_sold']= most_sold
       return context


class CategoryDetailView(DetailView):
    model = Category

class ProductDetailView(DetailView):
    model = Products
    def get(self,request,pk):
       product_detail = Products.objects.get(id=pk)
       product_detail.viwed_times+=1
       product_detail.save()
       context = {
          'object':product_detail
       }
       return render(request,'products/products_detail.html',context)
    def post(self,request,pk):
      if not self.request.user.is_authenticated:
          return redirect('login')
      product_id = pk
      product_detail = Products.objects.get(id=product_id)
      cart_check = Cart.objects.filter(product=product_detail,user=self.request.user)
    #   print(self.request.path_info)
      if len(cart_check) == 0:
          print("Has 0")
          cart=Cart(product = product_detail,user= self.request.user)
          cart.save()
          messages.success(self.request,'Successfully added the product to cart')
          return HttpResponseRedirect(self.request.path_info)
      else:
         cart = cart_check.first()
         if(cart.quantity < cart.product.quantity):
           cart.quantity+=1
           cart.save()
           print(Cart.objects.all().first().quantity)
           messages.info(self.request,'Successfully updated quantity to cart')
           return HttpResponseRedirect(self.request.path_info)
         else:
           messages.warning(self.request,'Maximum Quantity Already added Bro')
           return HttpResponseRedirect(self.request.path_info)
     
     

class SearchProductView(TemplateView):
    template_name="products/search_product.html"
    def get(self,request,*args,**kwargs):
        # print(self.request.user)
        product_name = self.request.GET['search']
        # filtered_products = Products.objects.filter(name=product_name)
        filtered_products = Products.objects.filter(name__startswith=product_name).values() or Products.objects.filter(category__name__startswith=product_name).values()
        for products in filtered_products:
           print(products["image"])
        # print(filtered_products)
        context= {
            'searched_products':filtered_products,
        }
        return render(request,'products/search_product.html',context) 
    # def post()

class SearchAddToCart(LoginRequiredMixin,TemplateView):
    template_name="products/search_product.html"
    def post(self,request,pk,*args,**kwargs):
        if not self.request.user.is_authenticated:
            return  redirect('login')
        # print(pk)
        product_id=pk
        product_obj = Products.objects.get(id=product_id)
        filtered_products = Products.objects.filter(name=product_obj.name)
        context= {
            'searched_products':filtered_products
            }
        cart_check = Cart.objects.filter(product=product_obj,user=self.request.user)
        if len(cart_check) == 0:
            cart=Cart(product = product_obj,user= self.request.user)
            cart.save()
            messages.success(request,'The Product is Added Bro')
            return render(request,'products/search_product.html',context)
        else:
          cart = cart_check.first()
          if(cart.quantity < cart.product.quantity):
            cart.quantity+=1
            cart.save()
            print(Cart.objects.all().first().quantity)
            messages.success(self.request,'Successfully updated quantity to cart')
            return render(request,'products/search_product.html',context)
          else:
            messages.warning(self.request,'Maximum Quantity Already added Bro')
            return render(request,'products/search_product.html',context)