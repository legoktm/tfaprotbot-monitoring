#!/usr/bin/env python

import datetime
import jinja2
import time
import urllib2
import webapp2

from google.appengine.api import mail

import ago

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


def get_last_run_time():
    url = 'http://tools.wmflabs.org/tfaprotbot/lastrun.txt'
    req = urllib2.urlopen(url)
    data = req.read()
    req.close()
    return float(data)


def send_email(unix):
    message = mail.EmailMessage(
        sender='legoktm@gmail.com',
        to='legoktm@gmail.com',
        subject='TFA Protector Bot is late!',
        body='TFA Protector Bot last ran at %s.' % str(unix),
        html=format_template(unix)
    )
    message.send()


def get_human(now, then):
    return ago.human(now-datetime.datetime.fromtimestamp(then))


def is_late(run_time):
    """
    Return bool if overdue for 24h
    """
    return time.time() > (run_time + (60 * 60 * 24))


def format_template(unix):
    now = datetime.datetime.utcnow()
    human = get_human(now, unix)
    now_fmt = now.strftime('%B %d, %Y at %H:%M')
    template = JINJA_ENVIRONMENT.get_template('index.html')
    return template.render(fmt_time=now_fmt, diff_time=human, unix_time=unix)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        unix = get_last_run_time()
        self.response.write(format_template(unix))


class CronHandler(webapp2.RequestHandler):
    def get(self):
        unix = get_last_run_time()
        if is_late(unix):
            send_email(unix)
            self.response.write('Sent email.')
        else:
            self.response.write('Is ok.')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/cron', CronHandler),
], debug=True)
