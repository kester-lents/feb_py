# Generated by Django 2.2.4 on 2020-03-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text_long',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
