from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Player


class IndexView(generic.ListView):
    template_name = 'playerstats/index.html'
    context_object_name = 'highest_rank_player_list'

    def get_queryset(self):
        """
        Return the five highest ranking players

        """

        return Player.objects.filter(
            tier='challenger',
            region='na1'
        ).order_by('-leaguepoints')[:5]


class DetailView(generic.DetailView):
    model = Player
    template_name = 'playerstats/detail.html'
    
    def get_queryset(self):
        return Player.objects