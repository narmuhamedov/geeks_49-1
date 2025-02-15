from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

#Cписок задач

class TodoListView(generic.ListView):
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_lst'
    model = models.TodoModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def todo_list(request):
#     if request.method == 'GET':
#         query = models.TodoModel.objects.all()
#         context_object_name = {
#             'todo_lst': query,
#         }
#         return render(request, template_name='todo/todo_list.html',
#                   context=context_object_name)

#Добавление задач
class CreateTodoView(generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)



# def create_todo(request):
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_lst')
#     else:
#         form = forms.TodoForm()
#     return render(request, template_name='todo/create_todo.html',
#                   context={'form': form})

#Удаление задачи
class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, *args, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)





# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     todo_id.delete()
#     return redirect('todo_lst')

#Изменение данных
class UpdateTodoView(generic.UpdateView):
    template_name = 'todo/update_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def get_object(self, *args, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)






# def update_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, instance=todo_id)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_lst')
#     else:
#         form = forms.TodoForm(instance=todo_id)
#     return render(request, template_name='todo/update_todo.html',
#                   context={
#                       'form': form,
#                       'todo_id': todo_id,
#                   })