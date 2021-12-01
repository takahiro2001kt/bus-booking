from flask import Flask
from flask import render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.Certificate(path to firebase-authorization-json))
firebase_admin.initialize_app(cred)
db = firestore.client() # 初期化

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",seat_A1 = seat_A1,seat_A2 = seat_A2, seat_A3 = seat_A3, seat_A4 = seat_A4,seat_A5 = seat_A5,seat_A6 = seat_A6,seat_A7 = seat_A7,seat_A8 = seat_A8,seat_B1 = seat_B1,seat_B2 = seat_B2,seat_B3 = seat_B3,seat_B4 = seat_B4,seat_B5 = seat_B5,seat_B6 = seat_B6,seat_B7 = seat_B7,seat_B8 = seat_B8,seat_C1 = seat_C1,seat_C2 = seat_C2,seat_C3 = seat_C3,seat_C4 = seat_C4,seat_C5 = seat_C5,seat_C6 = seat_C6,seat_C7 = seat_C7,seat_C8 = seat_C8)

"""
1,2３の番号でseatとボーディングの値をとってくる、それを辞書で格納
あとは比較処理
"""

doc_ref = db.collection(u"tokyo-osaka")
user_info = doc_ref.get()
num = len(user_info)

seat_info_dic = {}

# {A1:"ok"}形式を作成する。　後のコードを簡潔にするために
for i in range(num):
    doc_ref = db.collection(u'tokyo-osaka').document(str(i + 1))
    doc = doc_ref.get().to_dict()
    seat_info_dic.update({doc["seat"]:doc["boarding"]}) # {A1:"ok"}形式

print(seat_info_dic)



###
#A列
###

try:
    seat_A1 = seat_info_dic["A1"]
except KeyError:
    seat_A1 = None

try:
    seat_A2 = seat_info_dic["A2"]
except KeyError:
    seat_A2 = None

try:
    seat_A3 = seat_info_dic["A3"]
except KeyError:
    seat_A3 = None

try:
    seat_A4 = seat_info_dic["A4"]
except KeyError:
    seat_A4 = None

try:
    seat_A5 = seat_info_dic["A5"]
except KeyError:
    seat_A5 = None

try:
    seat_A6 = seat_info_dic["A6"]
except KeyError:
    seat_A6 = None

try:
    seat_A7 = seat_info_dic["A7"]
except KeyError:
    seat_A7 = None

try:
    seat_A8 = seat_info_dic["A8"]
except KeyError:
    seat_A8 = None

###
#B列
###

try:
    seat_B1 = seat_info_dic["B1"]
except KeyError:
    seat_B1 = None

try:
    seat_B2 = seat_info_dic["B2"]
except KeyError:
    seat_B2 = None

try:
    seat_B3 = seat_info_dic["B3"]
except KeyError:
    seat_B3 = None

try:
    seat_B4 = seat_info_dic["B4"]
except KeyError:
    seat_B4 = None

try:
    seat_B5 = seat_info_dic["B5"]
except KeyError:
    seat_B5 = None

try:
    seat_B6 = seat_info_dic["B6"]
except KeyError:
    seat_B6 = None

try:
    seat_B7 = seat_info_dic["B7"]
except KeyError:
    seat_B7 = None

try:
    seat_B8 = seat_info_dic["B8"]
except KeyError:
    seat_B8 = None

###
#C列
###

try:
    seat_C1 = seat_info_dic["C1"]
except KeyError:
    seat_C1 = None

try:
    seat_C2 = seat_info_dic["C2"]
except KeyError:
    seat_C2 = None

try:
    seat_C3 = seat_info_dic["C3"]
except KeyError:
    seat_C3 = None

try:
    seat_C4 = seat_info_dic["C4"]
except KeyError:
    seat_C4 = None

try:
    seat_C5 = seat_info_dic["C5"]
except KeyError:
    seat_C5 = None

try:
    seat_C6 = seat_info_dic["C6"]
except KeyError:
    seat_C6 = None

try:
    seat_C7 = seat_info_dic["C7"]
except KeyError:
    seat_C7 = None

try:
    seat_C8 = seat_info_dic["C8"]
except KeyError:
    seat_C8 = None

###
#D列
###

# try:
#     seat_D1 = seat_info_dic["D1"]
# except KeyError:
#     seat_D1 = None

# try:
#     seat_D2 = seat_info_dic["D2"]
# except KeyError:
#     seat_D2 = None

# try:
#     seat_D3 = seat_info_dic["D3"]
# except KeyError:
#     seat_D3 = None

# try:
#     seat_D4 = seat_info_dic["D4"]
# except KeyError:
#     seat_D4 = None

# try:
#     seat_D5 = seat_info_dic["D5"]
# except KeyError:
#     seat_D5 = None

# try:
#     seat_D6 = seat_info_dic["D6"]
# except KeyError:
#     seat_D6 = None

# try:
#     seat_D7 = seat_info_dic["D7"]
# except KeyError:
#     seat_D7 = None

# try:
#     seat_D8 = seat_info_dic["D8"]
# except KeyError:
#     seat_D8 = None

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True, port=5000)