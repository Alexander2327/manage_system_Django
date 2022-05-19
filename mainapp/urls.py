from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('registester', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('main_table', main_table, name='main'),
    path('table/osa', table_osa, name='osa'),
    path('table/documentation', table_doc, name='doc'),
    path('table/technicals', table_tech, name='tech'),
    path('', start, name='start'),
    path('home', home, name='home'),
    path('users', users, name='users'),
    path('mail', mail, name='mail'),
    path('table/add', AddProduct.as_view(), name='add_product'),
    path('table/osa/add', AddOSA.as_view(), name='add_osa'),
    path('table/technicals/add', AddTechnical.as_view(), name='add_tech'),
    path('table/documents/add', AddDocs.as_view(), name='add_doc'),
    path('table/add/modification', AddModification.as_view(), name='add_mod'),
    path('table/add/connector', AddConnector.as_view(), name='add_con'),
    path('table/add/order', AddOrder.as_view(), name='add_ord'),
    path('request', AddReq.as_view(), name='add_req'),
    path('request_list_all', request_list_all, name='req_list_all'),
]
