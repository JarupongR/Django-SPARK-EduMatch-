# Generated by Django 3.0.2 on 2020-02-16 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matched_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Selected_Subject',
        ),
        migrations.AddField(
            model_name='tutor',
            name='city',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='tutor',
            name='gender',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='tutor',
            name='groupMatch',
            field=models.ManyToManyField(blank=True, to='edu.Tutor'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='isMatched',
            field=models.TextField(blank=True, default='False'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='expert',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='name',
            field=models.TextField(blank=True, default=''),
        ),
    ]