#coding=utf-8
DEBUG = True 
#import sae.const


MYSQL_DB = 'myproject'      # 数据库名
MYSQL_USER = 'root'    # 用户名
MYSQL_PASS = '123456'    # 密码
MYSQL_HOST = 'localhost'    # 主库域名（可读写）
MYSQL_PORT = 3306    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int


DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}
