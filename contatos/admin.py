from django.contrib import admin
from .models import categoria, contato

class contatoadmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome','telefone','email','categoria','mostrar')
    list_display_links = ('nome','sobrenome')
    #list_filter = ('nome','telefone')
    list_per_page = 3
    search_fields = ('nome','sobrenome')
    list_editable = ('telefone','mostrar')

admin.site.register(categoria)
admin.site.register(contato,contatoadmin)

