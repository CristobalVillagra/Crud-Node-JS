from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from crud.models import Producto, Proveedor
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def products(request):
    context = {'productos': Producto.objects.all(),'proveedores': Proveedor.objects.all()}
    return render(request,'core/products.html',context)

def products_by_proveedor(request, proveedor):
    context = {'productos': Producto.objects.filter(proveedor = proveedor),'proveedores': Proveedor.objects.all()}
    return render(request,'core/products.html',context)


def login (request):
    login(request)
    return redirect('core/inicioSesion.html')

def exit (request):
    logout(request)
    return redirect('home')  

## clases para paysystem
class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
