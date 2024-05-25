from django.contrib import admin
from app.models import Produto
from app.models import Relacao
from app.models import Nivel
from app.models import Usuario

# Register your models here.
admin.site.register(Produto)
admin.site.register(Relacao)
admin.site.register(Usuario)
admin.site.register(Nivel)