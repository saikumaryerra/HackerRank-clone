# Generated by Django 2.2.3 on 2019-07-24 02:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20190723_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewlist',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 8, 1, 34, 846463)),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2019, 7, 24, 8, 1, 34, 848552))),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.InterviewList')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('output', models.TextField()),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.InterviewList')),
            ],
        ),
    ]