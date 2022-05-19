from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView, CreateView, ListView
from .forms import ProductForm, OSAForm, TechnicalForm, DocumentsForm, UserRegisterForm, UserLoginForm, \
    ModificationForm, OrderForm, ConnectorForm, ContactForm, ReqForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.contrib.auth.models import User


@login_required(login_url='login')
def mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                'name': form.cleaned_data['name'],
                'content': form.cleaned_data['content'],
                'contact': form.cleaned_data['contact'],
            }
            message = '\n'.join(body.values())
            mail = send_mail(form.cleaned_data['subject'], message,
                             'danilov.aa1@mail.ru', ['danilov.aa1@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо успешно отправленно!')
                return redirect('mail')
            else:
                messages.error(request, 'Ошибка отправки!')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = ContactForm()
    data = {
        'form': form,
    }
    return render(request, 'mainapp/mail.html', data)


@user_passes_test(lambda u: u.is_staff, login_url='home')
@login_required(login_url='login')
def request_list_all(request):
    uncheck = request.GET.get('uncheck')
    check = request.GET.get('check')
    search_query = request.GET.get('search')
    if search_query:
        requests = Request.objects.filter(req_date=search_query)
    elif uncheck:
        requests = Request.objects.filter(status=False)
    elif check:
        requests = Request.objects.order_by('-req_date')
    else:
        requests = Request.objects.order_by('-req_date')

    paginator = Paginator(requests, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'req': requests,
        'page_obj': page_obj,
    }

    return render(request, 'mainapp/req_list_all.html', data)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    data = {
        'form': form,
    }
    return render(request, 'mainapp/register.html', data)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                login(request, user)
                return redirect('home')
            # else:
            # Сообщение что не активный пользователь
    else:
        form = UserLoginForm()
    return render(request, 'mainapp/login.html', {'form': form})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')


@user_passes_test(lambda u: u.is_staff, login_url='home')
@login_required(login_url='login')
def users(request):
    search_query = request.GET.get('search')
    if search_query:
        user = User.objects.filter(last_name=search_query)
    else:
        user = User.objects.order_by('-username')
    paginator = Paginator(user, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'user1': user,
        'page_obj': page_obj,
    }

    return render(request, 'mainapp/usertable.html', data)


@login_required(login_url='login')
def main_table(request):
    search_query = request.GET.get('search')
    if search_query:
        products = Products.objects.filter(serial_num=search_query)
    else:
        products = Products.objects.order_by('-serial_num')

    paginator = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'prod': products,
        'page_obj': page_obj,
    }

    return render(request, 'mainapp/maintable.html', data)


@login_required(login_url='login')
def table_osa(request):
    search_query = request.GET.get('search')
    if search_query:
        spect = OSA.objects.filter(serial_num=search_query)
    else:
        spect = OSA.objects.order_by('-serial_num')
    paginator = Paginator(spect, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'spect': spect,
        'page_obj': page_obj,
    }
    return render(request, 'mainapp/osatable.html', data)


@login_required(login_url='login')
def table_doc(request):
    search_query = request.GET.get('search')
    if search_query:
        doc = Documents.objects.filter(serial_num=search_query)
    else:
        doc = Documents.objects.order_by('-serial_num')
    paginator = Paginator(doc, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'doc': doc,
        'page_obj': page_obj,
    }
    return render(request, 'mainapp/doctable.html', data)


@login_required(login_url='login')
def table_tech(request):
    search_query = request.GET.get('search')
    if search_query:
        tech = Technicals.objects.filter(serial_num=search_query)
    else:
        tech = Technicals.objects.order_by('-serial_num')
    paginator = Paginator(tech, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'tech': tech,
        'page_obj': page_obj,
    }
    return render(request, 'mainapp/techtable.html', data)


def start(request):
    data = {
    }
    return render(request, 'mainapp/start.html', data)


# @staff_member_required(login_url='login')
@login_required(login_url='login')
def home(request):
    product_count = Products.objects.count()
    user_count = User.objects.filter(is_active=False).count()
    req_count = Request.objects.filter(status=False).count()
    data = {
        'product_count': product_count,
        'user_count': user_count,
        'req_count': req_count,
    }
    return render(request, 'mainapp/home.html', data)


class AddProduct(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff is True

    # permission_required = 'is_staff'
    form_class = ProductForm
    template_name = 'mainapp/add_main.html'
    success_message = "Изделие успешно добавлено!"


class AddOSA(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff is True

    form_class = OSAForm
    template_name = 'mainapp/add_osa.html'
    success_message = "Результаты анализа успешно добавлены!"


class AddTechnical(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff is True

    form_class = TechnicalForm
    template_name = 'mainapp/add_tech.html'
    success_message = "Технические характеристики успешно добавлены!"


class AddDocs(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff is True

    form_class = DocumentsForm
    template_name = 'mainapp/add_doc.html'
    success_message = "Документы успешно добавлены!"


class AddModification(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff is True

    form_class = ModificationForm
    template_name = 'mainapp/mod.html'
    success_message = "Модификация успешно добавлена!"


class AddOrder(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff is True

    form_class = OrderForm
    template_name = 'mainapp/order.html'
    success_message = "Номер заказа успешно добавлен!"


class AddConnector(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff is True

    form_class = ConnectorForm
    template_name = 'mainapp/connector.html'
    success_message = "Тип коннекторов успешно добавлен!"


class AddReq(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = 'login'
    form_class = ReqForm
    template_name = 'mainapp/request.html'
    success_message = "Заказ успешно добавлен!"
