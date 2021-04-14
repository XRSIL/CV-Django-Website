from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import ResumeJob, ResumeEducation, OtherExperience
from .forms import ContactForm
from django.shortcuts import redirect


def home(request):
    return render(request, 'cv/home.html', {'title': 'Обо мне'})


class ResumeView(TemplateView):
    template_name = 'cv/resume.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['jobs'] = ResumeJob.objects.all()
        context['education'] = ResumeEducation.objects.all()
        context['internships'] = OtherExperience.objects.all()
        context['title'] = 'Резюме'
        return context


class ContactView(FormView):
    template_name = 'cv/contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.result()
        return redirect('cv-contacts')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context
