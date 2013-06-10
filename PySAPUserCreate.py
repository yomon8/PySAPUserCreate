import csv
from ConfigParser import ConfigParser
from sapnwrfc2 import *

def userAdd(sapconn,userName,initPass,userType,firstName,lastName):
    try:
        passwordStruct = {u'BAPIPWD':initPass}        
        impStruct = {u'FIRSTNAME':firstName,u'LASTNAME':lastName}
        logonStruct = {u'USTYP':userType}
        result = sapconn.call('BAPI_USER_CREATE1',
                           USERNAME=userName,
                           PASSWORD=passwordStruct,
                           LOGONDATA=logonStruct,
                           ADDRESS=impStruct)
        print(result['RETURN'][0]['MESSAGE']) 

    except:
        print('Error Occurred in ' + userAdd.__name__ )
        raise

def getConnectionInfo():
    try:
        config = ConfigParser()
        config.read("sapnwrfc.cfg")
        return config._sections["connection"]
    except:
        print('Error Occurred in ' + getConnectionInfo.__name__)
        raise

if __name__ == '__main__':
    try:
        connecitonInfo = getConnectionInfo() 
        csvReader = csv.reader(open('userinfo.csv'),delimiter=',')
        sapconn = Connection(**connecitonInfo)
        for username,initpass,usertype,firstname,lastname in csvReader:
            userAdd(sapconn,username,initpass,usertype,firstname,lastname)
    finally:
        print('connection close')
        sapconn.close()
    
    
    
        
        
