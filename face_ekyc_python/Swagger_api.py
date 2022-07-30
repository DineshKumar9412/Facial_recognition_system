# from fastapi import Request, FastAPI, File, UploadFile,Depends,Form
# import uvicorn
# from pydantic import BaseModel
# import time
# from typing import Dict
# import jwt
# from decouple import config
# import speech_recognition as sr
# from pytz import timezone
# from datetime import datetime
#
# ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
#
# app = FastAPI()
#
# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")
#
# r = sr.Recognizer()
#
# class Info(BaseModel):
#     encounter_UUID : int
#     patient_UUID : int
#     doctor_UUID : int
#
# async def checker(data: str = Form(...)):
#     try:
#         model = Info.parse_raw(data)
#     except Exception as e:
#         return {"Success": "false", "Result": str(e)}
#     return model
#
# @app.post("/voice_to_text/")
# async def submit(model: Info = Depends(checker), files : UploadFile = File(...)):
#     dis = dict(model)
#     print(dis)
#     res = files.file
#     try:
#         token = jwt.encode(dis, JWT_SECRET, algorithm=JWT_ALGORITHM)
#         with sr.AudioFile(res) as source:
#             audio_text = r.listen(source)
#             with open(f'files/{token}{ind_time}.wav', 'wb') as file:
#                 file.write(audio_text.get_wav_data())
#             text = r.recognize_google(audio_text)
#             return {"Token ": token, "Text_value":text,"Path_location": "/home/troondxadmin/aimp/files/"}
#     except Exception as e:
#         return {"Success": "false", "Result": str(e)}
# if __name__ == "__main__":
#     uvicorn.run("Swagger_api:app", port=8009, host='0.0.0.0', debug=True, reload=True)

# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn
# from datetime import datetime
# from typing import List, Optional

# class Course(BaseModel):
#     # name: str
#     # description: Optional[str] = None
#     # price: int
#     # author: Optional[str] = None
#     id: int
#     username: str
#     password: str
#     confirm_password: str
#     alias = 'anonymous'
#     timestamp: Optional[datetime] = None
#     friends: List[int] = []
#
# app = FastAPI()
#
# @app.post("/ courses /")
# def create_course(course: Course):
#     return course
#
# if __name__ == "__main__":
#     uvicorn.run("Swagger_api:app", port=8901, host='0.0.0.0', debug=True, reload=True)


