from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'survey.html')
        
class Success(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html')
