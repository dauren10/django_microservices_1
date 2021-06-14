from django.http import HttpResponse
from .models import Question
from .tasks import create_random_user_accounts
from time import sleep
from .producer import publish
from .serializers import QuestionSerializer
def index(request):
    total=2
    res=Question.objects.create(question_text='Test1')
    serializer = QuestionSerializer(res)
    print('IT IS A VIEW!!!!!!!!!!!!!!!!!!!!11')
    publish('product.created',serializer.data)
    create_random_user_accounts.delay(total)
    #sleep(10)
    #Question.objects.create(question_text='Test1')
    return HttpResponse("Hello, world. You're at the polls index.")
