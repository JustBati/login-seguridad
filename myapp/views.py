# myapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import Maquina, Prestamo
from django.views.decorators.http import require_http_methods
from .forms import MaquinaForm, SignUpForm 
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login


def login_register_view(request):
    if request.method == 'POST':
        if 'register_form' in request.POST:
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('main_page')
        elif 'login_form' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main_page')

    register_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'login_register.html', {
        'register_form': register_form,
        'login_form': login_form
    })


@login_required
def main_page_view(request):
    # Inicializa el formulario pero no lo muestres a menos que el usuario sea superusuario
    form = None
    is_admin = request.user.is_superuser
    
    if is_admin:
        if request.method == 'POST':
            form = MaquinaForm(request.POST)
            if form.is_valid():
                form.save()
                # Si quieres que la página se recargue tras añadir la máquina:
                form = MaquinaForm()  # Reinicia el formulario para que esté limpio después del POST
            # Si el formulario no es válido, se pasará con los errores al template
        else:
            form = MaquinaForm()

    context = {
        'is_admin': is_admin,
        'form': form,  # Esto puede ser None si el usuario no es admin
    }
    return render(request, 'main_page.html', context)

@login_required
@permission_required('myapp.add_maquina', raise_exception=True)
@require_http_methods(["POST"])
def add_machine(request):
    form = MaquinaForm(request.POST)
    if form.is_valid():
        new_machine = form.save()
        # Devuelve una respuesta positiva junto con la información de la máquina recién creada.
        data = {
            'id': new_machine.id,
            'tipo': new_machine.tipo,
            'marca': new_machine.marca,
            'modelo': new_machine.modelo,
            'numero_serie': new_machine.numero_serie,
            'observaciones': new_machine.observaciones
        }
        return JsonResponse({'success': 'Máquina añadida correctamente', 'machine': data}, status=201)
    else:
        # Devuelve una respuesta con los errores del formulario.
        return JsonResponse({'error': form.errors}, status=400)

@login_required
@permission_required('myapp.delete_maquina', raise_exception=True)
@require_http_methods(["DELETE"])
def delete_machine(request, id):
    # Obtén la máquina por su ID y si no existe devuelve un error 404
    maquina = get_object_or_404(Maquina, id=id)

    # Elimina la máquina
    maquina.delete()

    # Devuelve una respuesta para indicar que la máquina ha sido eliminada
    return JsonResponse({'success': 'Máquina eliminada correctamente'}, status=204)

@login_required
def get_machines(request):
    machines = Maquina.objects.all().values(
        'id', 'tipo', 'marca', 'modelo', 'numero_serie', 'observaciones'
    )
    return JsonResponse(list(machines), safe=False)

@login_required
@require_http_methods(["POST"])
def loan_machine(request):
    user = request.user
    maquina_id = request.POST.get('maquina_id')  # Asegúrate de enviar 'maquina_id' desde el cliente

    try:
        maquina = Maquina.objects.get(id=maquina_id)
        prestamo = Prestamo.objects.create(
            maquina=maquina,
            usuario=user,
            fecha_prestamo=timezone.now()
            # La fecha de devolución puede ser añadida más tarde
        )
        return JsonResponse({'success': 'Préstamo registrado con éxito', 'prestamo_id': prestamo.id}, status=201)
    except Maquina.DoesNotExist:
        return JsonResponse({'error': 'Máquina no encontrada'}, status=404)
    
@login_required
def get_loans(request):
    loans = Prestamo.objects.all().values(
        'id', 'usuario__Nombre', 'maquina__tipo', 'maquina__marca', 
        'maquina__modelo', 'fecha_prestamo', 'fecha_devolucion'
    )
    return JsonResponse(list(loans), safe=False)
