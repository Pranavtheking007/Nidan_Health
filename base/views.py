#imports
from django.shortcuts import render
from django.http import HttpResponse
from .forms import stroke
import tensorflow as tf
import base.Stroke_Main as STM
import base.Heart_Main as HM
import base.Diabetes_Main as Dia_New
import base.Diabetes_Life as Dia_Life
import base.Mental_Student as Men_Stud
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import pyrebase
import time
from datetime import datetime,timezone
import pytz

# Create your views here

#Your web app's Firebase configuration
#For Firebase JS SDK v7.20.0 and later, measurementId is optional
Config = {
  'apiKey': "AIzaSyDb8QpIKOBTskKiLMimxrf1PGydxDVKHLI",
  'authDomain': "nidan-b15a6.firebaseapp.com",
  'databaseURL': "https://nidan-b15a6-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "nidan-b15a6",
  'storageBucket': "nidan-b15a6.appspot.com",
  'messagingSenderId': "1023148822483",
  'appId': "1:1023148822483:web:7b1cbc91896a88582fa926",
  'measurementId': "G-4959W891PF",
  'databaseURL': "https://nidan-b15a6-default-rtdb.asia-southeast1.firebasedatabase.app"
};
# Config = {
#   'apiKey': "AIzaSyDO3w550comACj2SeQso1W26pab2qWfYJc",
#   'authDomain': "nidan-bd662.firebaseapp.com",
#   'projectId': "nidan-bd662",
#   'storageBucket': "nidan-bd662.appspot.com",
#   'messagingSenderId': "168818032129",
#   'appId': "1:168818032129:web:59afe36e586f70ee180a00",
#   'measurementId': "G-WFNZNJNPZ6",
#   "databaseURL": "https://nidan-b15a6-default-rtdb.asia-southeast1.firebasedatabase.app",
# };
firebase = pyrebase.initialize_app(Config);

auth = firebase.auth()
database = firebase.database()

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
            user = auth.sign_in_with_email_and_password(email,passw)
        except:
            msg = 'Invalid Credentials, COMRADE!!!'
            print(msg)

        session_id = user['idToken']
        request.session['uid']=str(session_id)
        return render(request,'index.html')

def chronic(request):
    return render(request , 'chronicdiseaseabout.html')

def physhlth(request):
    return render(request,'physicalhealthabout.html')

def mntlhlth(request):
    return render(request,'mentalhealthabout.html')

def dashboard(request):
    if request.method == 'GET':
        return render(request,'dashboardindex.html')
# Log Out Page
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
            user = auth.create_user_with_email_and_password(email,passw)
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

# def postsigh(request):
#     if request.method == 'POST':
#         print('POST*********')
#         name = request.POST['name']
#         email = request.POST['email']
#         passw = request.POST.get['pass']