# from fastapi import Request, FastAPI
#
# app = FastAPI()
#
# @app.post("/dummypath")
# async def get_body(request: Request):
#     return request
# if __name__ == "__main__":
#     uvicorn.run("Swagger_api:app", port=8901, host='0.0.0.0', debug=True, reload=True)
#
#
# import shutil
# import requests
#
# url = '''https://healthidsbx.abdm.gov.in/api//v2/account/getPngCard' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
#   -H 'Authorization: Captcha_03AGdBq250gmgXQS6e-jCfe3YMs_gi-RyH97DJf_M6k8JbuH0mmanieUjG5HNjqEsuwtTCqBJkCz8OVsyN93nTMa1EZgMd97ie6pJOwC_2vhs4G68XsgiKWUICDqr3ayO72en875q-jtt6cCcVull5jimuBYC5S6FayuGzweB57Pw9H0u6uLMOwcxAe-L6IYz6B6_isI1mAj8JPw9ZXr-LpIc3jfWWrU2EFbXtfSGnAS4Cmtvt1rCcrA0quhJQqucO9nWaee-_ueVn-WtBMoNh6K_d-sxiyYRLhkadaXkgfB-7oXAJIBQ_0IIRUD4LXy314BMUG2MGqA76hrD3STOiuYRFsB5z7efF1TKKdafT34xHhhYIZlQ9b6sCaMI9zG4VQbx2tjRIlLRKGPT6QiqcZo4YfJtXSBMQuW--mg7fHg-7QZ7sQWE0UV6u0W4Oc-a_LfyDHvdNVDd3iRe9v-XrZSl-nA4JWfXFSBPNmH6m-efxmqzZJt3_AwGqOSp6Y8eRnfolFfcR2HGKAdINSABdnfpz0QHhId2CesYTj59bhbkPtbsXIuOMhclFqObBYH5PGbslGpgK-hQByZIQd1kPWKlN9eP9jR4-GuI9_i3aZGUyBqjPivyyOoTKRPc-Em-VqXhHNFr2bulo4VOK8Ms7QYF4aQnJxUAcYUyBDfh2Ka6dGEHtQBeh1FSHqDO5komhXNZE7cEIcz0eGX7Krd2SV98gr28bh-UtkJEyrtryB3wxx9DTGEEnIlRz6VrTlOHBNtjysOI_Y4TmZJWWWiEmLTYSZn-yvV9M1yRdZjyaP1_3tP1uCG2blEpbCy4WxVDd_9vv-w3XumTQeggLP8jRqhTebobayEu4SVxstxRvHwSaEfFuWQ4KROJqEMJgyRJ8F2lCgXT4BgOXZgZLMZ8cuGI6ZTHjdjYLVovCA3HgFYiCj7nqaePlos-tXGJb8VcNyAd8UfAf_lyyf2fzSobYnvCFKoUY-HsehUGrw6d_UMoATnJX0EQn6xhD07-70-4HZucdxjP_sXvR4eYmKi1Jnbw2ltt2GDk4lBVs6pLelNjrSD7ex8MLy2YLD71Q5gDozhYNZYGO-MQKOnmg8Unao8amPHRbM2hO8Btc995vQosNtp3UnarJRLudjyfQql15lW_kugTrQ24E9lcvlUieIJxRyjnbcRhlQEJL4Ph0MW8GNDc8LIZdpPnLcyeVq0mM7HFPb1Q7L-gcCYL-Qjzt4UFccTRRWr4U8PZs08WYIdrrh3dwWIxyAlLOJLKHsH5D54xkLm2ZLmRe6FyDLnLgbILui_Xr8M8xwp9wWfcTtQ8_4-236PBLzZA' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: TS01c078b5=01115a1c903ce4e4b47c5ab970b1f557db53508d4a96b7e701e434c58f8d01eddd28a31923ce276dd613248417d0b9bf996127edaf' \
#   -H 'Referer: https://healthidsbx.abdm.gov.in/account' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
#   -H 'X-Token: Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImNsaWVudElkIjoiaGVhbHRoaWQtYXBpIiwic3lzdGVtIjoiQUJIQS1OIiwibW9iaWxlIjoiOTU5NzI0NzgyNCIsImV4cCI6MTY1NDU4NzU2NiwiaGVhbHRoSWROdW1iZXIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImlhdCI6MTY1NDU4NTc2Nn0.aG-eyn1O7uZwgxTUVWODHZ2wIIQd4WSNBM3St4YwJs5RFtKh_G1DfIiwoWKqFVoroXSOsJyJRLm1HqxcOuZHMiDhu982B9hGv_Y0LsT3fkfT3Gyj9q1U0dhae66pe2hi2EyAzpD2ETTsPYaN1BO3qtct2pUKBoscJ7rlIFiS-Nc8QiXaNgljdWo6i3v6oUQRUz6UIpqdxZ5sxmeZAzoI4FsRL1Djw3QBJyE_eGndN1SfWlGiucNwEPde6diAApyY-zocVT3-o2XJ8aPhX7rpqSPVqmd2baOXkTbtSuUBfVjsDNKe1HiNFtOrtLCmcwDsInE2ekM2wYowCQpDANKkORhWC-8we1xwT3gUtXepGONTy2BQtVEaENYJrj3NtD6V-pmzU3x0zEf2-EVepOZimkMHDjcts9kMYoJkzTSpYqkc8x4Hf3EMaQJqaip_gZfGOKaFfh08VN5nT33UWxLiekwBgwPAduQAMf0Yeltp023SCFI7K-Rxj9fVghFvhVbM3L0xXNADVKUvsC2HqFCUsy2Qiy_2DxXHmFJJXnTjHm-JLWLOHwIFNs-vrAXTHMUO8oKjHH0Iv4bEKrq30C2fgDAjMbwU4rUkG8PTh0MIEHshkvgDAoe2mzzcdn8k47Il1IXGRaO3JV4Bs65sl61fZc9jBXGmjVQ3p-CPYfys66g' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   --compressed '''
# response = requests.get(url, stream=True)
#
# with open('sample.jpg', 'wb') as out_file:
#   shutil.copyfileobj(response.raw, out_file)
#
# print('The file was saved successfully')
#
# import io
# import requests
# from PIL import Image
#
# r = requests.get('''
#  'https://healthidsbx.abdm.gov.in/api//v2/account/getPngCard' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
#   -H 'Authorization: Captcha_03AGdBq27as1uF48iElRWPIHa_4NXCdCEEJulZrgIzqL3svd-THUtF7_o78eTcfIh7mJx04ZralucEF-gLBUSqf5H6cj27h2eqYh04fs1t3SQuUT4MFILvBrHV3u6yNiyqh_M6Gn730h7zKxc0-7J93nLi0gitnO16-n3WMP2X7a5_YSR0WgXQ0YIhCOHB8t42q8a1jP_7l2x4wrySsOqSqh9VGJAjjpOeQ7c4iFZjSMQUFkR84UVvvQC_UMz0SbqJJlI6M6HH1CFby221Gi4CSHb3dI7LCmb-geVJU_1fxRjMi8IYQGBcEWxdJnHz4RHDlg1pw0sjrSyJvlGCreQepAfmtrxMrs25_0czh53huFZBAVdxkjqz8vWiJ90Htwhvh6GG04M8DIFqHnVmL0EBOYBgy-0tzR91TrmeNvWVsOUVx-_9oAE3i40cyDQZkvV6mSyJYun2xFf2Acyr9EuDcemr5iq9xhKyRBboL3N0gzysuCXFVy5j4tQm4y76rY2oP2-cBpfDDbwQhiYpi9wAMNeL7TaY6CmXD4RIUzpE7OTE0k8xSU0ZHziP8RiTxsyYnbd2IRxVUzWUr6Xm9cB4wqqjxNcp4X2SVJogUt4JVweNRAgCc0bm8OqQXP1cbfSei4JPdWZGTx9jLtDMKMYWdHRTqodQLILVhqb_DUMkcIOTaczMaFf8RBNP7l-idXU68AstJ9q2qYokpIgKyw8seHcZqD7cKdSdQ01kn2lqxHjjOQSm7X-B7pM7VV9EZzDwjuZGyRoI-eNUgnKy4aSdNh9Fd_wKvD4R5dFk2AuCAZ432Jh0PAVHTQ6QjhGBYXPITZnexWEBFV2uXWHvq4rbnvWQa5v36rqT3gUBEBNVKLUBXz7rq3F_5mllJb2vu3CWehfpBOlu5-912j1bknyoEcB7FJCQ-rfOpOtqLeCkxBpxUG_kQ2bK-O1X2tqrkLBrlPnAv-rk5iWoeG2yq_X_4huHs_liY-UtlEFsBmfvcsnXGzXfudEbrUBFsYUTtnRfYjYfI2me6mHN2pVKEP1Kv8nHTGuMoggKjSIc6FD_YrlQu9G4u6pBA_4M6I9W0zHXea2F95QKhGvdX85vMgUulkg-dorBln8leJm7Admdz4964IgxZthZrVrhrakUyLonHosmZndQeslAZhQg_SscOm_eXlFSuyX1pghJ0LPr2QbD6YHz2mCnpDjlt91hCp2hRpw1XG4WxhLfsHHnU-06IEnFvXCyDW2wRMvSfDqm0vN1EZA95QEtXe7d4RiY4Hf9F1gt6EISuiOX_17qBcUbhYodAqKKNR15PZhHmpYoDekwwYFHJ1j47_s' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: TS01c078b5=01115a1c9050eaea2aa0ca558006750af1ee38a603425a2c73e9641ff21977bc45cb572f677c9c7272928053474537f4834d4b13f1' \
#   -H 'Referer: https://healthidsbx.abdm.gov.in/account' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
#   -H 'X-Token: Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImNsaWVudElkIjoiaGVhbHRoaWQtYXBpIiwic3lzdGVtIjoiQUJIQS1OIiwibW9iaWxlIjoiOTU5NzI0NzgyNCIsImV4cCI6MTY1NDU5MzA4OSwiaGVhbHRoSWROdW1iZXIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImlhdCI6MTY1NDU5MTI4OX0.ara0vjP7MosxsK49w9eK-_1mq28aMznnTCwK24JMjxpCvxnE8B0hLDwUoFYlzOXVhIGVtjJSqxZT3s3w96ov0tOuyrCrS072Rh920ngwPECNfcYQ8Yhes-HZTnJqllhLgQHp4GYrjWlET4IlQNbx-s-mHhIFFrHT3UOVqTsa0cHUV5w5Ogdrg45f_sf59lOJ0StcXOedbRgWq8K-pXbzRZzjVng9XGRyJ5TgDXZnpIEi_AnsoLs1x51gCiYUNpffzHE1TJpdJPY53w8N5ed8y7tkC4y4CUGdrH9tY5-xDhYVBr7KFaM0U_YirZyKY-Vx2xDxOEci2cGmdTa_FxsRrdWrYZeOpeh3ud5hRRrMBlcpSqIPmWuu50obZE2j48OCySca9sLUKnVl4R1zUtHyXET1qVmsT2ZB3VtRP0hgQ3uAWIlIfyn9fTWOVvKlNbr4YwL5Ndjk1XmaYbAVdQy1Q2b_XWbqJyCghjdP0Jo63V3x5nCbhA26h91rVy1KNOKfGwihAUWWNP8uyYPZUV17FdarIjZZE5fYGQ_uYtB9xuO2Jq8c3hmSVBaK5ny-VwhLSCBfQDNd8kPHShA8dtyPo1KTAS9qjnUH1lQfxbw5NDDLicAhtJmzVSxWcD-LuG2xz-Lmn7Qx2C5EJnzZOBJ8ylr_JYYQpOpZ8mZlNeeNBbA' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   --compressed
#  ''', stream=True)
# # aux_im = Image.open(io.BytesIO(r.content))
# print(r.status_code)
# import requests
# from requests.structures import CaseInsensitiveDict
#
# url = "https://healthidsbx.abdm.gov.in/api//v2/account/getPngCard"
#
# headers = CaseInsensitiveDict()
# headers["Accept"] = "*/*"
# headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
# headers["Authorization"] = "Captcha_03AGdBq27as1uF48iElRWPIHa_4NXCdCEEJulZrgIzqL3svd-THUtF7_o78eTcfIh7mJx04ZralucEF-gLBUSqf5H6cj27h2eqYh04fs1t3SQuUT4MFILvBrHV3u6yNiyqh_M6Gn730h7zKxc0-7J93nLi0gitnO16-n3WMP2X7a5_YSR0WgXQ0YIhCOHB8t42q8a1jP_7l2x4wrySsOqSqh9VGJAjjpOeQ7c4iFZjSMQUFkR84UVvvQC_UMz0SbqJJlI6M6HH1CFby221Gi4CSHb3dI7LCmb-geVJU_1fxRjMi8IYQGBcEWxdJnHz4RHDlg1pw0sjrSyJvlGCreQepAfmtrxMrs25_0czh53huFZBAVdxkjqz8vWiJ90Htwhvh6GG04M8DIFqHnVmL0EBOYBgy-0tzR91TrmeNvWVsOUVx-_9oAE3i40cyDQZkvV6mSyJYun2xFf2Acyr9EuDcemr5iq9xhKyRBboL3N0gzysuCXFVy5j4tQm4y76rY2oP2-cBpfDDbwQhiYpi9wAMNeL7TaY6CmXD4RIUzpE7OTE0k8xSU0ZHziP8RiTxsyYnbd2IRxVUzWUr6Xm9cB4wqqjxNcp4X2SVJogUt4JVweNRAgCc0bm8OqQXP1cbfSei4JPdWZGTx9jLtDMKMYWdHRTqodQLILVhqb_DUMkcIOTaczMaFf8RBNP7l-idXU68AstJ9q2qYokpIgKyw8seHcZqD7cKdSdQ01kn2lqxHjjOQSm7X-B7pM7VV9EZzDwjuZGyRoI-eNUgnKy4aSdNh9Fd_wKvD4R5dFk2AuCAZ432Jh0PAVHTQ6QjhGBYXPITZnexWEBFV2uXWHvq4rbnvWQa5v36rqT3gUBEBNVKLUBXz7rq3F_5mllJb2vu3CWehfpBOlu5-912j1bknyoEcB7FJCQ-rfOpOtqLeCkxBpxUG_kQ2bK-O1X2tqrkLBrlPnAv-rk5iWoeG2yq_X_4huHs_liY-UtlEFsBmfvcsnXGzXfudEbrUBFsYUTtnRfYjYfI2me6mHN2pVKEP1Kv8nHTGuMoggKjSIc6FD_YrlQu9G4u6pBA_4M6I9W0zHXea2F95QKhGvdX85vMgUulkg-dorBln8leJm7Admdz4964IgxZthZrVrhrakUyLonHosmZndQeslAZhQg_SscOm_eXlFSuyX1pghJ0LPr2QbD6YHz2mCnpDjlt91hCp2hRpw1XG4WxhLfsHHnU-06IEnFvXCyDW2wRMvSfDqm0vN1EZA95QEtXe7d4RiY4Hf9F1gt6EISuiOX_17qBcUbhYodAqKKNR15PZhHmpYoDekwwYFHJ1j47_s"
# headers["Connection"] = "keep-alive"
# headers["Cookie"] = "TS01c078b5=01115a1c9050eaea2aa0ca558006750af1ee38a603425a2c73e9641ff21977bc45cb572f677c9c7272928053474537f4834d4b13f1"
# headers["Referer"] = "https://healthidsbx.abdm.gov.in/account"
# headers["Sec-Fetch-Dest"] = "empty"
# headers["Sec-Fetch-Mode"] = "cors"
# headers["Sec-Fetch-Site"] = "same-origin"
# headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
# headers["X-Token"] = "Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImNsaWVudElkIjoiaGVhbHRoaWQtYXBpIiwic3lzdGVtIjoiQUJIQS1OIiwibW9iaWxlIjoiOTU5NzI0NzgyNCIsImV4cCI6MTY1NDU5MzA4OSwiaGVhbHRoSWROdW1iZXIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImlhdCI6MTY1NDU5MTI4OX0.ara0vjP7MosxsK49w9eK-_1mq28aMznnTCwK24JMjxpCvxnE8B0hLDwUoFYlzOXVhIGVtjJSqxZT3s3w96ov0tOuyrCrS072Rh920ngwPECNfcYQ8Yhes-HZTnJqllhLgQHp4GYrjWlET4IlQNbx-s-mHhIFFrHT3UOVqTsa0cHUV5w5Ogdrg45f_sf59lOJ0StcXOedbRgWq8K-pXbzRZzjVng9XGRyJ5TgDXZnpIEi_AnsoLs1x51gCiYUNpffzHE1TJpdJPY53w8N5ed8y7tkC4y4CUGdrH9tY5-xDhYVBr7KFaM0U_YirZyKY-Vx2xDxOEci2cGmdTa_FxsRrdWrYZeOpeh3ud5hRRrMBlcpSqIPmWuu50obZE2j48OCySca9sLUKnVl4R1zUtHyXET1qVmsT2ZB3VtRP0hgQ3uAWIlIfyn9fTWOVvKlNbr4YwL5Ndjk1XmaYbAVdQy1Q2b_XWbqJyCghjdP0Jo63V3x5nCbhA26h91rVy1KNOKfGwihAUWWNP8uyYPZUV17FdarIjZZE5fYGQ_uYtB9xuO2Jq8c3hmSVBaK5ny-VwhLSCBfQDNd8kPHShA8dtyPo1KTAS9qjnUH1lQfxbw5NDDLicAhtJmzVSxWcD-LuG2xz-Lmn7Qx2C5EJnzZOBJ8ylr_JYYQpOpZ8mZlNeeNBbA"
# headers["sec-ch-ua"] = "Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"
# headers["sec-ch-ua-mobile"] = "?0"
# headers["sec-ch-ua-platform"] = "macOS"
#
# resp = requests.get(url, headers=headers)
#
# print(resp.status_code)

