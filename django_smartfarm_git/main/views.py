import os
import shutil
import glob
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage

from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.preprocessing import image
import tensorflow as tf
import tensorflow
from tensorflow import Graph
import pickle
import cv2
import numpy as np

from main.models import Temp
from main.models import Good
from main.models import Other
from main.models import Month_Season

import time
import datetime
from datetime import datetime, timedelta
import random
from django.db.models import Q

def fiindex(request):
    return render(request, "login.html")
    
def index(request):
    global now, ynow, mnow, dnow
    now = time.localtime()
    ynow = now.tm_year
    mnow = now.tm_mon
    dnow = now.tm_mday

    global season 
    if 3<= mnow <= 5:
        season = "봄"
    elif 6<= mnow <= 8:
        season = "여름"
    elif 9<= mnow <= 10:
        season = "가을"
    else:
        season = "겨울"

    global sfarm
    if season == "봄":
        sfarm = Month_Season.objects.filter(s_season = 'spring')
    elif season == "여름":
        sfarm = Month_Season.objects.filter(s_season = 'summer')
    elif season == "가을":
        sfarm = Month_Season.objects.filter(s_season = 'autumn')
    else:
        sfarm = Month_Season.objects.filter(s_season = 'winter')

    global temp, n_temp, n_humid
    temp = Temp.objects.last() 
    n_temp = temp.temper
    n_humid = temp.humadi

    global gfarm
    gfarm = Other.objects.filter(good_min_temp__lte = n_temp, good_max_temp__gte = n_temp,
        good_min_humid__lte = n_humid, good_max_humid__gte = n_humid)
    global temp_tomato
    temp_tomato = Good.objects.get(name='tomato')
    global temp_pepper
    temp_pepper = Good.objects.get(name='pepper')
    global temp_sangcu
    temp_sangcu = Good.objects.get(name='sangcu')

    datas = {"Temp" : temp, "Temp_tomato" : temp_tomato, "Temp_pepper" :temp_pepper, "Temp_sangcu" : temp_sangcu, "Ynow":ynow, "Mnow" : mnow, "Dnow" : dnow, 
    "Season" : season, "Sfarm" : sfarm, "Gfarm" : gfarm}
    return render(request, "index.html", datas)

def predictimage(request):
    #사진 저장 
    fileObj = request.FILES['filePath']
    filePathName = default_storage.save('./media/'+ "/"+request.session["id"]+"/"+fileObj.name, fileObj)
    filePathName = default_storage.url(filePathName)
    testimage = '.' + filePathName
    #추론
    model = load_model('./models/cityfarmer2_hy.h5')
    img = cv2.imread(testimage, cv2.IMREAD_COLOR)
    img = cv2.resize(img, dsize=(224, 224), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    img = img/255
    ans = model.predict_classes(np.expand_dims(img,axis = 0))
    with open('./models/class20.pickle', 'rb')as f:
        class20 = pickle.load(f)
    global predictedLabel
    predictedLabel = '{}'.format(class20[ans[0]])
    if predictedLabel == "tomato_baby":
        src = testimage
        dst = './media/media/'+request.session["id"]+"/"+"tomato"+"/"
        shutil.copy(src,dst)
    elif predictedLabel == "tomato_adult":
        src = testimage
        dst = './media/media/'+request.session["id"]+"/"+"tomato"+"/"
        shutil.copy(src,dst)
    elif predictedLabel == "pepper_baby":
        src = testimage
        dst = './media/media/'+request.session["id"]+"/"+"pepper"+"/"
        shutil.copy(src,dst)
    elif predictedLabel == "pepper_adult":
        src = testimage
        dst = './media/media/'+request.session["id"]+"/"+"pepper"+"/"
        shutil.copy(src,dst)
    elif predictedLabel == "sangchu_baby":
        src = testimage
        dst = './media/media/'+request.session["id"]+"/"+"sangcu"+"/"
        shutil.copy(src,dst)
    elif predictedLabel == "sangchu_adult":
        src = testimage
        dst = './media/media/'+request.session["id"]+"/"+"sangcu"+"/"
        shutil.copy(src,dst)
        

    datas = {"Temp" : temp, "Temp_tomato" : temp_tomato, "Temp_pepper" :temp_pepper, "Temp_sangcu" : temp_sangcu, "Ynow":ynow, "Mnow" : mnow, "Dnow" : dnow,
    "Season" : season, "Sfarm" : sfarm, "Gfarm" : gfarm, 'filePathName':filePathName, 'predictedLabel' : predictedLabel}
    return render(request, 'index.html', datas)

def showphoto(request):
    listofimages_t = os.listdir('./media/media/'+ "/"+request.session["id"]+"/"+"tomato"+"/")
    listofimagesPath_t = ['./media/media/'+ "/"+request.session["id"]+"/"+"tomato"+"/"+i for i in listofimages_t]
    listofimages_s = os.listdir('./media/media/'+ "/"+request.session["id"]+"/"+"sangcu"+"/")
    listofimagesPath_s = ['./media/media/'+ "/"+request.session["id"]+"/"+"sangcu"+"/"+i for i in listofimages_s]
    listofimages_p = os.listdir('./media/media/'+ "/"+request.session["id"]+"/"+"pepper"+"/")
    listofimagesPath_p = ['./media/media/'+ "/"+request.session["id"]+"/"+"pepper"+"/"+i for i in listofimages_p]
    datas = {"listofimagesPath_t" : listofimagesPath_t, "listofimagesPath_s" : listofimagesPath_s,"listofimagesPath_p" : listofimagesPath_p}
    return render(request, 'showphoto.html', datas)

def tomato_givewater(request):
    print(predictedLabel)
    time = datetime.now()
    print(time)
    t_water = time + timedelta(days=3) 
    print(t_water)
    datas = {"Temp" : temp, "Temp_tomato" : temp_tomato, "Temp_pepper" :temp_pepper, "Temp_sangcu" : temp_sangcu, "Ynow":ynow, "Mnow" : mnow, "Dnow" : dnow,
    "Season" : season, "Sfarm" : sfarm, "Gfarm" : gfarm, 'predictedLabel' : predictedLabel, "t_water" : t_water}
    return render(request, 'index.html', datas)

def pepper_givewater(request):
    print(predictedLabel)
    time = datetime.now()
    print(time)
    d_water = time + timedelta(days=3) 
    print(d_water)
    datas = {"Temp" : temp, "Temp_tomato" : temp_tomato, "Temp_pepper" :temp_pepper, "Temp_sangcu" : temp_sangcu, "Ynow":ynow, "Mnow" : mnow, "Dnow" : dnow,
    "Season" : season, "Sfarm" : sfarm, "Gfarm" : gfarm, 'predictedLabel' : predictedLabel, "d_water" : d_water}
    return render(request, 'index.html', datas)

def sangcu_givewater(request):
    print(predictedLabel)
    time = datetime.now()
    print(time)
    s_water = time + timedelta(days=3) 
    print(s_water)
    datas = {"Temp" : temp, "Temp_tomato" : temp_tomato, "Temp_pepper" :temp_pepper, "Temp_sangcu" : temp_sangcu, "Ynow":ynow, "Mnow" : mnow, "Dnow" : dnow,
    "Season" : season, "Sfarm" : sfarm, "Gfarm" : gfarm, 'predictedLabel' : predictedLabel, "s_water" : s_water}
    return render(request, 'index.html', datas)

def logout(request):
    if request.session.get("id")== None:
        return render(request, "login.html")
    else:
        del request.session["id"]
        del request.session["name"]
        return render(request, "login.html")

def showlive(request):
    return render(request, 'showlive.html')