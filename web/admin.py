from django.contrib import admin
from web.models import *

# Register your models here.

admin.site.register(Goods)
admin.site.register(Payments)
admin.site.register(PaymentsTranscript)
admin.site.register(PaymentsType)