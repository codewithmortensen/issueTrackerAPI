# Generated by Django 4.2.7 on 2023-11-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("issue", "0003_developer"),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="developer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="issue.developer",
            ),
        ),
    ]
