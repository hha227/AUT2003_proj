import dbconfig as cfg
import pymysql

def addBrew(brew_name, brewer, og, target_fg, target_temp):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
    #Creating sql query
    sql = "INSERT INTO BREW_INFO(BrewName, Brewer, OG, TargetFG, TargetTemp)\
          VALUES('{}','{}','{:05.3f}','{:05.3f}','{:d}');\
          ".format(brew_name, brewer, og, target_fg, target_temp)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


def addMeasurement(id,gravity,temp):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
    sql = "INSERT INTO MEASUREMENTS(BrewID, SG, Temperature)\
           VALUES('{:d}','{:05.3f}','{:d}')".format(getCurrentBrewId(),gravity,temp)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

def getCurrentBrewId():
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
    sql = "SELECT MAX(BrewID) FROM(BREW_INFO)"
    try:
        cursor.execute(sql)
        brew_id = cursor.fetchone()
    except:
        print('Error')
    finally:
        db.close()
    return brew_id[0]

def getBrewInfo(property, id):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    cursor = db.cursor()
    sql = "SELECT ({}) FROM(BREW_INFO) WHERE BrewID='{:d}'".format(property,id)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
    except:
        print('Error')
    finally:
        db.close()
    return result[0]





def getBrewVal(brew_ID, value):
    db = pymysql.connect(cfg.mysql['host'], cfg.mysql['user'], cfg.mysql['password'], cfg.mysql['database']) #Open DB-connection
    value = db.fetchone()
    #Returner ønsket verdi fra brygg(OG, FG, Temperatur)
