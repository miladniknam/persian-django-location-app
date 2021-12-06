from django.db import models

###################################################
#                                                 #
#                                                 #
#           This is my country model              #
#                                                 #
#                                                 #
###################################################


# This is my country model
class Country(models.Model):
    name = models.CharField(max_length=60, verbose_name='نام کشور')
    image = models.ImageField(upload_to='location/country',null=True, blank=True,
                              verbose_name='تصویر شاخص کشور')

    # This is place for META class
    class Meta:
        verbose_name = "کشور"
        verbose_name_plural = "کشور ها"

    # This is place for set display title of model
    def __str__(self):
        return self.name


###################################################
#                                                 #
#                                                 #
#           This is my province model             #
#                                                 #
#                                                 #
###################################################


# This is my province model
class Province(models.Model):
    name = models.CharField(max_length=60, verbose_name='نام استان')
    image = models.ImageField(upload_to='location/province',null=True, blank=True,
                              verbose_name='تصویر شاخص استان')

    # This is place for put foreign key models
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name='کشور',related_name='provinces')

    # This is place for META class
    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان ها"

    # This is place for set display title of model
    def __str__(self):
        return self.name


###################################################
#                                                 #
#                                                 #
#             This is my city model               #
#                                                 #
#                                                 #
###################################################


# This is my city model
class City(models.Model):
    name = models.CharField(max_length=60, verbose_name='نام شهر')
    image = models.ImageField(upload_to='location/city',null=True, blank=True,
                              verbose_name='تصویر شاخص شهر')

    # This is place for put foreign key models
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, verbose_name='استان',related_name='cities')

    # This is place for META class
    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"

    # This is place for set display title of model
    def __str__(self):
        return self.name
