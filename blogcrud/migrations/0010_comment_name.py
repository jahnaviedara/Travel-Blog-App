# Generated by Django 4.0.5 on 2022-08-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcrud', '0009_rename_body_comment_comment_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='user', max_length=255),
        ),
    ]