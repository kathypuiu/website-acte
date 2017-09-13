from django.apps import AppConfig
from watson import search as watson
from .models import Document, Institution

class ActeConfig(AppConfig):
    name = 'acte'
    def ready(self):
        YourModel = self.get_model("Document")
        watson.register(Document)
