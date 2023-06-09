# Generated by Django 4.2 on 2023-04-21 08:48

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0003_like"),
    ]

    operations = [
        migrations.RenameField(
            model_name="like",
            old_name="author",
            new_name="account",
        ),
        migrations.AddField(
            model_name="like",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("account", "post")},
        ),
    ]
