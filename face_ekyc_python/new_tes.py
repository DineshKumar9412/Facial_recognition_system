# # from flask import Flask, request
# # import numpy as np
# # import cv2
# #
# # app = Flask(__name__)
# #
# # @app.route('/de',  methods= ['POST','GET'])
# # def card():
# #    if request.method == 'POST':
# #        # file = request.files.getlist("file[]")
# #        files = request.files.getlist("file")
# #        # print(files[0].filename, files[1].filename)
# #        doc_file = files[0]
# #        selfie_file = files[1]
# #        print(doc_file.filename, selfie_file.filename)
# #        # a = "hhvb"
# #        # print(file)
# #        return "bvshvxzb"
# #    else:
# #        return "no"
#        # npimg = np.fromfile(file, np.uint8)
#        # file = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
#        # print(file)
#        # return "age"
#
#        #
#        # obj = DeepFace.analyze(file, actions=['age', 'gender'])
#        # # print(obj["age"])
#        # res = str(obj["age"])
#        # Age = str(obj["gender"])
#        # return Age
#        #
#        # # return "hi i am image"
#
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
# # from flask import Flask
# # app = Flask(__name__)
# #
# # @app.route('/flask')
# # def hello_flask():
# #    return 'Hello Flask'
# #
# # @app.route('/python/')
# # def hello_python():
# #    return 'Hello Python'
# #
# # if __name__ == '__main__':
# #    app.run()
# # lst = (10,22,37,41,100,123,29)
# # oddlist = tuple(map(lambda x:(x%3 == 0),lst))
# # print(oddlist)
# # adds = (map(lambda x:(x%3 == 0),lst))()
#
# # from Employees.ITEmployees import getITNames
# # print(Employees.getNames())
# # import Employees
# # print(getITNames())
#
# # from res import one
# #
# # print(one.nme())
# from flask import Flask
# from flask_restful import Resource, Api
# import datetime
# from flask import request
# from functools import wraps
#
# app = Flask(__name__)
# api = Api(app)
#
# def monitor(function=None):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         _ = function(*args, **kwargs)
#         print("Ip Address  : {} ".format(request.remote_user))
#         print("Cookies : {} ".format(request.cookies))
#         print(request.user_agent)
#         return _
#     return wrapper
# class HelloWorld(Resource):
#     @monitor
#     def get(self):
#         return {'hello': 'world'}
# api.add_resource(HelloWorld, '/')
# if __name__ == '__main__':
#     app.run(debug=True)


# import secrets
# df = secrets.token_hex(2)# how many you want ex: secrets.token_hex(25) its create a key
# print(df)



# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")
#
# payload = {
#         "user_id": "user",
#         "password":"admin@123",
#         "id_no": 67}
# token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#
# print(token)
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidXNlciIsInBhc3N3b3JkIjoiYWRtaW5AMTIzIiwiaWRfbm8iOjY3fQ.dWlZG_IMN_dB16tdkYcLjySZmVAcv_d2Bx5XieXW5qg"
#
# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")
# decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
# print(decoded_token)
# use = "user"
# pas = "admin@123"
#
# if decoded_token['user_id'] == use and decoded_token['password'] == pas:
#         print("yes")
# else:
#         print("NO")

from fastapi import Request, FastAPI, File, UploadFile,Depends,Form
import uvicorn
from pydantic import BaseModel
import time
from typing import Dict
import jwt
from decouple import config
import speech_recognition as sr
from pytz import timezone
from datetime import datetime

ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')

app = FastAPI()

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

r = sr.Recognizer()

class Info(BaseModel):
    encounter_UUID : int
    patient_UUID : int
    doctor_UUID : int

async def checker(data: str = Form(...)):
    try:
        model = Info.parse_raw(data)
        print(model)
    except Exception as e:
        return {"Success": "false", "Result": str(e)}
    return model

@app.post("/voice_to_text/")
async def submit(model: Info = Depends(checker), files : UploadFile = File(...)):
    dis = dict(model)
    res = files.file
    try:
        token = jwt.encode(dis, JWT_SECRET, algorithm=JWT_ALGORITHM)
        with sr.AudioFile(res) as source:
            audio_text = r.listen(source)
            with open(f'files/{token}{ind_time}.wav', 'wb') as file:
                file.write(audio_text.get_wav_data())
            text = r.recognize_google(audio_text)
            return {"Token ": token, "Text_value":text,"Path_location": "/Users/harikumar/PycharmProjects/Flask_api_test/venv/files"}
    except Exception as e:
        return {"Success": "false", "Result": str(e)}




# @app.post("/getInformation")
# def getInformation(base: Info = Depends(),files : UploadFile = File(...)):
#     dis = dict(base)
#     res = files.file
#     with sr.AudioFile(res) as source:
#         audio_text = r.listen(source)
#         text = r.recognize_google(audio_text)
#         return {"Token": text, "Result": dis}

    # return dis, res

    # res = info.files.file
    # with sr.AudioFile(res) as source:
    #     audio_text = r.listen(source)
    #     text = r.recognize_google(audio_text)
    #     return {"Token": text}


    # res = files.file
    # return {"resy": res}
    # # dis = dict(info)
    # # token = jwt.encode(dis, JWT_SECRET, algorithm=JWT_ALGORITHM)
    # # return {"Token": token}
    #
    # # with sr.AudioFile(res) as source:
    # #     audio_text = r.listen(source)
    # #     text = r.recognize_google(audio_text)
    # #     return {"Token": token}


# app = FastAPI()
#
# class Base(BaseModel):
#     name : str
#     point : str
#     id_num : int
#
# async def checker(data: str = Form(...)):
#     try:
#         model = Base.parse_raw(data)
#     except ValidationError as e:
#         raise HTTPException(detail=jsonable_encoder(e.errors()), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
#     return model
#
# @app.post("/submit")
# async def submit(model: Base = Depends(checker), files : UploadFile = File(...)):
#         return {"JSON Payload ": model, "Filenames":files.filename}


if __name__ == "__main__":
    uvicorn.run("new_tes:app", port=8901, host='0.0.0.0', debug=True, reload=True)