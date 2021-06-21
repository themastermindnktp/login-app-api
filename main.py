# coding=utf-8
import logging
import os
from core import app
from dotenv import load_dotenv

_logger = logging.getLogger(__name__)

_DOT_ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(_DOT_ENV_PATH)

if __name__ == '__main__':
    app.run()
