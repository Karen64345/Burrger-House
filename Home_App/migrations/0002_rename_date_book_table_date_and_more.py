# Generated by Django 5.1 on 2024-10-08 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_table',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='book_table',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='book_table',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='book_table',
            old_name='Person',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='book_table',
            old_name='Phone_Number',
            new_name='phone_number',
        ),
    ]