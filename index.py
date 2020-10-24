from flask import Flask,jsonify,request,render_template



information = {"result" : 0}
app = Flask(__name__)
@app.route("/api/calc",methods=["GET"])
@app.route("/",methods=["GET"])
def start():
	x = int(request.args["x"])
	y = int(request.args["y"])
	print(type(x))
	information["result"] = x*y
	print(request.args)

	return jsonify(information)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
