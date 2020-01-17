from django.contrib import admin
from libadmin.models import notice, book_info, lib_admin
# Register your models here.
admin.site.register(book_info)
admin.site.register(lib_admin)
admin.site.register(notice)
