from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from django.http import HttpResponseRedirect

class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    template_name = 'create.html'
    fields =('title','memo','important',)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

class TodoCurrentView(LoginRequiredMixin,ListView): 
    context_object_name = 'todos'
    template_name = 'current.html'
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user,date_completed__isnull=True)
    
    