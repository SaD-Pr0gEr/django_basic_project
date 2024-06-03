import multiprocessing

bind = '127.0.0.1:8001'  # Set bind url here
workers = multiprocessing.cpu_count() * 2 + 1
user = 'root'  # project owner username
timeout = 60
raw_env = ['DJANGO_SETTINGS_MODULE=core.settings.prod']
