from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models, forms
from django.views import generic

#Поиск
class SearchView(generic.ListView):
    template_name = 'show.html'

    def get_queryset(self):
        return models.FilmModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context







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
class FilmListView(generic.ListView):
    template_name = 'show.html'
    model = models.FilmModel

    def get_queryset(self):
        return self.model.objects.all()




# def film_list_view(request):
#     if request.method == 'GET':
#         query = models.FilmModel.objects.all().order_by('-id')
#         context_object_name = {
#             'film': query,
#         }
#         return render(request, template_name='show.html',
#                       context=context_object_name)


# #film detail
class FilmDetailView(generic.DetailView):
    template_name = 'show_detail.html'
    context_object_name = 'film_id'

    def get_object(self, *args, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.FilmModel, id=film_id)




# def film_detail_view(request, id):
#     if request.method == 'GET':
#         query = get_object_or_404(models.FilmModel, id=id)
#         context_object_name = {
#             'film_id': query,
#         }
#         return render(request,
#                       template_name='show_detail.html',
#                       context=context_object_name)
#








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