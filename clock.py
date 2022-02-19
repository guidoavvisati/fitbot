from apscheduler.schedulers.blocking import BlockingScheduler
from tweet_reply import reply_to_tweet

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=3)
def timed_job():
    reply_to_tweet()


sched.start()
