from django.shortcuts import render
from django.http import HttpResponse
from .forms import formularioCadastro, formularioCadastroModel

# Create your views here.

#Criando formulário direto no html
def home(request):
    return HttpResponse('teste')

def formulariohtml(request):
    return render(request, 'formHtml.html')

def processa_formulario_html(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    return HttpResponse(f"{nome} {email}")


#Criando formulário usando o Forms
def formularioforms(request):
    form = formularioCadastro()
    return render(request, 'formForms.html', {'form': form})

def processa_formulario_forms(request):
    form = formularioCadastro(request.POST)
    if form.is_valid():
        nome = form.data['nome']
        email = form.data['email']
        return HttpResponse(f"{nome} {email} forms")
    return HttpResponse('Erro interno!')


#Criando formulário usando o Model.
def formularioModels(request):
    form = formularioCadastroModel()
    return render(request, 'formModels.html', {'form': form})

def processa_formulario_model(request):
    form = formularioCadastroModel(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse(f"Salvo com sucesso")
    return HttpResponse('Erro interno!')