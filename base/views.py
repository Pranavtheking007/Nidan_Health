#imports
from django.shortcuts import render
from django.http import HttpResponse
import joblib
from .forms import stroke
import tensorflow as tf
import base.Stroke_Main as STM
import h5py
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import pyrebase

# Create your views here

#Your web app's Firebase configuration
#For Firebase JS SDK v7.20.0 and later, measurementId is optional
Config = {
  'apiKey': "AIzaSyDO3w550comACj2SeQso1W26pab2qWfYJc",
  'authDomain': "nidan-bd662.firebaseapp.com",
  'projectId': "nidan-bd662",
  'storageBucket': "nidan-bd662.appspot.com",
  'messagingSenderId': "168818032129",
  'appId': "1:168818032129:web:59afe36e586f70ee180a00",
  'measurementId': "G-WFNZNJNPZ6",
  "databaseURL": "https://nidan-b15a6-default-rtdb.asia-southeast1.firebasedatabase.app",
};
firebase = pyrebase.initialize_app(Config);

authe = firebase.auth()
database = firebase.database()
'''''
# Sign In Page

def login(request):
       print('GET****************')
       return render(request , 'loginsignup.html')


def Login(request): 
    
    
    if request.method == 'POST':
        print('POST****************')
        email = request.POST.get('email')
        passw = request.POST.get('pass')

    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        msg = 'Invalid Credentials, COMRADE!!!'

    session_id = user['idToken']
    request.session['uid']=str(session_id)



# Log Out Page
"""
aut.logout(request)

"""

# Sign Up Page

def SignUP(request):
    if request.method == 'POST':
        print('POST*********')
        name = request.POST.get('name')
        email = request.POST.get('email')
        passw = request.POST.get('pass')
        #print(name,email,passw)
        try:
            user = authe.create_user_with_email_and_password(email,passw)
            print('YAY')
            uid = user['localId']
        except:
            msg = 'Unable to sign you up currently'
            print('OH NOOOOOOO !!!!!!!')

        data = {
        'name':name,
        'status':'1'
        }

        database.child('users').child(uid).child('details').set(data)
        return render(request,'index.html')

def postsigh(request):
    if request.method == 'POST':
        print('POST*********')
        name = request.POST['name']
        email = request.POST['email']
        passw = request.POST.get['pass']

    data = {'name':name , 'email':email , 'passw':passw}
    database.push(data)
# Now for any models
"""
import time
drom datetime import datetime,timezone
import pytz

tz = pytz.timezone('Asia/Kolkata')
time_now = datetime.now(timezone.utc).astimezone(utc)
millis = int(time.mktime(time_now.timetuple()))

idtoken = request.session['uid']
a = authe.get_account_info(idtoken)
a=a['user']
a=a[0]
a=a['localid'] 

database.child('users').child(a).child(#Jo Bhi prediction ho rha ho => naam string mai hona chahiye).child('millis').child(data)

"""
'''
# home function
def home(request):

    return render(request , 'index.html') 

#card function
def card(request):
    if request.method == 'GET':
        return render(request,'card.html')

#storke page render
def stroke(request):
     
    if request.method =='GET':
        return render(request,'stroke.html')

    if request.method == 'POST':
        gender = request.POST['gender']
        ever_married  = request.POST['ever_married']
        work_type = request.POST['work_type']
        residence_type = request.POST["residence_type"]
        smoking_status = request.POST["smoking_status"]
        age = request.POST['age']
        Hypertension = request.POST['hypertension']
        heart_disease = request.POST['heart_disease']
        avg_glucose_level = request.POST["avg_glucose_level"] 
        bmi = request.POST['bmi']
        
        
        #return HttpResponse(gender,age,Hypertension,heart_disease,ever_married,work_type) 
        X,Y=STM.Predictions(gender,age,Hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smoking_status)
        #print("***********")
        #print('\n')
        #print(X)  
        #print('\n')
        ##print(Y)
        #print('\n') 
        Y=str(Y)
        # return HttpResponse(request,{X,Y})
        #return render(request,'Result_Tp.html',{'e':X}
    return render(request,'Result_Tp.html',{'e':Y})
 
    
    
#heart disease page render

def heart(request):
    
    if request.method =='GET':
        return render(request,'heartdisease.html')
    if request.method == 'POST':
        cp = request.POST['cp']
        ca = request.POST['ca']
        sex = request.POST['sex']
        age = request.POST['age']
        trestbps = request.POST['trestbps']
        thal = request.POST['thal']
        fbs = request.POST['fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak = request.POST['oldpeak']
        slope = request.POST['slope']

        print('******************************')
        print(cp,ca,sex,age,trestbps,thal,fbs,restecg,thalach,exang,oldpeak,slope)
        
    #return render('Result_Tp.html')
    
    #if request. == 'POST':

#diabetes page render 
def diabetes(request):
    
    if request.method =='GET':
        return render(request,'diabetes.html')
    
    if request.method =='POST':
        BMI = request.POST['BMI']
        Age = request.POST['Age']
        sex = request.POST['sex']
        Income = request.POST['Income']
        PhysHlth = request.POST['PhysHlth']
        GenHlth = request.POST['GenHlth']
        HighBP = request.POST['HighBP']
        HighChol = request.POST['HighChol']
        Smoker = request.POST['Smoker']
        Stroke = request.POST['Stroke']
        HeartDisease = request.POST['HeartDisease']
        PhysActivity = request.POST['PhysActivity']
        Veggies = request.POST['Veggies']
        HeavyAlcoholConsump = request.POST['HeavyAlcoholConsump']
        DiffWalk = request.POST['DiffWalk']

        print("****************************************")
        print(BMI,Age,sex,Income,PhysHlth,GenHlth,HighBP,HighChol,Smoker,Stroke,HeartDisease,PhysActivity,Veggies,HeavyAlcoholConsump,DiffWalk)

#diabetes med page render
def diabetesmed(request):
    
    if request.method =='GET':
        return render(request,'diabetesmed.html')
    
    if request.method =='POST':
        Gender = request.POST['Gender']
        Age = request.POST['Age']
        Urea = request.POST['Urea']
        HbA1c = request.POST['HbA1c']
        Chol = request.POST['Chol']
        TG = request.POST['TG']
        HDL = request.POST['HDL']
        VLDL = request.POST['VLDL']
        BMI = request.POST['BMI']  

        print('*************************************************')
        print(Gender,Age,Urea,HbA1c,Chol,TG,HDL,VLDL,BMI)
#mental health students
def mentalhlth(request):
    
    if request.method =='GET':
        return render(request,'mentalhealthstudents.html')
    
    if request.method =='POST':
        Choose_your_gender = request.POST['Choose your gender']
        age = request.POST['age']
        What_is_your_course = request.POST['What is your course?']
        Your_current_year_of_Study = request.POST['Your  current year of Study']
        What_is_your_CGPA = request.POST['What is your CGPA?']
        Do_you_have_Anxiety = request.POST['Do you have Anxiety?']
        Do_you_have_Panic_attack = request.POST['Do you have Panic attack?']
        Did_you_seek_any_specialist_for_a_treatment = request.POST['Did you seek any specialist for a treatment?']

    print('******************************************************')
    print(Choose_your_gender,age,What_is_your_course,Your_current_year_of_Study,What_is_your_CGPA,Do_you_have_Anxiety,Do_you_have_Panic_attack,Did_you_seek_any_specialist_for_a_treatment)    