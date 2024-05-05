import sqlite3
import plotly.express as px

conn = sqlite3.connect('MH.db', check_same_thread = False)
cursor = conn.cursor()

def get_levels_pie(email):

    cursor.execute('SELECT * FROM EMOTIONS WHERE Email_ID = ?', (email,))
    data = cursor.fetchall()

    cursor.execute('SELECT Name FROM Profile WHERE Email_ID = ?', (email,))
    data1 = cursor.fetchall()

    Labels = ['Happiness', 'Sadness', 'Disgust', 'Fear', 'Surprise', 'Anger']
    Values = list(data[0][1:])
    print(Values)

    fig = px.pie(data, names = Labels, values = Values, color = Labels,
                                color_discrete_map={'Happiness':'#09004f',
                                                        'Sadness':'#000080',
                                                        'Disgust':'#1c23c1',
                                                        'Fear':'#1c1df0',
                                                        'Surprise':'#40e0d0',
                                                        'Anger':'#b2ffff'})
    
    fig.update_layout(title=f'{data1[0][0]} - Your Mental Graph', )
    fig.update_traces(textinfo = 'label + percent', selector = dict(type = 'pie'))

    fig.write_html('MH_App/templates/piechart_mh.html')

# get_levels_pie('nkmadhukrishaa@gmail.com')