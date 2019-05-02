import dbconfig.py as cfg
import pymysql

def addBrew(brew_name, brewer, og, target_fg, target_temp):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
    #Creating sql query
    sql = "INSERT INTO brew_info(name, brewer, )"


def addMeasurement(gravity,temp):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
    
