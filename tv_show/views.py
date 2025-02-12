from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models, forms

#create reviews
def create_review_view(request):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)  # Сначала создаем объект, но не сохраняем
            review.save()  # Теперь сохраняем в базе данных
            film_id = review.choice_show.id  # Получаем id связанного фильма
            return redirect('film_detail', id=film_id)  # Передаем id фильма
    else:
        form = forms.CreateReviewForm()
    return render(request, template_name='create_review.html',
                  context={'form': form})



#films list
def film_list_view(request):
    if request.method == 'GET':
        query = models.FilmModel.objects.all().order_by('-id')
        context_object_name = {
            'film': query,
        }
        return render(request, template_name='show.html',
                      context=context_object_name)

#film detail
def film_detail_view(request, id):
    if request.method == 'GET':
        query = get_object_or_404(models.FilmModel, id=id)
        context_object_name = {
            'film_id': query,
        }
        return render(request,
                      template_name='show_detail.html',
                      context=context_object_name)









def emodji(request):
    if request.method == 'GET':
        return HttpResponse('😀 😅 😜')

def text(request):
    if request.method == 'GET':
        return HttpResponse('Lorem ipsum dolor sit amet')

def image(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Hello</h1>'
                            '<img src="https://wp-s.ru/wallpapers/0/6/345228397232059/fon-rabochego-stola-microsoft-belyj-na-chernom.jpg" />')