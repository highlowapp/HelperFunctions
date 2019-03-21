import pymysql

class User:

    #Define initialization function
    def __init__(self, uid, host, username, password, database):
        self.uid = uid
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        

        ## Get the user's data from MySQL ##

        #Connect to MySQL
        conn = pymysql.connect(host, username, password, database, cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()

        #Select the row with the user from the database
        cursor.execute("SELECT * FROM users WHERE uid='" + self.uid + "';")

        user = cursor.fetchone()

        #Commit and close the connection
        conn.commit()
        conn.close()

        #Make sure the user existed in the first place
        if user == None:
            raise ValueError("user-no-exist")

        #Otherwise, get all the data and store it
        self.firstname = user["firstname"]
        self.lastname = user["lastname"]
        self.password = user["password"]
        self.email = user["email"]
        self.profileimage = user["profileimage"]
    
    ## Setters ##

    #Any column
    def setColumn(self, column, value):

        #Connect to MySQL
        conn = pymysql.connect(self.host, self.username, self.password, self.database)
        cursor = conn.cursor()

        #Attempt to set the column
        cursor.execute("UPDATE users SET " + column + "'" + value + "' WHERE uid='" + self.uid + "';")

        #Commit and close the connection
        conn.commit()
        conn.close()

    def setFirstname(self, value):
        self.setColumn("firstname", value)

    def setLastname(self, value):
        self.setColumn("lastname", value)

    def setEmail(self, value):
        self.setColumn("email", value)

    def setProfileimage(self, value):
        self.setColumn("profileimage", value)

    def setPassword(self, value):
        print("WARNING: Setting the password can be dangerous!")
        self.setColumn("password", value)

        