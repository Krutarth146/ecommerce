from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.views import View


class CreateCategory(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'products/createcategory.html'
    success_url = '/products/listcategories'

class ListCategory(ListView):
    model = Category
    template_name = 'products/listcategories.html'
    context_object_name = 'categories'
    ordering = ['name']

class DeleteCategory(DeleteView):
    model = Category
    template_name = 'products/deletecategories.html'
    success_url = '/products/listcategories'

class UpdateCategory(UpdateView):
    model = Category
    template_name = "products/updatecategory.html"
    fields = '__all__'
    success_url = '/products/listcategories'


# -----------------------------------------------------

class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/createproducts.html'
    success_url  = '/listproducts'


class ListProducts(ListView):
    model = Product
    # paginate_by = 50
    template_name = 'products/listproducts.html'
    context_object_name = 'products'
    ordering = ['title']

#     # def get_queryset():

class DetailProduct(DetailView):
    model = Product
    template_name = 'products/detailsproduct.html'
    context_object_name = 'products'

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/deleteproduct.html'
    success_url = '/listproducts'

class UpdateProduct(UpdateView):
    model = Product
    template_name = "products/updateproduct.html"
    fields = '__all__'
    success_url = '/listproducts'
    

class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(product,cart)
        return redirect('index')
        

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products() 

        context = {}
        context['products'] = products
        context['categories'] = categories
        print(request.session.get('username'))
        print(request.session.get('customer_id'))
        return render(request,'index.html',context)


from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from user.models import User
from django.views import  View
from .models import Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
    
from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from user.models import User
from django.views import View

from .models import Product,Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('user')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=User(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')