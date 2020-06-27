from flask import Flask, request,  Response
from LogisticRegression.LogisticRegression import predObj


app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is  :', data)
            pred = predObj()
            res = pred.predict_log(data)
            print('result is :',res)
            return Response(res)
    except ValueError:
        return Response("Value is not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)


if __name__ == '__main__':
    app.run(debug = True)