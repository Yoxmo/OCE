import flask
from flask import Flask, render_template , request
import random
from static.clubs import txt

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    randomC = random.choice(txt).get("Clubs_Link")
    return render_template('ind.html', choice=randomC)

@app.route('/list' , methods=['GET'])
def list():
    newLoad = []
    for i in range(10):
        newLoad.append(random.choice(txt))
    return render_template('list.html', newLoad=newLoad)

@app.route('/view' , methods=['GET'])
def view():
    newLoad = []
    for i in range(10):
        newLoad.append(random.choice(txt))
    return render_template('oce.html', newLoad=newLoad)

        
@app.route('/list', methods=['POST']) 
def listPost(): 

    day = request.form.get('day')
    time = request.form.get('time')

    addit = request.form.get('filter')

    newLoad = []

    for i in txt:

        if(len(day) > 0 and len(time) > 0 and len(addit) > 0 ):
            outputx = "[*] New search all time, addit, and day included..."

            if str(day).lower() in str(i['Meeting_Time_and_Place']).lower() and str(time).lower() in str(i['Meeting_Time_and_Place']).lower() and str(addit).lower() in str(i).lower():
                newLoad.append(i) 
            else:
                pass

        elif(len(day) > 0 and len(time) > 0):
            outputx = "[*] New search only day and time included..."

            if str(day).lower() in str(i['Meeting_Time_and_Place']).lower() and str(time).lower() in str(i['Meeting_Time_and_Place']).lower():
                newLoad.append(i) 
            else:
                pass

        elif(len(day) > 0 and len(addit) > 0):
            outputx = "[*] New search only day and audit included..."

            if str(day).lower() in str(i['Meeting_Time_and_Place']).lower() and str(addit).lower() in str(i).lower():
                newLoad.append(i) 
            else:
                pass

        else:
            outputx = "[*] New search only day included..."

            if str(day).lower() in str(i['Meeting_Time_and_Place']).lower():
                newLoad.append(i) 
            else:
                pass

    print(outputx)

    return render_template('list.html', newLoad=newLoad, day= day, time = time, addit = addit)


@app.route('/all')
def all():
    return render_template('all.html', load=txt)



app.run(port=2323)