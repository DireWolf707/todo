from django.views.generic import CreateView,ListView,UpdateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Todo
from django.shortcuts import redirect,get_object_or_404
from django.utils import timezone

class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    template_name = 'create.html'
    fields =('title','memo','important',)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return redirect("current")

class TodoCurrentView(LoginRequiredMixin,ListView): 
    context_object_name = 'todos'
    template_name = 'current.html'
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user,date_completed__isnull=True)
    
class TodoUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Todo
    template_name = 'update_view.html'  
    fields = ('title','memo','important',)
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    
class todo_complete(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo,pk=kwargs['pk'],user=request.user)
        todo.date_completed = timezone.now()
        todo.save()
        return redirect("current")

class todo_delete(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo,pk=kwargs['pk'],user=request.user)
        todo.delete()
        return redirect("current")
