# okeetee

## Install

```
pip install -r requirements.txt
```

## Start

```
gunicorn -c gunicorn.config.py --bind "0.0.0.0:8000" --daemon app:application
```

Apply `sudo` and change port to `80` if needed.

## Stop

```
kill `cat pid/app.pid`
```
