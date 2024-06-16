# Generated by Django 5.0.6 on 2024-06-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_alter_choice_id_alter_course_id_alter_enrollment_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]