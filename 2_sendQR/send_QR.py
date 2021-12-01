# 手順イメージ
#１、シートから番号を取得し、QRを生成し、保存する
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import qrcode
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageDraw


cred = credentials.Certificate(path to firebase-authorization-json)
firebase_admin.initialize_app(cred)
db = firestore.client() # 初期化

mail_list = [] #送信するメールリスト
# ドキュメントの要素数をカウントするコード
doc_ref = db.collection(u"tokyo-osaka")
user_info = doc_ref.get()
num = len(user_info)

for i in range(num):
    doc_ref = db.collection(u'tokyo-osaka').document(str(i + 1))
    doc = doc_ref.get().to_dict()
    mail_list.append(doc["mail"])

counter = 0
for j,k in enumerate(mail_list):
    img = qrcode.make(j + 1)
    img.save(f"write path/{j + 1}.png") #パスを書く
    # 以下メール送信
    stmp_server = "smtp.gmail.com"
    stmp_port = 587
    stmp_user = mail_Account
    stmp_password = password

    to_address = mail_list[counter]
    from_address = stmp_user
    subject = "【出発1時間前】高速バス乗車確認"
    body = f"""
    <html>
        <body>
            <h1>予約確認です。</h1>
            <p>予約された高速バス出発１時間前となりました。乗車用のQRコードを添付しました。認証端末にかざし、チェックイン処理を行なってください。</p>
            あなたの予約番号は「{j + 1}」
        </body>
    </html>"""

    filepath = f"write_file_path/{j + 1}.png"
    filename = os.path.basename(filepath)

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to_address
    msg.attach(MIMEText(body, "html"))

    with open(filepath, "rb") as f:
        mb = MIMEApplication(f.read())

    mb.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(mb)

    s = smtplib.SMTP(stmp_server, stmp_port)
    s.starttls()
    s.login(stmp_user, stmp_password)
    s.sendmail(from_address, to_address, msg.as_string())
    s.quit()

    print(f"{j}.Eメールを送信しました。")
    counter += 1