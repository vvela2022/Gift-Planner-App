from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Board, Gift_Idea
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class BoardList(TemplateView):
    template_name = "board_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get('title')
        if title != None:
            context['boards'] = Board.objects.filter(title__icontains=title)
            context['header'] = f"Searching for {title}"
        else:
            context["boards"] = Board.objects.all()
            context['header'] = f"Enter your search below"
        return context

class BoardCreate(CreateView):
    model = Board
    fields = ['title', 'image', 'about']
    template_name = 'board_create.html'
    def get_success_url(self):
        return reverse('board_detail', kwargs={'pk': self.object.pk})

class BoardDetail(DetailView):
    model = Board
    template_name = 'board_detail.html'

class BoardUpdate(UpdateView):
    model = Board
    fields = ['title', 'image', 'about']
    template_name = 'board_update.html'
    def get_success_url(self):
        return reverse('board_detail', kwargs={'pk': self.object.pk})

class BoardDelete(DeleteView):
    model = Board
    template_name = 'board_delete_confirmation.html'
    success_url = '/boards/'

class Gift_IdeaCreate(View):

    def post(self, request, pk):
        idea = request.POST.get('idea')
        image = request.POST.get('image')
        link = request.POST.get('link')
        date_needed = request.POST.get('date_needed')
        board = Board.objects.get(pk=pk)
        Gift_Idea.objects.create(idea=idea, image=image, link=link, date_needed=date_needed, board=board)
        return redirect('board_detail', pk=pk)
   