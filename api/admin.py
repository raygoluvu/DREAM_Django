from django.contrib import admin
from .models import Thing, Gear, Exercise


# Register your models here.
class GearInline(admin.StackedInline):  # admin.TabularInline
    model = Gear
    extra = 1


class GearAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "token_id",
        "user",
        "level",
        "type",
        "color",
        "work_max",
        "exp",
        "lucky",
        "coupon",
    ]


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["user", "gear", "timestamp", "accuracy"]


class ThingAdmin(admin.ModelAdmin):
    list_display = ["user", "level", "amount"]


admin.site.register(Gear, GearAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Thing, ThingAdmin)
