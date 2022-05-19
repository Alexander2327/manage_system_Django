from django.contrib import admin
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'modification', 'con_type', 'create_date', 'order')
    list_display_links = ('serial_num',)
    search_fields = ('serial_num', 'create_date')


admin.site.register(Products, ProductsAdmin)


class ModificationsAdmin(admin.ModelAdmin):
    list_display = ('mod',)
    list_display_links = ('mod',)


admin.site.register(Modifications, ModificationsAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order',)
    list_display_links = ('order',)


admin.site.register(Orders, OrdersAdmin)


class OSAAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'gain', 'gain_flatness', 'noise_figure')
    list_display_links = ('serial_num',)
    search_fields = ('serial_num',)


admin.site.register(OSA, OSAAdmin)


class TechnicalsAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'i_op', 'i_eol', 'p_op', 'p_eol', 'attenuation')
    list_display_links = ('serial_num',)
    search_fields = ('serial_num',)


admin.site.register(Technicals, TechnicalsAdmin)


class ConnectorsAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)


admin.site.register(Connectors, ConnectorsAdmin)


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'laser', 'passtopt')
    list_display_links = ('serial_num',)
    search_fields = ('serial_num',)


admin.site.register(Documents, DocumentsAdmin)


class ReqAdmin(admin.ModelAdmin):
    list_display = ('count', 'count_m12', 'count_n19', 'con_type', 'req_date', 'end_of_date', 'order', 'explanations', 'status')
    list_display_links = ('req_date',)
    search_fields = ('req_date', 'end_of_date')


admin.site.register(Request, ReqAdmin)