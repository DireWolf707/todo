from django.views.generic import CreateView,ListView,UpdateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from .models import Todo
from django.shortcuts import redirect,get_object_or_404
from django.utils import timezone
from .forms import TodoForm
from django.contrib import messages

class TodoCreateView(LoginRequiredMixin,CreateView):
    template_name = 'create.html'
    form_class = TodoForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        success_message = "Todo added successfully"
        messages.success(self.request, success_message)
        return redirect('current')

class TodoCurrentView(LoginRequiredMixin,ListView): 
    context_object_name = 'todos'
    template_name = 'current.html'
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user,date_completed__isnull=True)
    
class TodoUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Todo
    template_name = 'update_view.html'  
    form_class = TodoForm
    
    def form_valid(self, form):
        self.object = form.save()
        success_message = "Todo updated successfully"
        messages.warning(self.request, success_message)
        return redirect('current')
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user and obj.date_completed is None
    
class todo_complete(LoginRequiredMixin,UserPassesTestMixin,View):
    def post(self, request, *args, **kwargs):
        todo = self.object
        todo.date_completed = timezone.now()
        todo.save()
        return redirect("current")
    
    def test_func(self):
        self.object = get_object_or_404(Todo,user=self.request.user,pk=self.kwargs.get('pk'))
        return self.object.date_completed is None
    

class todo_delete(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo,pk=kwargs['pk'],user=request.user)
        todo.delete()
        success_message = "Todo deleted successfully"
        messages.error(request, success_message)
        return redirect("completed_todos")
    
class TodoCompleteView(LoginRequiredMixin,ListView):
    context_object_name = 'todos'
    template_name = 'completed_todos.html'
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user,date_completed__isnull=False).order_by('-date_completed')