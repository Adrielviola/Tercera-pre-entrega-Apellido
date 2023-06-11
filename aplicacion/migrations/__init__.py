from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notebook',
            fields=[
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='aio',
            fields=[
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='dektop',
            fields=[
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='celulares',
            fields=[
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('imei', models.DecimalField(max_digits=20, decimal_places=0)),
            ],
        ),
    ]