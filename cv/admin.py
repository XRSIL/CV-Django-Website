from django.contrib import admin
from .models import ResumeJob, ResumeEducation, OtherExperience

admin.site.register(ResumeJob)
admin.site.register(ResumeEducation)
admin.site.register(OtherExperience)