# import requests
# import json
#
# word = """ curl 'https://healthidsbx.abdm.gov.in/api//v2/account/getPngCard' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
#   -H 'Authorization: Captcha_03AGdBq27TLVaW8kR8jAcCw8Ti9Z1EeV9JWXsxiFQhSO_nXcgH6uT5NWenm2IVUf5BqAqje1zyMI_7xlNehAxSEVVlN6kBA-M9_WtahBdT13tlYfEscwmB4juhiXSGQBpRU1G_kTBm-RoZ4RZEHT-i23abi6BUb245Le27EZl_kgz7j1ggIcmGU0HuBcR31B1TNIcHnoQjqrK3bvjr2zZvlfP5reKIv8XhtPyIv0zvHBYzzmUeh2DGeekdDgyULp_F7NRmtGXkuwf0eYs9dTUOGEOnN0dKh7bZwCD3f4BBIaYFd0gHAu_IDlk9f1zMqjLpK2ks-lwMMxmr8I7EZtiWEuqNDqyhSvwbX7Mzp3evmjyu6ekZ-75ByjVibyrC1kcKJR7Lmaf8lGnhVTa6T2vjg1_Ik_KZGucOYKY-GEs1e4Xh-dbxn6fE0Vgqp-vvmgUHu02fVBJhx5J9PADA1Ef_i7Fp_PVHbvm_V8A3YAZNkAUpElZrjcCIY92xTT18pzrxVdPG5DNYl4hAQ5Cq8FR-tt216Ao2yYdfkUDMfJ77qkAhEsf9rjMi--ZkGgf2MDBBb1mUSAbNuFl6b2Xc_Womb2UsehL4eRbKI4Dl5NS0LD8vNaDCQug2GJ5sOm2dM62oUxHuWZTTHSN59Fv2zY2zwlJ7mjk_v0M6KBpnEK1GjiIF43yiXmz4l8IcAbd_6VbHopuHA9u_AhDThZCrDu4i5s-fwO-P4cOQKx34yKTC-GfJT9jbN5x48IjKyjo6IulrxQVacJhWfne0tQtjs6LaGai51uMwybGlvX2BDebWeltbgwygGOo5ZOMUDQPPvkwUfZIPJGGJGzpV6XxxWhZ-HTVNtmD_03NNaFAiqfrkDde2juFhbbwlwpSk6SvRBP1TCuoH0Gth3c5vTPm7n40BYwffBewYJRXU7J_qOERUizatrhh7x9mERcLRI8zV6P_L9UTan5XBrogcemxXVqhI7enmUDHn_Jhna99RZW9yd9Weh0zSkx4wucwYRaSD28JKWRNhumXOG4Xsj2AaoPXpP9JP3aJBcRoKOuc1kQlk9bbBibgL7deiLZKbU4EisGXVfHdNCBaEJqJSi1XEzrJinuWbbzbBvRUqABkPavIEoxEyJ0aqB9D__0jYzV3f0HxoPkDFpDNhsLuSmrPnU7TMHFyAZ7OuD1m_fn2FF3ZLyzGDmDIMVwYYLrAZn314tOLJk880L1BxgARA6r8Nq5oxYG-PtR4Bi8sjbEdmEgp3xmm4RNya7nhYffWPHUOVXQwggECWTeQPsO4Lmd-ihSINapiOaZxt4VcLcnCN9XrlVuq2bg0jl1eDCb0' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: TS01c078b5=01115a1c90c97c4d008e1b999bcf49494971df5bea5ad4c05dcbe99cf5730b8b87f593001fc74c6f15a43d42f3b454ee1a58c6ae2e' \
#   -H 'Referer: https://healthidsbx.abdm.gov.in/account' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
#   -H 'X-Token: Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImNsaWVudElkIjoiaGVhbHRoaWQtYXBpIiwic3lzdGVtIjoiQUJIQS1OIiwibW9iaWxlIjoiOTU5NzI0NzgyNCIsImV4cCI6MTY1NDY2NjExNywiaGVhbHRoSWROdW1iZXIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImlhdCI6MTY1NDY2NDMxN30.FgDHBKUcy-BTlRrDPvi-siN3uIwVpj1suO2F4Ojg69S4IgWB0VfL_mVDpD0ZOyZZxhO1q_lF7_cOpKCpzxZfQ2Co8NcUZe6ZhchJ5_mShr9Yo-DSuJJ8v-ZbjLwFEwpYWxCTPJHrd3oLxYOHCEfASyCpbg0vAjtjojhfbeLOUl_QXKWMmNf4dDS44gGzEnVGPLBET2AMfloM5J6VZW3p_6P75Mrl9FV3XtjqJjY3_drZVBhUwRKVZhsOU6llFiAPoVGfQihVkQ98NFrTP2LSCfEH0JcvfK-I-SlaWODP-s4eqH64TyPe13_MHCAsxOtDggXtLKWQCQt85fW4iJaXCnLeZg2s3MbsUODZqH1F_Ivh69mhPd1L8Ga0CvwBIWqjZhjBlpwQgu4iYiq-uIOMqDUyfX_Kcdo2Zxd74jJ4PfBKKl0ob64-yn7HmWf9vedEp5KV8H_YORTpabbZOHmKys9_deDGsAF0GboQvW--d13hYP4jq30JNlTDiwZBmRS0hNszt3_EaraQPxcCfLV2Br3rBz3b8U3xeHOv3nDfsdj2PSxZs1m_y6iPhMszuQ48YJh3qSoPpfwIUuIuNYKgLhNfCDS7HjdYISrCSZ2aQkwXEfhe0O5oWnsQsgcoZUH5gskvuqu7T088ab277U6qL3Ln012s-Ho0HFHSy2I572w' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   --compressed"""
#
# words = word.split()
#
# cookies = words[9], words[10]
# print(cookies)

