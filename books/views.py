from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

def writers(request):
    writers_list = [
        "Лев Толстой",
        "Чингиз Айтматов",
        "Фёдор Достоевский",
        "Омар Хайям",
        "Уильям Шекспир",
        "Франсуа Рабле",
        "Джейн Остин",
        "Эрнест Хемингуэй",
        "Габриэль Гарсиа Маркес",
        "Антуан де Сент-Экзюпери"
    ]
    return HttpResponse("<br>".join(writers_list))

def quotes(request):
    quotes_list = [
        "“Жизнь — это МЫК. Ауф (безумноо можно быть последним)” — Ч. Айтматов",
        "“Все счастливые семьи похожи на не счастливых.” — Л. Толстой",
        "“Красота сосет мир.” — Ф. Достоевский",
        "“Быть или сдохнуть.” — Шекспир",
        "“Человек рожден для поражения.” — Хемингуэй"
    ]
    return HttpResponse("<br>".join(quotes_list))

def system_time(request):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {now}")
