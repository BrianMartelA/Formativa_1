from django.shortcuts import redirect, render,get_object_or_404
from .forms import SignUpForm, UserProfileForm, BoletaForm,ProductosForm
from .models import cliente,Registro_cliente, BoletaModel,Articulo, Boleta, detalle_boleta,Productos
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from alumnos.compra import Carrito
from django.db.models import Q
from .models import proveedores,amigos
from .forms import ProveedorForm,AmigosForm
from django.http import HttpResponse
from openpyxl import Workbook
from .models import amigos

# Create your views here.
def index(request):
    context ={}
    return render(request,'alumnos/index.html',context)

def galeria(request):
    context ={}
    return render(request,'alumnos/Galeria.html',context)
def contacto(request):
    context= {}
    return render(request,'alumnos/contacto.html',context)

def quienes_somos(request):
    context = {}
    return render(request,'alumnos/Quienes_somos.html',context)

def boulder(request):
    context = {}
    return render(request,'alumnos/Boulder.html',context)


def test(request):
    context ={}
    return render(request,'alumnos/test.html',context)




def registro(request):
    data ={
        'form' : SignUpForm()
    }
    if request.method=="POST":
        formulario= SignUpForm(data=request.POST)
        if formulario.is_valid():

            user=formulario.save()
            Registro_cliente.objects.create(user=user)
            group = Group.objects.get(name='cliente')
            user.groups.add(group)

            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('login')
        data["form"] = formulario
    return render(request, 'alumnos/registro.html',data)


def tienda(request):
    queryset = request.GET.get("buscar")
    articulos = Articulo.objects.all()
    if queryset:
        articulos = Articulo.objects.filter(
            Q(codigo = queryset)
        ).distinct()
    print(request.GET)
    

    datos={
        'articulos':articulos
    }
    return render(request, 'alumnos/tienda.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.agregar(articulo=articulo)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.eliminar(articulo=articulo)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Articulo.objects.get(codigo=id)
    carrito_compra.restar(articulo=articulo)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Articulo.objects.get(codigo = value['articulo_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'alumnos/detallecarrito.html',datos)

@login_required
def perfil(request):
    cliente_id = request.user.id
    boletas = BoletaModel.objects.filter(id_person_id=cliente_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'tu contraseña se ha actualizado correctamente')
            return redirect('perfil')
    else:
            form = UserProfileForm(instance=request.user)
    return render(request, 'alumnos/perfil.html',{'form':form, 'boletas':boletas})
            
def crear_boleta(request):
    if request.method == 'POST':
        form = BoletaForm(request.POST)
        if form.is_valid():
            boleta = form.save(commit=False)
            boleta.id_person = request.user
            boleta.total = boleta.cant * boleta.precio
            boleta.save()
            return redirect('test.html')
    else:
        form = BoletaForm()
    return render(request, 'test.html', {'form': form})


@login_required
def products_manage(request):
    products = Productos.objects.all()
    ctx  = {'products': products}
    return render(request, 'catalogo/product_manage.html', ctx)

@login_required
def product_add(request):
    if request.method == "POST":
        form = ProductosForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_manage')
    else:
        form = ProductosForm()
    return render(request, 'catalogo/product_add.html', {'form': form})
@login_required
def product_edit(request, id):
    product = Productos.objects.get(id=id)
    ctx = {
        'form': ProductosForm(instance=product),
        'id': id,
    }
    if request.method == "POST":
        form = ProductosForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_manage')
    return render(request, 'catalogo/products_edit.html', ctx)
@login_required
def product_delete(request, id):
    product = Productos.objects.get(id=id)
    product.delete()
    return redirect('product_manage')

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'catalogo/test.html')


def boleta(request):
    cliente_id = request.user.id
    boletas = BoletaModel.objects.filter(id_person_id=cliente_id)

    return render(request, 'alumnos/boleta.html',{'boletas':boletas})



@login_required
def proveedor_manage(request):
    proveedor_list = proveedores.objects.all()
    ctx = {'proveedores': proveedor_list}
    return render(request, 'proveedores/provider_manage.html', ctx)
@login_required
def proveedor_add(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('provider_manage')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/provider.html', {'form': form})
@login_required
def proveedor_edit(request, id):
    proveedor = get_object_or_404(proveedores, id=id)
    if request.method == "POST":
        form = ProveedorForm(request.POST, request.FILES, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('provider_manage')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/provider_edit.html', {'form': form, 'id': id})
@login_required
def proveedor_delete(request, id):
    proveedor = get_object_or_404(proveedores, id=id)
    proveedor.delete()
    return redirect('provider_manage')

def amigos_manage(request):
    amigos_list = amigos.objects.all()
    ctx = {'amigos':amigos_list}
    return render(request,'personas/amigos_manage.html',ctx)

def amigos_add(request):
    if request.method =='POST':
        form =AmigosForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('amigos_manage')
    else:
        form = AmigosForm()
        return render(request,'personas/amigos.html',{'form':form})

@login_required
def exportar_productos_excel(request):
    productos = Productos.objects.all()
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Productos"

    # Cabecera
    ws.append(['ID', 'Nombre', 'Descripción', 'Precio', 'Stock', 'Categoría'])

    # Datos
    for p in productos:
        ws.append([p.id, p.nombre, p.description, p.price, p.stock, str(p.categoria)])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=productos.xlsx'
    wb.save(response)
    return response