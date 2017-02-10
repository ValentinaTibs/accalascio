from django.contrib import admin
from django import forms
from django.db import models

from tinymce.widgets import TinyMCE
from mce_filebrowser.admin import MCEFilebrowserAdmin
from django.forms import CheckboxSelectMultiple


# Register your models here.
from accalascio.models import  Post, Category, rangeCat, Renting, catRent, roomFac, imgRent, Booking


class PostAdmin(MCEFilebrowserAdmin):
	list_display = ('title','text','cat','active','order')
	can_delete = False

class InlineImage(admin.TabularInline):
    model = imgRent

class RentingAdmin(MCEFilebrowserAdmin):
	list_display = ('title','text','cat','active','order',)
	can_delete = False
	formfield_overrides = { models.ManyToManyField: {'widget': CheckboxSelectMultiple},}
	inlines = [InlineImage]


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)

class BookingAdmin(admin.ModelAdmin):
	list_display = ('start_date','end_date','room','notes','contacts_mail','checkin_time','approved')
	can_save = False
	can_add = False
	can_save = False

class catRentAdmin(admin.ModelAdmin):
	list_display = ('name',)

class rangeCatAdmin(admin.ModelAdmin):
	list_display = ('name','color')

class iconCatAdmin(admin.ModelAdmin):
	list_display = ('name','png')

class roomFacAdmin(admin.ModelAdmin):
	list_display = ('name','png')
	can_save = False
	can_add = False
	can_save = False



admin.site.register(Post, PostAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Renting, RentingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(rangeCat, rangeCatAdmin)
admin.site.register(catRent, catRentAdmin)
admin.site.register(roomFac, roomFacAdmin)



