from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def notification(request):
    form = SubscruberForms(request.POST or None)
    if request.POST and form.is_valid():
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()
    return render(request, 'notification.html', locals())


def userinfo(request):
    form = BandsUsernames(request.POST or None)

    if request.POST and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'userinfo.html', locals())


class BandView(ListView):
    model = Band
    template_name = 'bands.html'

    def get(self, request, *args, **kwargs):
        self.id = request.GET.get('id')

        if self.id:

            self.template_name = "Band.html"
            self.queryset = Band.objects.filter(id=self.id)
        else:
            self.template_name = "bands.html"
        # return render(request, "runs_list.html", locals())
        return super(BandView, self).get(request, *args, **kwargs)


class MainListView(ListView):
    model = Band
    template_name = "main.html"
    queryset = Band.objects.filter(id='3')


def about(request):
    return render(request, 'about.html')


class BandsListView(ListView):
    model = Band
    template_name = "bands.html"
    form_class = BandsForms

    def get(self, request, *args, **kwargs):
        id = request.GET.get('id')
        form = BandsForms(request.POST or None)
        if id:
            queryset = Band.objects.filter(id=id)
            object_list = Band.objects.filter(id=id)
        else:
            object_list = Band.objects.all()
        return render(request, 'bands.html', locals())

    def post(self, request):
        object_list = Band.objects.all()
        form = BandsForms(request.POST or None, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_form = form.save()
        return render(request, 'bands.html', locals())


class ConcertAgencyListView(ListView):
    model = ConcertAgency
    template_name = "concert_agency.html"
    form_class = ConcertAgencyForms

    def get(self, request, *args, **kwargs):
        form = ConcertAgencyForms(request.POST or None)
        object_list = ConcertAgency.objects.all()
        return render(request, 'concert_agency.html', locals())

    def post(self, request):
        object_list = ConcertAgency.objects.all()
        form = ConcertAgencyForms(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            new_form = form.save()
        return render(request, 'concert_agency.html', locals())


class Registration(FormView):
    form_class = RegistrationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = 'authorization/'

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(Registration, self).form_valid(form)


def registration2(request):
    errors = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'

        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'

        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'

        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'

        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'

        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not errors:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=surname)
            return HttpResponseRedirect(reverse('authorization'))

    return render(request, 'reg2.html', locals())


class Authorization(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "authorization.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(Authorization, self).form_valid(form)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')
