from TelegramBot.models import Cliente, Subscription
from TelegramBot.forms import ClienteForm, SubscriptionForm
from TelegramBot.telegram import threadTelegramReader, bot
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import telebot

# Inizializzo il bot
pin = None
pin_inserted = False
    
# Views
class Home(TemplateView):
    template_name = "TelegramBot/home.html"

class ClienteList(ListView):
    model = Cliente
    template_name = "TelegramBot/users.html"

class ClienteCreate(CreateView):
    form_class = ClienteForm
    template_name = 'TelegramBot/user.html'
    success_url = reverse_lazy('utenti')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuovo cliente'
        return context

class ClienteUpdate(UpdateView):
    queryset = Cliente.objects.all()
    form_class = ClienteForm
    template_name = 'TelegramBot/user.html'
    success_url = reverse_lazy('utenti')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Aggiorna cliente'
        return context

class SubscriptionList(ListView):
    model = Subscription
    template_name = "TelegramBot/subscriptions.html"

class SubscriptionCreate(CreateView):
    form_class = SubscriptionForm
    template_name = 'TelegramBot/subscription.html'
    success_url = reverse_lazy('iscrizioni')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuova iscrizione'
        return context

class SubscriptionUpdate(UpdateView):
    queryset = Subscription.objects.all()
    form_class = SubscriptionForm
    template_name = 'TelegramBot/subscription.html'
    success_url = reverse_lazy('iscrizioni')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Aggiorna iscrizione'
        return context

# Avvio del thread
messageReader = threadTelegramReader(1, "messageReader", 1)
messageReader.start()
