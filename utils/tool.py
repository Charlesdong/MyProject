# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.template import loader
from MyProject.settings import EMAIL_FROM_EMAIL


def send_html_mail(subject, params, to_email):
    template_path = 'mail_template.html'

    html_content = loader.render_to_string(
        template_path,  # 需要渲染的html模板
        {
            'params': params  # 参数
        }
    )
    msg = send_mail(subject, html_content, EMAIL_FROM_EMAIL, to_email)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

