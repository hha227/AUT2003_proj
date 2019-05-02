import dbconfig.py as cfg
import pymysql

db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database'])
cursor = db.cursor()
