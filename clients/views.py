from django.shortcuts import render, get_object_or_404
from .models import Client, Payment, ActivityLog

# Vista del dashboard principal
def dashboard(request):
    clients = Client.objects.all()  # Trae todos los clientes registrados
    return render(request, 'clients/dashboard.html', {'clients': clients})

# Vista para mostrar los detalles de un cliente específico
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)  # Obtiene el cliente por su ID (pk)
    routines = client.routines.all()  # Rutinas asignadas al cliente
    logs = client.activity_logs.all()  # Actividades registradas del cliente
    return render(request, 'clients/client_detail.html', {
        'client': client,
        'routines': routines,
        'logs': logs,
    })

# Vista para mostrar los pagos pendientes
def payments(request):
    payments = Payment.objects.filter(is_paid=False).order_by('due_date')  # Filtra pagos pendientes
    return render(request, 'clients/payments.html', {'payments': payments})