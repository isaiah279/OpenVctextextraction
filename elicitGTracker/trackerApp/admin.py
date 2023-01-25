from django.contrib import admin
# from.models import OilMessage
from.models import OilModel
from .models import*
# Register your models here.
admin.site.register(OilModel)
# admin.site.register(OilMessage)
admin.site.register(DrugsModels)
admin.site.register(AerosalModels)
admin.site.register(SoaplModels)
admin.site.register(BreadModels)
