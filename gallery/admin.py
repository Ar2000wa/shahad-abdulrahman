from django.contrib import admin
#from .models import Gallery
from . models import Beauty
from . models import Fashion
from . models import Weddings
# Register your models here.
#admin.site.register(Gallery)
admin.site.register(Beauty)
admin.site.register(Fashion)
admin.site.register(Weddings)