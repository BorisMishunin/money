from django.contrib import admin
from fop.models import Fops, Payments, Taxe_Payments, Taxes

admin.site.register(Fops)
admin.site.register(Payments)
admin.site.register(Taxe_Payments)
admin.site.register(Taxes)
# Register your models here.
