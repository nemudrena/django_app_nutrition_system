from django.contrib import admin
from .models import Articles
from .models import Contacts
from .models import Ankets
from .models import Infos

admin.site.register(Articles)
admin.site.register(Contacts)
admin.site.register(Ankets)
admin.site.register(Infos)
