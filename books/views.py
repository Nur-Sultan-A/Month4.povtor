from django.shortcuts import render, get_object_or_404
from .models import Book
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


#hw 2 views for books app

def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/book_detail.html', {'book': book})
