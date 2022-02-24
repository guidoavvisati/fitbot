# Fitbot
Tweet and track your fitness results via fitbot

# References Bot
- https://auth0.com/blog/how-to-make-a-twitter-bot-in-python-using-tweepy/
- https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
- https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9
- https://funsizeathlete.medium.com/my-first-twitter-bot-using-python-and-heroku-e3ef83578f58
- https://emcain.github.io/heroku-twitter-bot/

# References Scheduling
- https://pypi.org/project/APScheduler/
- https://charlesreid1.com/wiki/Heroku/APScheduler
- https://devcenter.heroku.com/articles/clock-processes-python
- https://devcenter.heroku.com/articles/scheduled-jobs-custom-clock-processes
- https://aws.amazon.com/premiumsupport/knowledge-center/schedule-elastic-beanstalk-stop-restart/

# Heroku Flow
- Git deployment `git push heroku master`
- Start one-off dyno `heroku ps:scale clock=1`
- Monitoring `heroku logs --tail`
- Stopping the dyno `heroku ps:stop clock`

# Hosting
- https://botwiki.org/resource/tutorial/how-to-make-a-twitter-bot-the-definitive-guide/
- https://botwiki.org/resources/hosting-platforms/
- https://www.therobinlord.com/creating-a-twitter-bot-using-google-cloud-functions/
- https://blog.andyjiang.com/intermediate-cron-jobs-with-heroku