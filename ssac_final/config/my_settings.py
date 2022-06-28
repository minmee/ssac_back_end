
SECRET_KEY = "cc)*5=(s+i2-&9x7&&&o+y7$g5!db3tvu85ykok#mwxf#6gir2"
MYSQL_ID = 'root'
MYSQL_PASSWORD = 'ssac1234!'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ssacdb',
        'USER': f'{MYSQL_ID}',
        'PASSWORD': f'{MYSQL_PASSWORD}',
        'HOST': 'ssacdb.clvyujlywwfo.us-east-1.rds.amazonaws.com',
        'OPTIONS': {
        'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'PORT': '3306'
    }
}
