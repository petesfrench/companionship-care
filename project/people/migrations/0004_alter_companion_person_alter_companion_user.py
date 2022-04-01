# Generated by Django 4.0.1 on 2022-04-01 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0003_joinrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companion',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companions_through', to='people.person'),
        ),
        migrations.AlterField(
            model_name='companion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companions_through', to=settings.AUTH_USER_MODEL),
        ),
    ]