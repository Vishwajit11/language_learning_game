# Generated by Django 4.2.2 on 2023-12-21 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApp', '0002_testscore_delete_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscore',
            name='test_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testscore',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=1)),
                ('q2', models.CharField(max_length=1)),
                ('q3', models.CharField(max_length=1)),
                ('q4', models.CharField(max_length=1)),
                ('q5', models.CharField(max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
