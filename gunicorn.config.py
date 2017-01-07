# coding=utf-8
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
# worker_class = "gaiohttp"

max_requests = 1000
max_requests_jitter = 100

preload = True
sendfile = True

pidfile = "pid/app.pid"

accesslog = "log/access.log"
errorlog = "log/error.log"

