from flask import Flask, json, request, jsonify
import sys

app = Flask(__name__)

master_id = "118b05554dedc5781be3004fe1543e75c7f1058ee91418b6084955eff65ab71f79"
message_block = "60d5e0792649813b4a32ec9a"

@app.route('/keyboard')
def Keyboard():
	dataSend = {

	}
	return jsonify(dataSend)
        
@app.route('/message', methods=['POST'])
def Message():
	req = request.get_json()
	content = req["userRequest"]["utterance"]
	content=content.replace("\n","")
	id_value = req["userRequest"]["user"]["id"]
	block_value = req["userRequest"]["block"]["id"]
	answer_value = req["action"]["detailParams"]["answer_list"]["value"]
	print(answer_value)
	print(req["userRequest"]["utterance"])
	print(id_value)
	print(block_value)
	if content == "오늘의 메뉴":
		day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
		dataSend = {
			"version" : "2.0",
			"template" : {
				"outputs" : [
					{
						"carousel" : {
							"type" : "basicCard",
							"items" : [
							{
								"title" : day_weeks ,
								"description": "안뇨오옹"
							}
						]
						}
					}
				]
			}
		}
	elif content  == "이미지 업로드" and master_id == id_value: 
		dataSend = {
			"version" : "2.0",
			"template" : {
				"outputs" : [
				{
					"simpleText" : {
						"text" : "이미지업로드 승인!!"
						}
					}
				]
			}
		}
	elif content == "명령어":
		dataSend = {
			"version" : "2.0",
			"template" : {
				"outputs" :[{
					"simpleText":{
						"text" : "메뉴를 눌러주세요"
					}
				}],
				"quickReplies" : [
					{
						"action" : "message",
						"label" : "오늘의 메뉴",
						"messageText" : "메뉴"
					}
				]
			}
		}
	else:
		dataSend = {
			"version" : "2.0",
			"template" : {
				"outputs" : [
					{
						"simpleText" : {
							"text" : "error입니다."
						}
					}
				]
			}
		}
	return jsonify(dataSend)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)
