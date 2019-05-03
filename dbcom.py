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
<<<<<<< HEAD
=======

def getBrewVal(brew_ID, value):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    value = db.fetchone()
    #Returner ønsket verdi fra brygg(OG, FG, Temperatur)
>>>>>>> 49942eb89474837f992a42e4beb9a6143c2c0ce5
