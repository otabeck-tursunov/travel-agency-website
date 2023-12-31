# Generated by Django 4.2.3 on 2023-07-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_service_about_en_service_about_ru_service_about_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='about_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='about_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='about_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='city_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='city_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='city_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='country_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='country_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='country_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='full_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='full_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='full_name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='about_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='about_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='about_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='about_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='about_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='about_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='location_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='location_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='location_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
