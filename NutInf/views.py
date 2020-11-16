from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import NutinfForm, ProductsForm
from NutInf.models import Nutinf, Products, NutProduct


class Inicio(TemplateView):
    template_name= 'NutInf/indiceNut.html'

class crearNut_Info(CreateView):
    model= Nutinf
    template_name= 'NutInf/crear_valor.html'
    form_class= NutinfForm
    success_url= '/lista_valores'

class listarNutInfo(ListView):
    model= Nutinf
    template_name='NutInf/lista_valores.html'
    context_object_name='infonuts'
    queryset= Nutinf.objects.all()

class editarNutInfo(UpdateView):
    model= Nutinf
    template_name= 'NutInf/crear_valor.html'
    form_class= NutinfForm
    success_url= '/lista_valores'

class eliminarNutInfo(DeleteView):
    model= Nutinf
    template_name= 'NutInf/eliminar_valor.html'
    form_class= NutinfForm
    success_url= '/lista_valores'


class crearProducto(CreateView):
    model= Products
    template_name= 'NutInf/crear_producto.html'
    form_class= ProductsForm
    success_url= '/lista_productos'

class listarProducto(ListView):
    model= Products
    template_name='NutInf/lista_productos.html'
    context_object_name='products'
    queryset= Products.objects.all()

class listarNutProduct(ListView):
    model= NutProduct
    template_name='NutInf/lista_totales.html'
    context_object_name='nutproducts'
    queryset= NutProduct.objects.all()
    








