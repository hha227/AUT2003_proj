import dbconfig as cfg
import pymysql

def addBrew(brew_name, brewer, og, target_fg, target_temp):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
    #Creating sql query
    sql = "INSERT INTO brew_info(brew_name, brewer, og, target_fg, target_temp)\
          VALUES('{}','{}','{:05.4f}','{:05.4f}','{:d}');\
          ".format(brew_name, brewer, og, target_fg, target_temp)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def addMeasurement(gravity,temp):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
