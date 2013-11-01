# -*- coding: utf-8 -*-
from django.db import models


class BlogArticle(models.Model):
    title = models.CharField('文章标题', max_length=300, null=True, blank=True)
    content = models.TextField('文章内容', null=True, blank=True)
    out_url = models.CharField('转自url', max_length=300, null=True, blank=True)
    author = models.CharField('作者', max_length=30, null=True, blank=True, default='watcher')
    count = models.IntegerField('查看次数', default=0, blank=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)

    @property
    def __unicode__(self):
        return self.title

    class Meta:
        def __init__(self):
            pass
        db_table = u'blogarticle'



#from apscheduler.scheduler import Scheduler
#
#sched = Scheduler()
#sched.add_interval_job(sign_in.sign_count_charge, seconds=10)
#sched.start()
