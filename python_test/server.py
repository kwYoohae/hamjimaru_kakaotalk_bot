
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename #버전 변경으로 이렇게 사용

app = Flask(__name__) 

@app.route("/")
def hello(): 
    return "Hello Flask!!!!!!!"

@app.route("/upload")
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if os.path.isfile('./TodayPicture/TodayMenu.png') == True:
            os.remove(r'./TodayPicture/TodayMenu.png')
        f.save('./TodayPicture/TodayMenu.' + secure_filename(f.filename))
        return '파일 업로드 성공'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True) # 서버 설정 그대로 놔둘것
