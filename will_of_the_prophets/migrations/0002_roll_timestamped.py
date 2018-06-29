# Generated by Django 2.0.6 on 2018-06-29 08:47

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import will_of_the_prophets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('will_of_the_prophets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='roll',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='roll',
            name='embargo',
            field=models.DateTimeField(validators=[will_of_the_prophets.validators.future_validator, will_of_the_prophets.validators.RollEmbargoValidator()]),
        ),
    ]
