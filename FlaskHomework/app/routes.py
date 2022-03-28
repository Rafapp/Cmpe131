from app import myapp_obj
from flask import render_template,flash,request

@myapp_obj.route('/', methods=['POST', 'GET'])
def home():
    name = ''
    city_names = []
    text = ''
    if(request.form):
        text = request.form['cityName']
    flash(text)
    return render_template('home.html', name=name, city_names=city_names)