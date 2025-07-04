from django.urls import path
from . import views
from alumnos.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.registro,name='register'),
    path('index',views.index,name='index'),
    path('galeria',views.galeria,name='galeria'),
    path('contacto',views.contacto,name='contacto'),
    path('quienes_somos',views.quienes_somos,name='quienes_somos'),
    path('boulder',views.boulder,name='boulder'),
    path('registro',views.registro,name='registro'),
    path('perfil',views.perfil, name='perfil'),
    path('test',views.test,name='test'),
    path ('boleta',views.boleta,name='boleta'),

    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('product/manage/',views.products_manage, name='product_manage'),
    path('product/add/',views.product_add, name='product_add'),
    path('product/edit/<int:id>/',views.product_edit, name='product_edit'),
    path('product/delete/<int:id>/',views.product_delete, name='product_delete'),

    path('test', views.test, name='test'),
    path('', views.home, name='home'),

    path('proveedor/manage/', views.proveedor_manage, name='provider_manage'),
    path('proveedor/agregar/', views.proveedor_add, name='provider_add'),
    path('proveedor/editar/<str:id>/', views.proveedor_edit, name='provider_edit'),
    path('proveedor/eliminar/<str:id>/', views.proveedor_delete, name='provider_delete'),


  

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


]
