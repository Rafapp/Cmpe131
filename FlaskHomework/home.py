from flask import Flask, render_template_string

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
    name = ""
    city_names = []
    html_code =  """
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Welcome {{name}}</h1>
            <a href = "https://www.google.com">not google</a>
            {% for city in city_names %}
            <ul>
                <li>city</li>
            </ul>
            {% endfor %}
        </body>
    </html>"""
    return render_template_string(html_code, name=name, city_names=city_names)


myapp_obj.run()
