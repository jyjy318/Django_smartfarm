import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# 모델 호출
from user.models import User

# 파일 업로드
from django.core.files.storage import FileSystemStorage

# DB 저장
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine

# 암호화
import bcrypt

# 1. 초기화면 페이지
def index(request):
    return render(request, "login.html")

# 2. 로그인
@csrf_exempt
def login(request):
    if request.method == "POST":
        login_data = request.POST
        id = login_data['id']
        login_list = User.objects.filter(user_id=id)
        input_pw = login_data['pw'].encode('utf-8')
        if login_list.first() == None:
            return render(request, "login.html", {"success": 0 })
        else:
            pw = login_list[0].pw.encode('utf-8')
            pw_check= bcrypt.checkpw(input_pw, pw)
            if pw_check == True:
                request.session["id"] = login_list[0].user_id
                request.session["name"] = login_list[0].name
                return redirect("index")
            else:
                return render(request, "login.html", {"success":-1}) 
    else:
        return redirect("index")

#3. 회원가입
def joinus(request):
    return render(request, 'join.html', {})

#4. 사용자 등록
@csrf_exempt
def user_insert(request):
    userID = request.POST.get('userID', '')
    name = request.POST.get('userName', '')
    pw = request.POST.get('userPW', '')
 
    password = pw.encode('utf-8')
    password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
    password_crypt = password_crypt.decode('utf-8')
    userdatas = User(user_id=userID, name=name, pw=password_crypt)
    dir_path = "./media/media"
    dir_name = userID
    if os.path.isdir(dir_path+"/"+dir_name+"/") == True:
        return render(request, "join.html", {"success":1})
    else:
        os.mkdir(dir_path+"/"+dir_name+"/")
        dir_path = "./media/media"+"/"+userID
        dir_name = "tomato"
        os.mkdir(dir_path+"/"+dir_name+"/")
        dir_path = "./media/media"+"/"+userID
        dir_name = "sangcu"
        os.mkdir(dir_path+"/"+dir_name+"/")
        dir_path = "./media/media"+"/"+userID
        dir_name = "pepper"
        os.mkdir(dir_path+"/"+dir_name+"/")
        userdatas.save()
        return render(request, "login.html", {})
    

