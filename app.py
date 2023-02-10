import flask
from flask import Flask, render_template , request
import random
from static.clubs import txt

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


print(txt[0]['Clubs_Link'])


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

        
@app.route('/list', methods=['POST']) 
def listPost(): 

    #print(request.form)

    day = request.form.get('day')
    time = request.form.get('time')

    addit = request.form.get('filter')

    newLoad = []

    for i in txt:

        if(len(day) > 2 and len(time) > 2):
            if str(day).lower() in str(i['Meeting_Time_and_Place']).lower() and str(time).lower() in str(i['Meeting_Time_and_Place']).lower():
                newLoad.append(i) 
            else:
                pass
        else:
            pass 

        if(len(time) > 2):
            if str(time).lower() in str(i['Meeting_Time_and_Place']).lower():
                newLoad.append(i) 
            else:
                pass
        else:
            pass 

        if(len(day) > 2):
            if str(day).lower() in str(i['Meeting_Time_and_Place']).lower():
                newLoad.append(i) 
            else:
                pass
        else:
            pass 

        if(len(addit) > 2):
            if str(addit).lower() in str(i).lower():
                newLoad.append(i)   
            else:
                pass
        else:
            pass 

    return render_template('list.html', newLoad=newLoad)


@app.route('/all')
def all():
    return render_template('all.html', load=txt)



app.run(port=2323)