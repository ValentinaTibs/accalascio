from django import forms
from datetime import datetime

from django.forms import ModelForm
from django.db.models import Count
from django.contrib.admin.widgets import AdminDateWidget 
from django.contrib.auth.models import User
from django.forms.fields import DateField

from accalascio.models import Booking

class BookingForm(ModelForm):
	
    class Meta:
        model = Booking
        fields = ('start_date','end_date','notes','contacts_mail','checkin_time')
        widgets = { 'start_date' : forms.DateInput(attrs={'class':'datepicker', 'id':'start_date'}), 
                    'end_date' : forms.DateInput(attrs={'class':'datepicker', 'id':'end_date'}),
                    }
		
       