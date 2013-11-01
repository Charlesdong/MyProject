# -*- coding: utf-8 -*-

from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.add_interval_job(sign_in.sign_count_charge, seconds=10)
#sched.start()
