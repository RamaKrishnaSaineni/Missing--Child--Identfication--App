from django.contrib import admin
from .models import Child, Report

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'last_seen', 'location', 'status')
    search_fields = ('name', 'status', 'location')
    list_filter = ('gender', 'status', 'last_seen')
    ordering = ('-last_seen',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'child', 'reporter_name', 'reporter_contact', 'report_date')
    search_fields = ('child__name', 'reporter_name', 'reporter_contact')
    list_filter = ('report_date',)
    ordering = ('-report_date',)