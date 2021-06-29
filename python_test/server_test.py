from flask import Flask, json, request, jsonify
import sys

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
	dataSend = {

	}
	return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
	req = request.get_json()
	content = req["action"]["detailParams"]["menu"]["value"]
	content=content.replace("\n","")
	day_weeks = req["action"]["detailParams"]["day_of_the_week"]["value"]
	print(content)
	print(day_weeks)
	if content == "오늘의 메뉴":
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
