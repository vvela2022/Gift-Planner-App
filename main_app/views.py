from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Board:
    def __init__(self, title, image, about):
        self.title = title
        self.image = image
        self.about = about


boards = [Board("Gifts for Troy","https://cdn3.vectorstock.com/i/1000x1000/79/32/happy-birthday-gifts-pack-vector-16147932.jpg", "Gifts for my brother, Troy"), Board("Gifts for Mom", "https://media.istockphoto.com/vectors/isometric-gift-flat-icon-pixel-perfect-for-mobile-and-web-vector-id1152848595?k=20&m=1152848595&s=612x612&w=0&h=T9QQc2EYpvnB_sBzvcNrraL77VE9aXQlA86xum364uU=", "Ideas for my mom" )]

class BoardList(TemplateView):
    template_name = "board_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["boards"] = boards
        return context
