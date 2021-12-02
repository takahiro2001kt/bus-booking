from flask import Flask
from flask import render_template,request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import random
import smtplib
from email.mime.text import MIMEText


cred = credentials.Certificate(path to firebase-authorization-json)
firebase_admin.initialize_app(cred)
db = firestore.client() # 初期化

app = Flask(__name__)

# index.htmlを開く
@app.route("/", methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route("/complete",methods=['POST','GET'])
def complete():
    add_DB()
    send_mail()
    return render_template("complete.html")


# 変数、リスト等の設定
bace_seat = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8"] #全座席情報
get_seat = [] # 現在埋まっているシート

    # ドキュメントの要素数をカウントするコード
doc_ref = db.collection(u"tokyo-osaka")
user_info = doc_ref.get()
num = len(user_info) + 1

def add_DB(): # 座席の指定 & DBへの登録

    # 現在の座席状況の取得
    for i in range(num):
        doc_ref = db.collection(u'tokyo-osaka').document(str(i + 1))
        doc = doc_ref.get().to_dict()

    # 空席の作成
    vavant_seat = list(set(bace_seat) - set(get_seat))
    seat = random.choice(vavant_seat)

    # HTMLの入力データを追加追加処理
    doc_ref = db.collection(u'tokyo-osaka').document(str(num))
    doc_ref.set({
        u'name_L': request.args["name_L"],
        u'name_F': request.args["name_F"],
        u'gender': request.args["gender"],
        u'address': request.args["address"],
        u'tel': request.args["tel"],
        u'mail': request.args["mail"],
        u'checkin': "",
        u'boarding': "",
        u'seat': seat
    })


def send_mail():
    # SMTP認証情報
    account = mail_Account
    password = password
    
    # 送受信先
    to_email = request.args["mail"]
    from_email = mail_Account
    
    # MIMEの作成
    subject = "予約完了"
    message = f"""
    {request.args["name_L"]}様\n

    高速バスの予約を受け付けました。\n
    確認用のQRコードを出発１時間前に送付します。\n
    乗車日にバス停までお持ちください。
    予約番号は「{num}」
    
    """
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email
    
    # メール送信処理
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(account, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
