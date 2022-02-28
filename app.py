from flask import Flask, render_template, request, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
import urllib.request, json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changethislater'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///theDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class axie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    axie_text = db.Column(db.String(100), index = True)

db.create_all()

class axieForm(FlaskForm):
    axie = StringField("Axie ID")
    submit = SubmitField('Add ID')

@app.route('/', methods=('GET', 'POST'))
def index():
    #get_axie_info()
    if 'axie' in request.form:
        db.session.add(axie(axie_text = request.form['axie']))
        db.session.commit()
    return render_template('index.html', axie=axie.query.all(), template_form=axieForm())

@app.route('/axieinfo')
def get_axie_info():
    
    url = "https://graphql-gateway.axieinfinity.com/graphql={}".format(os.environ.get("AXIE_API_KEY"))
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("index.html", axies=dict["results"])

if __name__ == "__main__":
    app.run(debug=True)
'''

# for base.html<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}"> #
# last text for index.html : 

{% extends 'base.html' %}

{% block content %}
    <h1>{% block title %} Axie Breeding Recommendations {% endblock %}</h1>
    <form method="post">
        <label for="title">Axie ID</label>
        <br>
        <input type="text" name="title"
               placeholder="Axie ID"
               value="{{ request.form['title'] }}"></input>
        <br>
        <button type="submit">Submit</button>
    </form>

{% endblock %}

'''