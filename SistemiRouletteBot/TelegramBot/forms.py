from django.db import models
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import DateInput
from TelegramBot.models import Cliente, Subscription

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        menu = ModelChoiceField(queryset=Cliente.objects.all())
        fields = '__all__'
        widgets = {
            'inizio': DateInput(attrs={'type': 'date'}),
            'scadenza': DateInput(attrs={'type': 'date'}),
        }