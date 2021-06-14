from celery import Celery

app = Celery('hello', broker='amqp://guest:guest@localhost//')

@app.task
def hello():
    print(1)
    return 'hello world'