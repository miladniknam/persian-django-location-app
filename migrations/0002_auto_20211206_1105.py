# Generated by Django 3.2.9 on 2021-12-06 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='location.province', verbose_name='استان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='province',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='location.country', verbose_name='کشور'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='تصویر شاخص شهر'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=60, verbose_name='نام شهر'),
        ),
        migrations.AlterField(
            model_name='country',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='تصویر شاخص کشور'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=60, verbose_name='نام کشور'),
        ),
        migrations.AlterField(
            model_name='province',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='تصویر شاخص استان'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=60, verbose_name='نام استان'),
        ),
    ]