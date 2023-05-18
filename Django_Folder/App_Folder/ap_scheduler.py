from datetime import datetime,date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Account

def periodic_execution():
    data = Account.objects.get
    data.status = False
    Account.save()
    
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution, 'cron', hour=7, minute=46)
    scheduler.start()