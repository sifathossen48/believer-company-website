from django.shortcuts import render
from django.views.generic import TemplateView

from Home_Page.models import Review, TeamMember, Why_Selecting_US, C_Level_Person

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['whyUs'] = Why_Selecting_US.objects.last()
        context['team'] = TeamMember.objects.filter(is_Draft=False).order_by('si')
        context['reviews'] = Review.objects.all()
        return context
class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['whyUs'] = Why_Selecting_US.objects.last()
        context['c_level'] = C_Level_Person.objects.all()
        return context
class CertificationView(TemplateView):
    template_name = 'certification.html'

class StructuralView(TemplateView):
    template_name = 'structural-and-safety-compliance.html'

class TestingView(TemplateView):
    template_name = 'testing-and-inspection.html'

class OtherView(TemplateView):
    template_name = 'others-service.html'