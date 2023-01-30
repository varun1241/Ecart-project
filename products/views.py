from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import*
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm

from django.urls import reverse, reverse_lazy
class HomePage(APIView):
    def get(self,request):
        print("The login user is ",request.session.get('user'))
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
      
        product=Product.objects.all()
        productnmae=Product.objects.all()[:5]
        print(productnmae)


        return render(request,template_name='home.html',context={"data":product})
    
    def post(self,request):

        product=request.POST.get('product_id')
        remove=request.POST.get('remove')
        print(product)

        cart=request.session.get('cart')
        #here we check a cart and if not create one using session
        if cart:
            quantity=cart.get(product)

            print("quantity",quantity)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product ]=1

           
        else:
            cart={}
            cart[product ]=1
        
        request.session['cart']=cart
        print(request.session['cart'])

        return redirect('home')


# Create your views here.

class Login(APIView):
    def get(self,request):
        print("hello entered")
        return render(request,template_name='login.html')


    def post(self,request):

        if request.method == 'POST':
            user = auth.authenticate(username=request.POST.get('usernam'),password = request.POST.get('password'))
            if user is not None:
                request.session['user']=user.username
                auth.login(request,user)
                return redirect('home')
            else:
                return render (request,'login.html', {'error':'Username or password is incorrect!'})
        else:
            return render(request,'login.html')
                  
class Singup(APIView):
    def get(self,request):
       
        return render(request,template_name='signup.html')


    def post(self,request):
        if request.method == "POST":
            if request.POST.get('password1') == request.POST.get('password2'):
                try:
                    User.objects.get(username =request.POST.get('usernam'))
                    return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST.get('usernam'),password=request.POST.get('password1'))
                    auth.login(request,user)
                    return redirect('login')
            else:
                return render (request,'signup.html', {'error':'Password does not match!'})
        else:
            return render(request,'signup.html')



def logout(request):
    request.session.clear()

    return redirect('login')

class Cart(APIView):
    def get(self , request):
      
        try:
            ids = list(request.session.get('cart').keys())
       
    
            products = Product.get_products_by_id(ids)
        # print(products)
        # return redirect('home')
            return render(request , 'cart.html' , {'products' : products} )
        except:
            return redirect('home')


class ProductView(APIView):
    # def get(self,request):

    #      return render (request,'productview.html')


    def post(self,request):
        pruct_id=request.POST.get('product_id')
        products=Product.objects.filter(product_id=pruct_id)
       

        return render (request,'productview.html',{'products' : products})


class TaskCreateView(APIView):

    def get(self,request):
        return render (request,'productadd.html')


    def post(self,request):
        tutorial_data = request.data
        print(tutorial_data)
        product_name=request.POST['product_name']
        print(product_name)
        pro_price=request.POST['pro_price']
        print(pro_price)
        strap_color=request.POST['strap_color']
        print(strap_color)
        highlights=request.POST['highlights']
        print(highlights)
        productimage=request.FILES['productimage']
        print(productimage)
        
        product=Product(product_name=product_name,price=pro_price,strap_color=strap_color,highlights=highlights,image=productimage,status=True)
        product.save()
        return redirect('home')

        
     
class TaskUpdateView(APIView):
    def get(self,request):
        return render (request,'productadd.html')
    model = Product
    form_class = ProductForm
    template_name = 'updateproduct.html'
    success_url = reverse_lazy('home')

class ProductDeleteView(DeleteView):
    model = Product 
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('home')
     
  


