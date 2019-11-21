# Generated by Django 2.2.7 on 2019-11-19 04:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoadmapParent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('overview', models.CharField(max_length=200, verbose_name='概要')),
                ('like', models.IntegerField(default=0, verbose_name='いいね数')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'roadmap_parent',
            },
        ),
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('detail', models.CharField(default='', max_length=200, verbose_name='詳細')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('next_id', models.UUIDField(default=uuid.uuid4, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadmap.RoadmapParent', verbose_name='親ロードマップ')),
            ],
            options={
                'db_table': 'roadmap',
            },
        ),
    ]
