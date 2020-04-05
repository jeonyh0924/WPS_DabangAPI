from django.contrib import admin

# Register your models here.
from posts.models import SalesForm, ControlPoint, PostAddress, SecuritySafetyFacilities, PostRoom, OptionItem


class PostRoomAdmin(admin.ModelAdmin):
    list_display = ['pk']


class SalesFormAdmin(admin.ModelAdmin):
    list_display = ['pk', 'type', 'deposit', 'monthly', 'PriceText']


class ControlPointAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class PostAddressAdmin(admin.ModelAdmin):
    list_display = ['pk', 'loadAddress']


class SecuritySafetyFacilitiesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class OptionItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', ]


admin.site.register(PostRoom, PostRoomAdmin)
admin.site.register(SalesForm, SalesFormAdmin)
admin.site.register(ControlPoint, ControlPointAdmin)
admin.site.register(PostAddress, PostAddressAdmin)
admin.site.register(SecuritySafetyFacilities, SecuritySafetyFacilitiesAdmin)
admin.site.register(OptionItem, OptionItemAdmin)