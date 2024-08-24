from flask import Flask, render_template, request, flash, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db
import os
app = Flask(__name__)
app.secret_key = 'your_secret_key'

file_path = os.path.join(os.path.dirname(__file__), 'fb.json')
# Initialize Firebase app with service account credentials
cred = credentials.Certificate(file_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://v-thuvien-default-rtdb.asia-southeast1.firebasedatabase.app/m/'
})

# Define database reference, the name of database
db_ref = db.reference('users')

#register route
@app.route('/index1', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = db_ref.get()

        for user_id in users:
            user_data = users[user_id]
            if user_data['email'] == email and user_data['password'] == password:
                return render_template('index1.html', message='the account exists, try another email please')
            elif user_data['email'] == email and user_data['password'] != password:
                return render_template('index1.html', message = 'the account exists, try another email please')
        #if none of the condition above fulfill, the below block will send user's info to the database    
        new_user_ref = db_ref.push()
        new_user_ref.set({
            'email': email,
            'password': password
        })    
        return render_template('xin-chao copy1.html')           
    return render_template('index1.html')            

@app.route('/index', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        mail = request.form['login_email']
        password = request.form['login_password']

        users = db_ref.get()

        for user_id in users:
            user_data = users[user_id]
            if user_data['email'] == mail and user_data['password'] == password:
                return render_template("trang-chu.html")
            
        flash("Mật khẩu hoặc email sai, hãy thử lại", "error")
        return redirect(url_for("login")) #return to the function login
            
    return render_template('index.html')
#lounge route
@app.route('/')
def home():
    return render_template('xin-chao copy1.html')

@app.route('/trang-chu')
def dashboard():
    return render_template('trang-chu.html')

@app.route('/thu-vien')
def thu_vien():
    return render_template('thu-vien.html')

@app.route('/sach-giao-khoa')
def sgk():
    return render_template('sach-giao-khoa.html')

@app.route('/sach-bai-tap')
def sbt():
    return render_template('sach-bai-tap.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/ve-chung-toi')
def about_us():
    return render_template('ve-chung-toi.html')

@app.route('/ket-noi-tri-thuc')
def kntt():
    return render_template('ket-noi-tri-thuc-lop-update.html')

@app.route('/ket-noi-tri-thuc-bt')
def kntt_bt():
    return render_template('ket-noi-tri-thuc-bt.html')

@app.route('/chan-troi-sang-tao')
def ctst():
    return render_template('chan-troi-sang-tao-lop-update.html')

@app.route('/canh-dieu')
def kite():
    return render_template('canh-dieu-lop-update.html')

@app.route('/sach-truyen')
def comics():
    return render_template('sach-truyen.html')

@app.route('/truyen-tranh')
def comics_2():
    return render_template('truyen-tranh.html')

@app.route('/sach-hoc-thuat')    
def sht():
    return render_template('sach-hoc-thuat.html')

@app.route('/video-vat-ly')
def physics():
    return render_template('video-vat-ly.html')

@app.route('/ket-noi-tri-thuc-lop-1')
def kntt1():
    return render_template('ket-noi-tri-thuc-lop-1.html')

@app.route('/ket-noi-tri-thuc-lop-2')
def kntt2():
    return render_template('ket-noi-tri-thuc-lop-2.html')

@app.route('/ket-noi-tri-thuc-lop-3')
def kntt3():
    return render_template('ket-noi-tri-thuc-lop-3.html')

@app.route('/ket-noi-tri-thuc-lop-4')
def kntt4():
    return render_template('ket-noi-tri-thuc-lop-4.html')

@app.route('/ket-noi-tri-thuc-lop-4-bt')
def kntt4_bt():
    return render_template('ket-noi-tri-thuc-lop-4-bt.html')

@app.route('/ket-noi-tri-thuc-lop-6')
def kntt6():
    return render_template('ket-noi-tri-thuc-lop-6.html')

@app.route('/ket-noi-tri-thuc-lop-7')
def kntt7():
    return render_template('ket-noi-tri-thuc-lop-7.html')

@app.route('/ket-noi-tri-thuc-lop-8')
def kntt8():
    return render_template('ket-noi-tri-thuc-lop-8.html')

@app.route('/bo-giao-duc-9')
def bgd9():
    return render_template('lop-9.html')

@app.route('/bo-giao-duc-5')
def bgd5():
    return render_template('lop-5.html')

@app.route('/canh-dieu-lop-1')
def kite1():
    return render_template('canh-dieu-lop-1.html')

@app.route('/canh-dieu-lop-2')
def kite2():
    return render_template('canh-dieu-lop-2.html')

@app.route('/canh-dieu-lop-3')
def kite3():
    return render_template('canh-dieu-lop-3.html')

@app.route('/canh-dieu-lop-4')
def kite4():
    return render_template('canh-dieu-lop-4.html')

@app.route('/canh-dieu-lop-6')
def kite6():
    return render_template('canh-dieu-lop-6.html')

@app.route('/canh-dieu-lop-7')
def kite7():
    return render_template('canh-dieu-lop-7.html')

@app.route('/canh-dieu-lop-8')
def kite8():
    return render_template('canh-dieu-lop-8.html')

@app.route('/chan-troi-sang-tao-lop-1')
def ctst1():
    return render_template('chan-troi-sang-tao-lop-1.html')

@app.route('/chan-troi-sang-tao-lop-2')
def ctst2():
    return render_template('chan-troi-sang-tao-lop-2.html')

@app.route('/chan-troi-sang-tao-lop-3')
def ctst3():
    return render_template('chan-troi-sang-tao-lop-3.html')

@app.route('/chan-troi-sang-tao-lop-4')
def ctst4():
    return render_template('chan-troi-sang-tao-lop-4.html')

@app.route('/chan-troi-sang-tao-lop-6')
def ctst6():
    return render_template('chan-troi-sang-tao-lop-6.html')

@app.route('/chan-troi-sang-tao-lop-7')
def ctst7():
    return render_template('chan-troi-sang-tao-lop-7.html')

@app.route('/chan-troi-sang-tao-lop-8')
def ctst8():
    return render_template('chan-troi-sang-tao-lop-8.html')

if __name__ == '__main__':
    app.run(debug=True)
