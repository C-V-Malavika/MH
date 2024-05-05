from django.shortcuts import render
from database import insert_into_login, select_all_login, select_all_profile, insert_into_PROFILE, insert_into_ACTIVITIES
from Visualisation import get_levels_pie
from Tasks_gen import create_tasks
import sqlite3

conn = sqlite3.connect('MH.db', check_same_thread = False)
cursor = conn.cursor()

# Create your views here.

def home(request):

    return render(request, 'welcome.html')


def signup(request):

    if request.method == "POST":

        email = request.POST['user']
        password = request.POST['pass']

        request.session['email'] = email
        request.session['password'] = password

        data = select_all_login()
        for user, pas in data:
            if user == email:
                return render(request,'login.html')

        insert_into_login(email, password)
        return render(request,'login.html')

    return render(request,'signup.html')


def login(request):

    if request.method == "POST":

        email = request.POST['user']
        password = request.POST['pass']

        data = select_all_login()

        Flag = False
        for user, pas in data:
            if user == email and pas == password:
                Flag = True
                break
            if user == email and pas != password:
                Flag = False

        if Flag == True:

            request.session['email'] = email
            request.session['password'] = password

            return render(request,'hello.html')

        elif Flag == False:

            request.session['email'] = email
            request.session['password'] = password
            return render(request,'password_login.html')

    return render(request,'login.html')


def profile(request):

    class Data:

        def __init__(self, Name, DOB, Phone_Number, Email_ID, Nationality, Occupation, Hobbies):

            self.Name = Name
            self.DOB = DOB
            self.Phone_Number = Phone_Number
            self.Email_ID = Email_ID
            self.Nationality = Nationality
            self.Occupation = Occupation
            self.Hobbies = Hobbies

    if request.method == "GET":

        item = select_all_profile(request.session['email'])

        if item is not None:

            data = []
            data.append(Data(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

            return render(request,'filledprofile.html', {'data' : data})

        else:
            return render(request,'profile.html')


def fill_profile(request):

    class Data:

        def __init__(self, Name, DOB, Phone_Number, Email_ID, Nationality, Occupation, Hobbies):

            self.Name = Name
            self.DOB = DOB
            self.Phone_Number = Phone_Number
            self.Email_ID = Email_ID
            self.Nationality = Nationality
            self.Occupation = Occupation
            self.Hobbies = Hobbies

    if request.method == "POST":

        name = request.POST['name']
        dob = request.POST['dob']
        phone = request.POST['phone']
        nationality = request.POST['nationality']
        occu = request.POST['occu']
        hobbies = request.POST['hobbies']

        insert_into_PROFILE(name, dob, phone, request.session['email'], nationality, occu, hobbies)

        data = []
        data.append(Data(name, dob, phone, request.session['email'], nationality, occu, hobbies))

        return render(request,'filledprofile.html', {'data' : data})


def activity(request):

    if request.method == "POST":

        description = request.POST['description']
        emotional = request.POST['emotional']

        insert_into_ACTIVITIES(request.session['email'], description, emotional)

        return render(request,'activity.html')

    return render(request,'activity.html')

def view_history(request):

    if request.method == "GET":

        cursor.execute('SELECT * FROM EMOTIONS WHERE Email_ID = ?', (request.session['email'],))
        data = cursor.fetchall()
        print(data)

        if data != []:

            get_levels_pie(request.session['email'])
            return render(request, 'piechart_mh.html')

        else:
            return render(request, 'notavail.html')
        
def tasks(request):

    class Data:

        def __init__(self, task1, task2, task3):

            self.Task1 = task1
            self.Task2 = task2
            self.Task3 = task3

    if request.method == "GET":

        print(create_tasks())
        t1, t2, t3 = create_tasks()
        data = []
        data.append(Data(t1, t2, t3))

        return render(request, 'tasks.html', {'data':data})
    
def chatbot(request):

    if request.method == 'GET':

        return render(request, 'https://oviasree-blissbound-chatbot-app-zj10pk.streamlit.app/')

def logout(request):

    if request.method == "GET":

        return render(request, 'welcome.html')