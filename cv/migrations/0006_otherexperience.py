# Generated by Django 3.1.7 on 2021-04-04 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0005_auto_20210401_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('period', models.CharField(max_length=150)),
                ('website', models.CharField(default='', max_length=150)),
                ('company', models.CharField(default='', max_length=150)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
