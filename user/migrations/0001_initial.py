# Generated by Django 3.2.8 on 2022-03-13 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('note', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('READ_ONLY', 'READ_ONLY'), ('EDITOR', 'EDITOR')], max_length=10)),
                ('collaborators', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('notes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collaborations', to='note.note')),
            ],
            options={
                'unique_together': {('notes', 'collaborators')},
            },
        ),
    ]
