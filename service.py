import threading
import time

from send_email import send_email_with_text

TASKS = []
NUMBER_OF_TASKS = 10 
EMAIL_FROM = 'aleksioprime@gmail.com'

def worker(text, email):
    send_email_with_text(text, EMAIL_FROM, email)
    

def add_email(text, timer, email):
    TASKS.append({"text": text, "timer": timer, "email": email})
    t = threading.Timer(timer, worker, args=(text, email, ))
    t.start()

def get_tasks():
    return TASKS[-NUMBER_OF_TASKS:]