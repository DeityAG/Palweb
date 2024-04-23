# pip install -r requirements.txt
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/manipal')
def manipal_page():
    return render_template('Manipal_page.html')

@app.route('/kiit')
def kiit_page():
    return render_template('landing_KIIT.html')

@app.route('/vit')
def vit_page():
    return render_template('landing_VIT.html')

@app.route('/Forum.html')
def forum_page():
    return render_template('Forum.html')

@app.route('/Important_link')
def important_link_page():
    return render_template('Important_link.html')

@app.route('/map.html')
def map_page():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
