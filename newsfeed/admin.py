from django.contrib import admin
from .models import News
from .models import LogInstance
from .models import LogAction
from .models import AlgoChoice

# Register your models here.

admin.site.register(News)
admin.site.register(LogInstance)
admin.site.register(LogAction)
admin.site.register(AlgoChoice)