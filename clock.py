from apscheduler.schedulers.blocking import BlockingScheduler
from tweet_reply import reply_to_tweet

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=3)
def timed_job():
    reply_to_tweet()


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched.start()