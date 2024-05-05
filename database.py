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


# Driver code
# if __name__ == '__main__':

    # insert_into_login('cvmalavika@gmail.com', '1234')
    # insert_into_login('nkmadhukrishaa@gmail.com', 'abcd')

    # insert_into_PROFILE("C V MALAVIKA", "2004-08-16", 7200068373, "cvmalavika@gmail.com", "Indian", "Student", "Dancing, Drawing")
    # insert_into_PROFILE("N K MADHUKRISHAA", "2004-11-06", 9499947145, "nkmadhukrishaa@gmail.com", "Indian", "Student", "Dancing, Drawing, Poetry")

    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "I am very happy because the mid models exam has been postponed to next week due to IV", "Happiness")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "I am extremely sad because I miss my school friend", "Sadness")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "My friend talked with me harshly and now I am sad", "Sadness")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "I am very angry because my friend did not tell me that she had won the competition", "Anger")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "I am extremely surprised now because my parents bought me a gift for winning in the hackathon", "Surprise")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "I was disgusted at the sight of a group's behaviour towards a beggar while coming home", "Disgust")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "I don't want to go to the shop, there are a lot of dogs here that can bite anyone.", "Fear")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "I am really worried about my results in the semester examination", "Fear")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "I am really happy today, because I met my school friend today, she really threw me a surprise", "Surprise")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "My friend irritated me a lot today, I had a fight with her", "Anger")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "My friend and I went to college wearing same colour dress today, we both were surprised as we never planned it and so, we took a photo", "Surprise")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "During lunch time, I saw a puppy in my hostel sleeping quietly in a corner. It was soo beautiful and made my mood happy", "Happiness")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "I bunked a class today. I went to my class only during lunch break to notice that my professor was coming out of my class. I had a hearty laugh within me", "Surprise")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "I felt very guilty today for not attending the seminar that took place in my department's seminar hall.", "Sadness")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "I saw a snake in my hostel today. I was shocked and I constantly fear now if it is there somewhere around ", "Fear")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "I had a bad dream today. It was very very very disgusting!! I hate sleeping now!", "Disgust")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "I am excited that next week, we are going on a trip to my native!! It will be very nice to visit my friends there", "Happiness")
    # insert_into_ACTIVITIES("nkmadhukrishaa@gmail.com", "Me and my friend were talking about our school days and we has a hearty laugh. We could not control our laughs that when a faculty entered our class, she was surprised to see us laugh that much. I guess that professor would have thought that we went crazy!!", "Happiness")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "My friend tried to escape from the class to go and eat. By the time she went near the door, professor came in and pulled her to her bench. They both reminded me about my childhood days!!", "Happiness")
    # insert_into_ACTIVITIES("cvmalavika@gmail.com", "I saw a very big worm today, I could not concentrate in anything else because I felt very disgusted at the thought of it", "Disgust")
