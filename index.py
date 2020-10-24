from flask import Flask,jsonify,request,render_template



information = {"result" : 0}
app = Flask(__name__)
@app.route("/api/calc",methods=["GET"])
def start():
	x = int(request.args["x"])
	y = int(request.args["y"])
	information["result"] = x*y
	return jsonify(information)

@app.route("/",methods=["GET"])
def end():
    x = int(request.args["x"])
    y = int(request.args["y"])
    information["result"] = x*y
    return jsonify(information)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
