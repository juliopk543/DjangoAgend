from django.shortcuts import render
from .models import contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

def index(request):
    contatos = contato.objects.order_by('nome').filter(
        mostrar = True
    )
    paginator = Paginator(contatos, 1)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos' : contatos
    })

def ver_contato(request,contato_id):
    try:
        v_contato = contato.objects.get(id = contato_id)

        if not v_contato.mostrar:
            raise Http404()
        return render(request, 'contatos/ver_contato.html', {
            'contato' : v_contato
        })
    except contato.DoesNotExist as c:
        raise Http404()


def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404()

    campos = Concat('nome',Value(' '),'sobrenome')

    contatos = contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 1)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
