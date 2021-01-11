from django.contrib import admin
from .models import News
from .models import Configuration
from .models import LogInstance
from .models import LogAction

# Register your models here.

admin.site.register(News)
admin.site.register(Configuration)
admin.site.register(LogInstance)
admin.site.register(LogAction)
