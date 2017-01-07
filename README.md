# okeetee

## Install

```
pip install -r requirements.txt
```

## Start

```
gunicorn -c gunicorn.config.py --bind "127.0.0.1:8000" --daemon app:application

```

Apply `sudo` and change port if needed.

## Stop

```
kill `cat pid/app.pid`
```
