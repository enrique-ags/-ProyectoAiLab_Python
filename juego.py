import csv
class Juego:

    def __init__(self):
        
        archivo = open('Usuario1.csv','a')
        with archivo:
            escritor = csv.writer(archivo)
        '''    escritor.writerows(a)'''

    def validAdministradorExist(self):
        flag=False
        with open('Usuario1.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for renglon in lector:
                 if len(renglon)>0:
                    if renglon[1] == '10':
                        flag = True
                    else:
                        flag= False
        return  flag

    def creadAdminUser(self, userid,password,level):

        self.userid = '10'
        self.password = password
        self.level = level
        a = [['password','user','level'],[self.userid,self.password, self.level]]
        archivo = open('Usuario1.csv','a')
        try:
            with archivo:
                escritor = csv.writer(archivo,'w')
                escritor.writerows(a)
            return True
        except:
            return False

    def isDuplicated(self, userID):
        self.userID = userID
        flag=False
        with open('Usuario1.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for renglon in lector:
                if len(renglon)>0:
                    if renglon[1] == self.userID:
                        flag = True
                    else:
                        flag= False
        return  flag 
    def insertNewUser(self, userid, password, level):
        self.userid = userid
        self.password = password
        self.level = level
        l = [[self.userid,self.password, self.level]]
        archivo = open('Usuario1.csv','a')
        try:
            with archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(l)
            return True
        except:
            return False
    def validate_csv(self, userID,password):
        self.userID = userID
        self.password = password
        
        flag=False
        with open('Usuario1.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for renglon in lector:
               
                if len(renglon)>0:
                    
                    if renglon[0] == self.userID and renglon[1]==self.password:
                        flag = True
                        break
                    else:
                        flag= False
        return  flag 
    
    def userExists(self, userID):
       self.userID = userID
       
        
       flag=False
       with open('Usuario1.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for renglon in lector:               
                if len(renglon)>0:                    
                    if renglon[0] == self.userID:
                        flag = True
                        break
                    else:
                        flag= False
            return  flag    
    




    








        


