from django.shortcuts import render
from application.service import ran
from application.models import Car

menu = ["О сайте", "Добавить статью", "Обратная связь"]

def index(request):
    all_entries = Car.objects.all()
    #print("all_entries", all_entries)
    return render(request, 'applications/index.html', {'title': 'Главная страница', 'menu': menu, 'ran': ran(),
                                                       'all_entries': all_entries})
