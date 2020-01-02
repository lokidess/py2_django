from django.views.generic import TemplateView, FormView, CreateView, ListView, DeleteView

from core.models import Todo


class IndexView(CreateView, ListView):
    template_name = 'index.html'
    success_url = '/'
    model = Todo
    fields = '__all__'
    queryset = model.objects.all()
    context_object_name = 'todos'


class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'delete-todo.html'
    success_url = '/'

    # def post(self, request):
    #     form = CreateTodoForm(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #     context = self.get_context_data()
    #     context['form'] = form
    #     return self.render_to_response(context)

    # def get(self, request, *args, **kwargs):
    #     pass
    #
    # def post(self, request):
    #     pass
