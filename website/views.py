#КОНТРОЛЛЕР БЭКЕНДА
import socket
from django.shortcuts import render, redirect
from .models import Appointment
from django.core.mail import send_mail


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

        try:
            subject = f"Новая заявка на консультацию от {client_name}"
            message = (
                f"Здравствуйте Марина!\n\n"
                f"На вашем сайте оставлено новое обращение:\n"
                f"• Имя клиента: {client_name}\n"
                f"• Контакт в Telegram: {client_tg}\n"
                f"• Текст психологического запроса: {client_req}\n\n"
                f"Данные успешно зафиксированы в СУБД SQLite вашего сайта."
            )

            send_mail(
                subject=subject,
                message=message,
                from_email='kostyazu2014@yandex.ru',
                recipient_list=['kostyazu2014@yandex.ru'],
                fail_silently=False,
            )
            print("✅ Письмо успешно отправлено через SMTP!")
        except socket.gaierror as e:
            print(f"❌ Ошибка DNS (getaddrinfo failed): Не удалось найти сервер SMTP. Проверьте EMAIL_HOST в settings.py. Детали: {e}")
        except Exception as e:
            print(f"❌ Системное исключение при отправке Email: {e}")

        return redirect('index')

    return render(request, 'website/index.html')

def oferta(request):
    return render(request, "website/oferta.html")

def privacy(request):
    return render(request, "website/privacy.html")