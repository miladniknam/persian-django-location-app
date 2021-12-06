from django.contrib import admin
from location.models import Country, Province, City
from django.utils.html import mark_safe

###################################################
#                                                 #
#                                                 #
#          This is my CountryAdminModel           #
#                                                 #
#                                                 #
###################################################


# This is admin model manager for country model
class CountryAdminModel(admin.ModelAdmin):
    list_display = ('show_image', 'name', 'provinces_count')
    fields = ('name', 'image')

    def provinces_count(self, obj):
        return obj.provinces.all().count()

    def show_image(self, obj):
        return mark_safe('<img src="%s" width="50" height="50" />' % (obj.image.url))

    provinces_count.short_description = 'تعداد استان ها'
    show_image.short_description = 'تصویر شاخص کشور'
    show_image.allow_tags = True


###################################################
#                                                 #
#                                                 #
#          This is my ProvinceAdminModel          #
#                                                 #
#                                                 #
###################################################


# This is admin model manager for province model
class ProvinceAdminModel(admin.ModelAdmin):
    list_display = ('show_image', 'name',  'country', 'cities_count')
    fields = ('name', 'image', 'country')
    list_filter = ('country__name',)

    def cities_count(self, obj):
        return obj.cities.all().count()

    def show_image(self, obj):
        return mark_safe('<img src="%s" width="50" height="50" />' % (obj.image.url))

    cities_count.short_description = 'تعداد شهر ها'
    show_image.short_description = 'تصویر شاخص استان'
    show_image.allow_tags = True


###################################################
#                                                 #
#                                                 #
#           This is my CityAdminModel             #
#                                                 #
#                                                 #
###################################################


# This is admin model manager for city model
class CityAdminModel(admin.ModelAdmin):
    list_display = ('show_image', 'name', 'province')
    fields = ('name', 'image', 'province')
    list_filter = ('province__name',)

    def show_image(self, obj):
        return mark_safe('<img src="%s" width="50" height="50" />' % (obj.image.url))

    show_image.short_description = 'تصویر شاخص شهر'
    show_image.allow_tags = True


###################################################
###################################################
###################################################
######## This is my registraion of models #########
###################################################
###################################################
###################################################


# This is place for register location models
admin.site.register(Country, CountryAdminModel)
admin.site.register(Province, ProvinceAdminModel)
admin.site.register(City, CityAdminModel)