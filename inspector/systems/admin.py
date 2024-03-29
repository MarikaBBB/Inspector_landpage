from django import forms
from django.contrib import admin

from .models import DbTable, Environment, Instance, System


class SystemAdminForm(forms.ModelForm):
    class Meta:
        model = System
        fields = "__all__"


class SystemAdmin(admin.ModelAdmin):
    form = SystemAdminForm
    list_display = ["name", "application"]
    readonly_fields = ["name", "application"]


admin.site.register(System, SystemAdmin)


class EnvironmentAdminForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = "__all__"


class EnvironmentAdmin(admin.ModelAdmin):
    form = EnvironmentAdminForm
    list_display = ["name"]
    readonly_fields = ["name"]


admin.site.register(Environment, EnvironmentAdmin)


class InstanceAdminForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = "__all__"


class InstanceAdmin(admin.ModelAdmin):
    form = InstanceAdminForm
    list_display = ["host", "port", "db", "schema", "login", "password", "extra_json"]
    readonly_fields = [
        "host",
        "port",
        "db",
        "schema",
        "login",
        "password",
        "extra_json",
    ]


admin.site.register(Instance, InstanceAdmin)


class DbTableAdminForm(forms.ModelForm):
    class Meta:
        model = DbTable
        fields = "__all__"


class DbTableAdmin(admin.ModelAdmin):
    form = DbTableAdminForm
    list_display = ["name"]
    readonly_fields = ["name"]


admin.site.register(DbTable, DbTableAdmin)
