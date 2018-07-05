from django.shortcuts import get_object_or_404
from django.views.generic import View, ListView
from django.http import HttpResponse
from django.db.models import F

from .models import UserProfile


class ListUsersView(ListView):
    model = UserProfile
    template_name = 'voting/vote.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = UserProfile.objects.all()
        return context


class ClapView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        profile = get_object_or_404(UserProfile, pk=pk)
        profile.votes = F('votes') + 1
        profile.save()
        profile.refresh_from_db()
        return HttpResponse('{}'.format(profile.votes))


class GetWinning(View):

    def get(self, request, *args, **kwargs):
        winning = UserProfile.objects.order_by('-votes').first()
        return HttpResponse('')
