from django.contrib import admin
from smart_selects.db_fields import ChainedForeignKey

from.models import *

admin.site.register(Voluntirio)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Cidade2)


