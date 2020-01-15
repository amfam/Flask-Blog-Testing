from flask import Flask,render_template

app = Flask(__name__)

posts=[
    {'author':'fane duo',
    'title':'232',
    'content':'DSDSDdnask',
    'date posted':'12'},

    {'author':'jane duo',
    'title':'djsjd',
    'content':'sdnask',
    'date posted':'25'}

]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)
@app.route('/about')
def about():
    return render_template('about.html',title ='About')  


if __name__ == '__main__':
    app.run(debug=True)
