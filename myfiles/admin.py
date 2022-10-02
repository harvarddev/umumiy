from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminMurojat(admin.ModelAdmin):
    list_display = ['id','ism','email','murojat','vaqt']
admin.site.register(murojaat,AdminMurojat)


class AdminMobiles(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','rasm5','rasm5','rasm6','rasm7','rasm8','narxi','chegirma','vaqt']
admin.site.register(Mobiles,AdminMobiles)

class AdminAudio(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','rasm5','rasm5','rasm6','rasm7','rasm8','narxi','chegirma','vaqt']
admin.site.register(Audioss,AdminAudio)

class AdminComp(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Computers,AdminComp)

class AdminHH(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Household,AdminHH)

class AdminKitch(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Kitchen,AdminKitch)

class AdmiNew(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Newproducts,AdmiNew)

class AdminHead(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Headphone,AdminHead)

class Adminmr3(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(mr3,Adminmr3)

class AdminLaptop(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Laptop,AdminLaptop)

class AdminWear(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Wearable,AdminWear)

class AdminTv(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Tv,AdminTv)

class AdminCamera(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Camera,AdminCamera)

class AdminGrinder(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Grinder,AdminGrinder)

class AdmintTeg(admin.ModelAdmin):
    list_display = ['id','model','malumot','rasm1','rasm2','rasm3','rasm4','narxi','chegirma','vaqt']
admin.site.register(Tegishli,AdmintTeg)