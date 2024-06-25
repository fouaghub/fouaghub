# lev01_pen_test/logger.py
import os
import logging

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/general.log', level=logging.INFO, 
                    format='%(asctime)s %(message)s')
