from django.shortcuts import render,redirect
from django.views import generic

from . import models, forms

# PARSER FILM LIST
class RezkaListView(generic.ListView):
    template_name = 'parser_app/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel


    def get_queryset(self):
        return self.model.objects.all().order_by('id')


# FORM PARSER
class RezkaFormView(generic.FormView):
    template_name = 'parser_app/rezka_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('rezka_list')
        else:
            return super(RezkaFormView, self).post(request, *args, **kwargs)






