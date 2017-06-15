#!/usr/bin/python
# run.py
import os
from web_app import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port)