# cookies = {
#     'TS01c078b5': '01115a1c903523005468da65db1c8519c8b85174bb8e3d642380c28ea8c28aef9770e8f93e6caa0b9c6bd3a2a3c45427c9f6a976d6',
# }
#
# headers = {
#     'Accept': '*/*',
#     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     'Authorization': 'Captcha_03AGdBq26X5s2J9tBki7r7okWH7R194kYik2ZEQsLbPRiU_CKoyL8eHcEP2uBTXGhRBl_sebb0PkF8ddh1_NRcWJZjamhPbGCZCj3tYbtbbeh2OmPFjbvnWL0UlRMfBgG64MTimmMR_bEVG5ozAPEEvGd6ODouAmetHfZYANbXi-ihduHOq77LgxGq7CIq6dpGz-7CayKZnvlzFpNOAxh4arOiu8SZIOW81h1UUt1nuueKl8P2RqCUjhMCCpbfxJp8jxJpoAw7gotH4fd0HgzGZ6NEr_CMWTgo72Oy3v7bHon3WB9z_pxwua9KoN9BekCyK_VTKK7lxTVRVoK1uVr39ITw_Z5Ewsgw9ZN5JuzRF-p7A0-eVNZxlWsxa46Ie1t4AVWxL-PbupWEAwo2j3O6TA0WWKc4stUZ469_jp1g_3MlgsznsU4usdWMC2552F8bjD7jQAiFrGX23V56ftshfeeYHcbmBnrW7SuF9RBq3zK-qY8XYYZ0MJFXzqpSxJzTqI8VMhVdw1noyUrTtVJPWZgk4ilBJ0xWjqMrPcELE2gEdYKOixPOFDbK2b1ZOGslYEz8nQm2qHQezZ1JXf-8FiBqsD3ISRx1NxtadqMbcCC9hq35wlA1eWhYR32Sq4twrvrppUGmBFbr5SJkPb2YggF0vJU2oEfffDZMg3EOLg8_MRWSZLbQ1Mw4dspg5Ke0_Lk_bMXUJQ9bEANC1E9-YTNBZxKYffzF9AEXtL7GAzM-RnQJ2GIUQmH5Yx5qhyiOCtTEkXs_vhu9qsrtABKulofJuJQJB3SY_cifcgKhLcLNe5N85fTHB94zfiLHtXA7sQnhrrsXMU44MftP8h5rwfsNfAhCtELV2jeIIZDq8cM1FB8YyNfyUF2UojzTDGnTw7dg0QJ9SEV9O6OOm9-OqRAGIEcel28eX3rfYWFlDZktk4v-urvtVqdrhK58Eql5gE0IVbieWB6IKSqrAWtqTeWtuCzkUyt6enaJuhzfXV9XOMZYQywzbOUUinueHbYDFD8qKmGY8Vg97gWeldq63z-WIIjhNgjWO6CGUkrbOs-BLmXwnOFg1HIk7sAmSyoUIQfHV6hzPxQm4OJBIRHOjR31QQfPKEd1twJnZNHMbMZfjatKrJtQxDHBNMxRfEHRfGdps42O90fcWQO_AzUA9L8R_VK1PIcbrgLJKD31xeTf6gTUn608mMuJr5lA4l4DwwF5AHcx_oEL2sgX-AIv5ShrUCGszdYPsMGpDeItRwcLivQcyI_RyfoSKNxuSjDLUN8E5HPyiQuIxWp25i9uVBKXbYp_g6GMo3vrxi5woABXCQqcAPfAWfE',
#     'Connection': 'keep-alive',
#     'Referer': 'https://healthidsbx.abdm.gov.in/account',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
#     'X-Token': 'Bearer eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImNsaWVudElkIjoiaGVhbHRoaWQtYXBpIiwic3lzdGVtIjoiQUJIQS1OIiwibW9iaWxlIjoiOTU5NzI0NzgyNCIsImV4cCI6MTY1NDU5Njg0MywiaGVhbHRoSWROdW1iZXIiOiI2MC0wNTEwLTE1NDYtNjAyMiIsImlhdCI6MTY1NDU5NTA0M30.fXwTfePMyvBCxMeoEwrDpG_iPw__r6EaIUzvswZKuGEgHtC6NLxhScZtfvjjub5jGygsHRA6pP8FHScMYJUCq8TAv9h1ON1X-jNJfM63qCaT2eGnV4Rxo8DJsKPOcAiuiEfkVhOiJ2vgQPKxxQjINSYYNMoN8de5iZD5TkQ7tmQMBwFNtrXboIbKRZNntozHHNEVPG176Nr0wy350UhqJxF0nMh1L1qZRL4z8pDCRw8hOMOKMJaEQUMIs_UzmnsA__cjNAf40sy9bRgu03H23cSZMOQGiYyPUv_I_ginlEaI23g_SmN2hwrfsG9ETEhGQ6bmyhkeKkGFaBPF2AS_V62SfIxOkA98Jljm3SLhndlAluWZNF_X2A9b6EyaXgUxtevOkg6VA4er5BG5og3y2vTBD0grHq9eEU8Nx5dSAqgk2REmKODleZgg69uoadWNDNcwoq9fAj9gsC-IjRY8AkiPVEY9OksZFUwda6fRBK-aeC_Au5QTUisS5BXOtPD_QE5p5AIejduhFTJnhmOhLn07R7MlbJrSwiF_7Sc1naQpa0giJt7ibC8OtaiLKkoVlq_XCOPApoLu6QR7k3SvkqGCO0HtiQ8rnKql4i9N3cSjurhpv1qESQhYf2hK74Q1YO7uI8tMz-PRMdhZfdSaLjV7_zatdagJNf-gAAgRyZw',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
# }
#
# response = requests.get('https://healthidsbx.abdm.gov.in/api//v2/account/getPngCard', headers=headers, cookies=cookies)
#
# with open(r'file_name.png', 'wb') as f:
#     f.write(response.content)

# from datetime import datetime
# from pytz import timezone
#
# ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
# print(ind_time)