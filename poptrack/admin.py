from django.contrib import admin

from poptrack.models import Pop, Column, Filling, Stocking, PopColumnRelation

admin.site.register(Pop)
admin.site.register(Column)
admin.site.register(Filling)
admin.site.register(Stocking)
admin.site.register(PopColumnRelation)