#     data = {'name':name , 'email':email , 'passw':passw}
#     database.push(data)
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
        X = str(X)
        print("Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(Y)
        print("X:-****************************")
        print(X)
        print('\n')

        data = {
            'Gender':[gender],
            'Age':[age],
            'Hypertension':[Hypertension],
            'Heart disease':[heart_disease],
            'Ever Married':[ever_married],
            'Work Type':[work_type],
            'Residence Type':[residence_type],
            'Average Glcose Level':[avg_glucose_level],
            'BMI':[bmi],
            'Smoking Status':[smoking_status]
        }

        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))

        idtoken = request.session['uid']
        a = auth.get_account_info(idtoken)
        a=a['users']
        a=a[0]
        a=a['localId'] 
        print(str(a))

        database.child('users').child(a).child('Stroke').child(millis).set(data)        
        
        # return HttpResponse(request,{X,Y})
        if X=='[0]':
            return render(request ,'Stroke_No_Result.html',{'e':Y})
        else:
            return render(request,'Stroke_Yes_Result.html',{'e':Y})

    #return render(request,'Result_Tp.html',{'e':Y})
 
    
    
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
        chol = request.POST['chol']

        print('******************************')
        X = HM.predictions(cp,ca,sex,age,trestbps,thal,fbs,restecg,thalach,exang,oldpeak,slope,chol)
        X = str(X)
        print(X)

        data = {
            'Chest Pain':[cp],
            'ca':[ca],
            'Sex':[sex],
            'Age':[age],
            'trestbps':[trestbps],
            'thal':[thal],
            'fbs':[fbs],
            'restecg':[restecg],
            'thalach':[thalach],
            'exang':[exang],
            'oldpeak':[oldpeak],
            'slope':[slope],
            'chol':[chol]
        }

        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))

        idtoken = request.session['uid']
        a = auth.get_account_info(idtoken)
        a=a['users']
        a=a[0]
        a=a['localId'] 
        print(str(a)) 

        database.child('users').child(a).child('Heart Disease').child(millis).set(data)
    
    return render(request,'result.html',{'e':X})
    
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
        X=Dia_Life.prediction(BMI,Age,sex,Income,PhysHlth,GenHlth,HighBP,HighChol,Smoker,Stroke,HeartDisease,PhysActivity,Veggies,HeavyAlcoholConsump,DiffWalk)
        print(X)

        data = {
            'BMI':[BMI],
            'Age':[Age],
            'Sex':[sex],
            'Income':[Income],
            'Physical Health':[PhysHlth],
            'General Health':[GenHlth],
            'High BP':[HighBP],
            'High Cholestrol':[HighChol],
            'Smoker':[Smoker],
            'Stroke':[Stroke],
            'Heart Disease':[HeartDisease],
            'Physical Activity':[PhysActivity],
            'Veggies':[Veggies],
            'Heavy Alcohol Consumption':[HeavyAlcoholConsump],
            'Difficulty in walking':[DiffWalk]
        }

        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))

        idtoken = request.session['uid']
        a = auth.get_account_info(idtoken)
        a=a['users']
        a=a[0]
        a=a['localId'] 
        print(str(a)) 

        database.child('users').child(a).child('Mental Health Student').child(millis).set(data) 

        return render(request , 'diabetesmedresult.html',{'e':X})
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
        X = Dia_New.preds(Gender,Age,Urea,HbA1c,Chol,TG,HDL,VLDL,BMI)

        #return render(request , 'result.html',{'e':X})
        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))

        idtoken = request.session['uid']
        a = auth.get_account_info(idtoken)
        a=a['users']
        a=a[0]
        a=a['localId'] 
        print(str(a))

        data = {
            'Gender':Gender,
            'Age':Age,
            'Urea':Urea,
            'HbA1c':HbA1c,
            'Chol':Chol,
            'TG':TG,
            'HDL':HDL,
            'VLDL':VLDL,
            'BMI':BMI,
            'Result':str(X)
        }

        database.child('users').child(a).child('Dia_Med').child(millis).set(data)
        return render(request , 'diabetesmedresult.html',{'e':X})
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
        X=Men_Stud.predictions(Choose_your_gender,age,What_is_your_course,Your_current_year_of_Study,What_is_your_CGPA,Do_you_have_Anxiety,Do_you_have_Panic_attack,Did_you_seek_any_specialist_for_a_treatment)

        data = {
            'Gender':[Choose_your_gender],
            'Age':[age],
            'Course':[What_is_your_course],
            'Year of Study':[Your_current_year_of_Study],
            'CGPA':[What_is_your_CGPA],
            'Anxiety':[Do_you_have_Anxiety],
            'Panic Attack':[Do_you_have_Panic_attack],
            'Specialist Treatment':[Did_you_seek_any_specialist_for_a_treatment]
        }

        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))

        idtoken = request.session['uid']
        a = auth.get_account_info(idtoken)
        a=a['users']
        a=a[0]
        a=a['localId'] 
        print(str(a)) 

        database.child('users').child(a).child('Mental Health Student').child(millis).set(data)    
        
#Django report upload function

# def upload(request):
#     if request.method == 'POST':
#         upload_image = request.FILES['images'] # put images in html form <input type = 'form' name = 'images>
#         print(upload_image.size)
#         print(upload_image.name)

# settings.py 
# MEDIA_ROOT = os.path.join(BASE_DIR , 'media')
# MEDIA_URL = '/media/

#views.py file
#from django.core.files.storage import FileSystemStorage 
# fs = FileSystemStorage()
#fs.save(upload_image.name)

# urls.py(project wale file me)
#from django.config import settings
#from django.conf.urls.static import static
#if settings.DEBUG:
# urlpatterns = static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)        




#Django retrive data from the database
# def check(request):
#     idtoken = request.session['uid']
#     a = auth.get_account_info(idtoken)
#     a = a['users']
#     a = a[0]
#     a = a['localId']
#    # function report needed to be added in the firebase
#     timestamps = database.child('users').child(a).child('report').shallow().get().vals()
#     lis_tps = []
#     for i in timestamps:
#         lis_tps.append(i)
#     lis_tps.sort(reverse = True)    
#     print(timestamps)

#     return render(request, 'Result_Tp.html')
