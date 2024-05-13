import sqlite3
import datetime

conn = sqlite3.connect('MH.db', check_same_thread = False)

cursor = conn.cursor()

# cursor.execute("DROP TABLE LOGIN")
# cursor.execute("DROP TABLE PROFILE")
# cursor.execute("DROP TABLE ACTIVITIES")
# cursor.execute("DROP TABLE EMOTIONS")

# Table LOGIN
cursor.execute(
'''
    CREATE TABLE IF NOT EXISTS LOGIN(
        Email_ID VARCHAR PRIMARY KEY NOT NULL,
        Password VARCHAR)
'''
)

# Inserts record into the LOGIN table
def insert_into_login(email, password):

    cursor.execute("INSERT INTO LOGIN(Email_ID, Password) VALUES (?, ?)", (email, password))
    conn.commit()

# Returns all the records from the login table
def select_all_login():

        cursor.execute("SELECT * FROM LOGIN")
        res = cursor.fetchall()
        return res

# Returns the password for the given Email ID
def select_password(email):

        cursor.execute("SELECT Password FROM LOGIN WHERE Email_ID = ?", (email,))
        res = cursor.fetchone()
        return res[0][0]

# print(select_all_login())

# Table PROFILE
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS PROFILE(
    Name CHAR(25),
    DOB DATE,
    Phone_Number INTEGER,
    Email_ID VARCHAR PRIMARY KEY NOT NULL,
    Nationality CHAR(20),
    Occupation VARCHAR,
    Hobbies VARCHAR,
    FOREIGN KEY(Email_ID) REFERENCES LOGIN(Email_ID))
    '''
)

# Inserts record into the PROFILE table
def insert_into_PROFILE(name, dob, ph_no, email, nationality, occupation, hobbies):

    cursor.execute("INSERT INTO PROFILE(Name, DOB, Phone_Number, Email_ID, Nationality, Occupation, Hobbies) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (name, dob, ph_no, email, nationality, occupation, hobbies))
    conn.commit()


# Selects all the records from the PROFILE table
def select_all_profile(email):

    cursor.execute("SELECT * FROM PROFILE WHERE Email_ID = ?", (email,))
    res = cursor.fetchone()
    return res

# print(select_all_profile('valuerchandrakani@gmail.com'))

# Table ACTIVITIES
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS ACTIVITIES(
    Email_ID VARCHAR,
    Date_of_activity DATE,
    Time_of_activity TIME,
    Description VARCHAR,
    Emotional_State VARCHAR,
    FOREIGN KEY(Email_ID) REFERENCES LOGIN(Email_ID))
    '''
)

def find_dt():

    now = datetime.datetime.now()
    date = f"{now.year} : {now.month} : {now.day}"
    return date

def find_time():

    now = datetime.datetime.now()
    time = f"{now.hour} : {now.minute} : {now.second}"
    return time


# Inserts record into the ACTIVITIES table
def insert_into_ACTIVITIES(email, description, emo_stat):

    cursor.execute("INSERT INTO ACTIVITIES(Email_ID, Date_of_activity, Time_of_activity, Description, Emotional_State) VALUES (?, ?, ?, ?, ?)",
                   (email, find_dt(), find_time(), description, emo_stat))
    conn.commit()
    ACTIVITY_EMOTIONS(email, emo_stat)

# cursor.execute("SELECT * FROM ACTIVITIES")
# r = cursor.fetchall()
# print(r)
# print()

# Selects all the records from the ACTIVITIES table
def select_all_ACTIVITIES(email):

    cursor.execute("SELECT * FROM ACTIVITIES WHERE Email_ID = ?", (email,))
    res = cursor.fetchall()
    return res

# print(select_all_ACTIVITIES('nkmadhukrishaa@gmail.com'))

def ACTIVITY_EMOTIONS(e_mail, emotion):

    cursor.execute("SELECT * FROM EMOTIONS WHERE Email_ID = ?", (e_mail,))
    res1 = cursor.fetchall()
    if res1 == []:
        insert_into_EMOTIONS(e_mail, emotion)
    elif len(res1) == 1:
        update_EMOTIONS(e_mail, emotion)

# Table EMOTIONS
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS EMOTIONS(
    Email_ID VARCHAR,
    Happiness INTEGER,
    Sadness INTEGER,
    Disgust INTEGER,
    Fear INTEGER,
    Surprise INTEGER,
    Anger INTEGER,
    FOREIGN KEY(Email_ID) REFERENCES LOGIN(Email_ID))
    '''
)

# cursor.execute("SELECT * FROM EMOTIONS")
# r = cursor.fetchall()
# print(r)
# print()

# Inserts record into the EMOTIONS table based on the type of
# emotion for every input in ACTIVITIES table
def insert_into_EMOTIONS(email, emotion):
    
    if emotion is not None:
        
        cursor.execute("INSERT INTO EMOTIONS(Email_ID, Happiness, Sadness, Disgust, Fear, Surprise, Anger) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (email, 0, 0, 0, 0, 0, 0))
        conn.commit()

        update_EMOTIONS(email, emotion)

# Updates the EMOTIONS table corresponding to the respective emotion type
# for every input to the ACTIVITIES table
def update_EMOTIONS(email, emotion):
    
    if emotion is not None:
         
        if emotion == 'Happiness':
            cursor.execute("UPDATE EMOTIONS SET Happiness = Happiness + ? WHERE Email_ID = ?", (1, email))
            conn.commit()

        elif emotion == 'Sadness':
            cursor.execute("UPDATE EMOTIONS SET Sadness = Sadness + ? WHERE Email_ID = ?", (1, email))
            conn.commit()

        elif emotion == 'Disgust':
            cursor.execute("UPDATE EMOTIONS SET Disgust = Disgust + ? WHERE Email_ID = ?", (1, email))
            conn.commit()
            
        elif emotion == 'Fear':
            cursor.execute("UPDATE EMOTIONS SET Fear = Fear + ? WHERE Email_ID = ?", (1, email))
            conn.commit()

        elif emotion == 'Surprise':
            cursor.execute("UPDATE EMOTIONS SET Surprise = Surprise + ? WHERE Email_ID = ?", (1, email))
            conn.commit()

        elif emotion == 'Anger':
            cursor.execute("UPDATE EMOTIONS SET Anger = Anger + ? WHERE Email_ID = ?", (1, email))
            conn.commit()
