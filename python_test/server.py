import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename #버전 변경으로 이렇게 사용

app = Flask(__name__) 

@app.route("/")# '/' route 기본 화면
def Hello():
    return "Hello!"

@app.route("/keyboard")                        #버튼 지정
def keyboard(): 
    dataSend = {    
        "type" : "buttons",     
        "buttons" : ["오늘의 메뉴" , "도움말"]
    }
    print(dataSend)
    print("\n")
    print(jsonify(dataSend))
    return jsonify(dataSend)


@app.route("/message", methods = ['POST','GET'])
def Message():
    dataRecieve = request.get_json()
    print(dataRecieve)
    user_input = dataRecieve["content"]
    if user_input == u"오늘의 메뉴":            # prefix 'u'는 unicode문자열 변환
         dataSend = {
            "message":{
                "text" : "오늘의 메뉴입니다.....\n"         #해당 위치에 크롤링한 내용을 출력한다
            },
            "keyboard":{                        # 버튼 재지정
                "type" : "buttons",
                "buttons" : ["오늘의 메뉴" , "도움말"]
            }
        }
    elif user_input == u"도움말":
        dataSend = {
            "message":{
                "text" : "도움말입니다.\n"
            },
            "keyboard":{
                "type" : "buttons",
                "buttons" : ["오늘의 메뉴" , "도움말"]
            }
        }
    return jsonify(dataSend)


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
