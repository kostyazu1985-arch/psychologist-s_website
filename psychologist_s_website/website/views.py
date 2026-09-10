from django.shortcuts import render, redirect
from models import Appointment

# Create your views here.
def index(request):
    if request.method == "POST":
        client_name = request.POST.get('name', '').strip()
        client_tg = request.POST.get('telegram', '').strip()
        client_req = request.POST.get('request', '').strip()

        agree_data = request.POST.get('agree_data')

        if not client_name or not client_tg or not client_req:
            return render(request, 'website/index.html', {
                'error_message': 'Ошибка безопасности: Все поля обязательны для заполнения!'
            })

        if not agree_data:
            return render(request, 'website/index.html', {
                'error_message': 'Вы должны дать согласие на обработку персональных данных!'
            })

        Appointment.objects.create(
            name=client_name,
            telegram=client_tg,
            client_request=client_req
        )

        return redirect('index')

    return render(request, 'website/index.html')