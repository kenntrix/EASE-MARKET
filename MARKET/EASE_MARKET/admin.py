from django.contrib import admin
from .models import Client, Goods_detail, Seller, ContactUs

import xlwt
from django.http import HttpResponse


# Download function for Excel files
def download(queryset, filename, columns):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Data')

    row_num = 0

    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)

    for obj in queryset:
        row_num += 1
        row = [getattr(obj, field_name) for field_name in columns]
        for col_num, cell_value in enumerate(row):
            ws.write(row_num, col_num, cell_value)

    wb.save(response)
    return response


# Actions for downloading data in Excel format
def download_clients_list(modeladmin, request, queryset):
    columns = ('first_name', 'last_name', 'birth_date', 'email', 'address', 'phone_number')
    return download(queryset, filename='clients_list', columns=columns)


def download_goods_list(modeladmin, request, queryset):
    columns = ('name', 'category', 'price', 'description', 'model', 'brand', 'color')
    return download(queryset, filename='goods_list', columns=columns)


def download_sellers_list(modeladmin, request, queryset):
    columns = ('first_name', 'last_name', 'id_number', 'current_location', 'birth_date', 'email', 'address', 'phone_number')
    return download(queryset, filename='sellers_list', columns=columns)


# Register your models here.
admin.site.site_header = 'EASE_MARKET'

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'subject', 'message')
    list_per_page = 30
    list_filter = ('username', 'email')


class ClientAdmin(admin.ModelAdmin):
    site_header = 'USER ADMIN'
    list_display = ('first_name', 'last_name', 'birth_date', 'email', 'address', 'phone_no')
    list_display_links = ['first_name']
    list_editable = ('last_name', 'birth_date', 'email', 'address', 'phone_no')
    list_filter = ['first_name']
    search_fields = ('first_name', 'last_name')
    actions = [download_clients_list]
    list_per_page = 30


class GoodsAdmin(admin.ModelAdmin):
    site_header = 'Goods Details'
    list_display = ('item', 'category', 'price', 'description', 'model', 'brand', 'color')
    list_display_links = ['item']
    list_editable = ('category', 'price', 'description', 'model', 'brand', 'color')
    list_filter = ['category']
    search_fields = ('item', 'category', 'price')
    actions = [download_goods_list]
    list_per_page = 30


class SellerAdmin(admin.ModelAdmin):
    list_display = ('username', 'id_number', 'current_location', 'price', 'email', 'address', 'phone_no')
    list_display_links = ['username']
    list_editable = ('id_number', 'current_location', 'price', 'email', 'address', 'phone_no')
    list_filter = ('username', 'email')
    list_per_page = 30
    search_fields = ('first_name', 'last_name')
    actions = [download_sellers_list]


admin.site.register(Client, ClientAdmin)
admin.site.register(Goods_detail,GoodsAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
