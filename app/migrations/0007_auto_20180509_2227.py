# Generated by Django 2.0 on 2018-05-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_step_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectenv',
            name='description',
        ),
        migrations.AddField(
            model_name='step',
            name='sn',
            field=models.IntegerField(default=1, verbose_name='序号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='access_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='AccessID'),
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='access_key',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='AccessKey'),
        ),
        migrations.AlterField(
            model_name='step',
            name='assertion',
            field=models.TextField(blank=True, null=True, verbose_name='断言'),
        ),
        migrations.AlterField(
            model_name='step',
            name='data',
            field=models.TextField(blank=True, null=True, verbose_name='数据'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='描述'),
        ),
    ]
