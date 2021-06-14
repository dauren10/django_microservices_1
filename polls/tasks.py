import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .models import Question
from celery import shared_task
from time import sleep
@shared_task
def create_random_user_accounts(total):
    print('IT IS A TASK!!!!!!!!!!!!!!!!!!!!11')
    print('START TASK')
    for i in range(total):
        print('create')
        sleep(10)
        res=Question.objects.create(question_text='Test1')
        if res:
            print('YES')
        else:
            print('NO!!!!!!!!!!!!!!')
    return '{} random users created with success!'.format(total)