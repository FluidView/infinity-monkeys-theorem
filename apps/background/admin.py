from django.contrib import admin
from apps.background import models as m

# Register your models here.


admin.site.register(m.basic)
admin.site.register(m.best)
admin.site.register(m.statistic)