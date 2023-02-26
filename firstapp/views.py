
from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse
from .models import Person
from django.forms import UserForm
from django import forms
# from .import forms  не работает


class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(label="Возраст")


def index_app1(request):
    userform = UserForm()
    return render(request, 'firstapp/index_app1.html',
                  {"form": userform})
#
#
# def about(request):
#     return HttpResponse("<h2>О сайте </h2>")
#
#
# def contact(request):
#     return HttpResponse("<h2>контакты </h2>")
#
#
# def products(request, productid):
#     category = request.GET.get("cat"," ")
#     output = "<h2> Продукт № {0} категория {1} </h2>". format(productid,category)
#     return HttpResponse(output)
#
#
# def users(request):
#     id = request.GET.get("id", 1)
#     name = request.GET.get("name", "Maxim")
#     output = "<h2> Пользователь </h2>" \
#              "<h3>id: {0}  имя: {1} </h3>". format(id, name)
#     return HttpResponse(output)


# def index(request):
#     return HttpResponse("Index")


def about(request):
     return HttpResponse("About")


def contact(request):
     return HttpResponseRedirect("/about")


def details(request):
     return HttpResponsePermanentRedirect("/")


def index(request):
    return render(request, "index.html")

# передача данных в шаблоны
# def index(request):
#     # return render(request, "firstapp/home.html")
#     data = {'header': "передача парвметров в шаблон Django",
#            'message':
#            "загружен шаблон templates/firstapp/index_app1" }
#     return render(request, 'firstapp/index_app1.html', context=data)


# def index(request):
#     header = "Person data"
#     langs = ['english', 'french', 'deutsch']
#     users = {'name': "maxim", "age": 30}
#     addr = ('grape', 23, 45)
#     data = {'header': header, 'langs': langs, 'users': users,  'address': addr}
#     # return render(request, "index.html", context=data)     идентич но
#     return TemplateResponse(request, 'index.html', data)


# def index(request):
#     return render(request, 'firstapp/index.html')


# def index(request):
#     data={"age": 60}
#     return render(request,  'firstapp/index.html', context=data)


# def index(request):
#     cat = ["Notebook", "phone", "printer", "scaner", "wires"]
#     return render(request,  'firstapp/index.html', context={"cat": cat})


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        output = "<h2> Пользователь</h2><h3> Имя -{0}, Возраст -{1}</h3>". format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()



# получение данных из БД и загрузка index.html
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

# сохранени
def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")


# изменение

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person" : person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден </h2>")

# удаление


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден </h2>")
