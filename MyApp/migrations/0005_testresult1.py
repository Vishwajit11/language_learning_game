# Generated by Django 4.2.2 on 2023-12-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_testresult_remove_useranswers_user_delete_testscore_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username1', models.CharField(max_length=255)),
                ('testname1', models.CharField(max_length=255)),
                ('result1', models.IntegerField()),
            ],
        ),
    ]
