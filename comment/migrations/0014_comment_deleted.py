# Generated by Django 3.2 on 2021-05-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0013_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
