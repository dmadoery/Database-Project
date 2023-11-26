""" 
small template to outsource sensible information while still being able to push files to repo 
"""

pw = "INSERT PASSWORD" # password to access database
db = 'group8' # name of the database
usr = "INSERT USER NAME" # username to access database, usually 'root'

def getPwd():
    return pw
    
def getDb():
    return db

def getUser():
    return usr