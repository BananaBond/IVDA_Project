from src import app
from flask import Flask, flash, redirect, render_template, request, session, abort, g, url_for, jsonify
from flask_cors import CORS
# from functools import wraps
# from datetime import datetime
# from wtforms import Form, BooleanField, StringField, PasswordField, validators,TextAreaField,IntegerField
# import numpy as np
 


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
def index():

    return("Index")

    # return render_template('index.html')


@app.route("/endpoint", methods=["POST","GET"])
def submitData():

    #a = some_fn()
    a = [1, 2, 3]
    return jsonify(a)



@app.route('/getquery',methods=['POST','GET'])
def reservation():
#     form=ReservationForm(request.form)
#     if query_db("select firstname from Reservations where firstname = ?",( form.firstname.data,)):
#         if(query_db("select lastname from Reservations where lastname = ?",( form.lastname.data,))):
#
#             ("User already taken","danger")
#         return render_template("reservation.html",form=form)
#     if request.method == 'POST' and form.validate():
#         password = sha.encrypt(form.password.data)
#         execute_db("insert into Reservations values(?,?,?,?,?,?)", (form.firstname.data,form.lastname.data,form.email.data,form.time,form.seats.data,form.message.data,))
#         flash('Thanks for your reservation')
#         return redirect(url_for('index'))
    if request.method=="GET":
        return render_template('index.html',var_to_pass=var)
    else:
        submission ={}
        submission["var1"]=request.form["varname1"]
        submission["var2"]=request.form["varname2"]
        

    # Call functions here

    return render_template('index.html',var_to_pass=var)