from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required

#from NutInf import views
from .views import listarNutInfo, crearNut_Info, editarNutInfo, eliminarNutInfo, Inicio, crearProducto, listarProducto, listarNutProduct




urlpatterns = [
    
    path('indiceNut/', login_required(Inicio.as_view()), name="ValorNut"),
    path('crear_valor/', login_required(crearNut_Info.as_view()), name="crear_valor"),
    path('lista_valores/', login_required(listarNutInfo.as_view()), name="lista_valores"),
    path('editar_valor/<int:pk>', login_required(editarNutInfo.as_view()), name="editar_valor"),
    path('eliminar_valor/<int:pk>', login_required(eliminarNutInfo.as_view()), name="eliminar_valor"),
    path('crear_producto/', login_required(crearProducto.as_view()), name="crear_producto"),
    path('lista_productos/', login_required(listarProducto.as_view()), name="lista_productos"),
    path('lista_totales/', login_required(listarNutProduct.as_view()), name="lista_totales"),

]