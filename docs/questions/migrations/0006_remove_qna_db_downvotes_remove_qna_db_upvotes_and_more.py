# Generated by Django 5.0.6 on 2024-06-17 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_remove_answer_downvotes_remove_answer_qid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qna_db',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='qna_db',
            name='upvotes',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]