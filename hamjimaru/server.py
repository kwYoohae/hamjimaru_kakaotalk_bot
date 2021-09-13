from flask import Flask, json, request, jsonify
import sys
import os
import datetime
import pandas as pd

app = Flask(__name__)

menuData = pd.read_csv("./table.csv", header=None, encoding="utf=8")

def get_img_content(coding='utf-8'):
    with open('./TodayPicture/TodayMenu.png', 'rb') as f:
        img_data = base64.b64encode(f.read()).decode(coding)
        return img_data


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        'type': 'buttons',
        'buttons': ['아무것도아님']
    }
    return jsonify(dataSend)

@app.route('/test', methods=['GET'])
def Test():
    return "hello"

@app.route('/message', methods=['POST'])
def Message():
    req = request.get_json()
    content = req["userRequest"]["utterance"]
    content = content.replace("\n", "")
    print(content)
    id_value = req["userRequest"]["user"]["id"]
    block_value = req["userRequest"]["block"]["id"]
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    price = "가격은 점심 : 5,500원\n천원의 밥상 : 1,000원";
    dayweek = datetime.datetime.today().weekday()
    # print(content)
    if content == "월요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[0][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "화요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[1][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "수요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[2][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "목요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[3][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "금요일 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": day_weeks,
                                    "description": menuData[4][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "얼마야?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "가격정보",
                                    "description": price
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "내일의 메뉴":
        day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
        if dayweek + 1 >= 6:
            dataSend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "carousel": {
                                "type": "basicCard",
                                "items": [
                                    {
                                        "title": day_weeks,
                                        "description": "안뇨오옹"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
    elif content == "오늘 밥은?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": "메뉴를 눌러주세요"
                    }
                }],
                "quickReplies": [
                    {
                        "action": "message",
                        "label": "월요일 메뉴",
                        "messageText": "월요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "화요일 메뉴",
                        "messageText": "화요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "수요일 메뉴",
                        "messageText": "수요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "목요일 메뉴",
                        "messageText": "목요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "금요일 메뉴",
                        "messageText": "금요일 메뉴"
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "잘못된 입력입니다. 메뉴가 궁금하시면 다음버튼을 눌러주세요"
                        }
                    }],
                "quickReplies": [
                    {
                        "action": "message",
                        "label": "오늘 밥은?",
                        "messageText": "오늘 밥은?"
                    },
                    {
                        "action": "message",
                        "label": "얼마야?",
                        "messageText": "얼마야?"
                    }
                ],
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)