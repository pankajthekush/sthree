from flask import Flask,request,jsonify,render_template
from sthree import return_resource


app = Flask(__name__, template_folder='templates')

@app.route('/s3')
def hello_world():
    fname = request.args['surl']
    return jsonify(return_resource(fname))


if __name__ == '__main__':
    app.run()