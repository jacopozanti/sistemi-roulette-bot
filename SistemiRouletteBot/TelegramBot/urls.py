from TelegramBot.views import ClienteUpdate, ClienteList, ClienteCreate, SubscriptionUpdate, SubscriptionList, SubscriptionCreate, Home
from django.urls import path

urlpatterns = [
    path('', Home.as_view()),

    path('clienti', ClienteList.as_view(), name="utenti"),
    path('clienti/nuovo', ClienteCreate.as_view(), name="utente_nuovo"),
    path('cliente/<int:pk>/', ClienteUpdate.as_view(), name="utente"),
    
    path('iscrizioni/', SubscriptionList.as_view(), name="iscrizioni"),
    path('iscrizioni/nuovo', SubscriptionCreate.as_view(), name="iscrizione_nuova"),
    path('iscrizione/<int:pk>/', SubscriptionUpdate.as_view(), name="iscrizione"),
]