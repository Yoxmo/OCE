import flask
from flask import Flask, render_template , request
import random
from static.clubs import txt

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    randomC = str(random.choice(txt).get("Clubs_Link")).replace('https://activities.osu.edu/involvement/student_organizations/find_a_student_org?i=' ,'').replace('&l=ALL&v=list&c=Columbus&page=0' , '')
    randomC = f"view?id={randomC}"

    random1 = str(random.choice(txt).get("Clubs_img"))
    random2 = str(random.choice(txt).get("Clubs_img"))
    random3 = str(random.choice(txt).get("Clubs_img"))

    if random1 == "https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-10615.jpg":
        random1 = "https://activities.osu.edu/posts/studentorgs/logos/official-logo-640x480.png"
        
    if random2 == "https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-10615.jpg":
        random2 = "https://activities.osu.edu/posts/studentorgs/logos/quizbowl_1-640x480.PNG"
    
    if random3 == "https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-10615.jpg":
        random3 = "https://activities.osu.edu/posts/studentorgs/logos/1girl-logo-640x480.png"
           

    return render_template('index.html', choice=randomC, random1 =random1, random2=random2, random3= random3)

@app.route('/list' , methods=['GET'])
def list():
    newLoad = []
    for i in range(10):
        newLoad.append(random.choice(txt))
    return render_template('list.html', newLoad=newLoad)

@app.route('/view' , methods=['GET'])
def view():
    args = request.args.to_dict()
    if args:
        link = str(args["id"])
        link = f"https://activities.osu.edu/involvement/student_organizations/find_a_student_org?i={link}&l=ALL&v=list&c=Columbus&page=0"
        if link:
            for i in txt:
                if(i['Clubs_Link'] == link):
                    x = i
            return render_template('oce.html', newLoad=x)
        else:
            return '[*] Error no arg ID but we do have ' + str(args)
    else:
        return '[*] Error no args'
        
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
    return render_template('complete.html', load=txt)



app.run(host="0.0.0.0", )