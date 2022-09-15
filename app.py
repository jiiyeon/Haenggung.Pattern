import os, sys
from flask import Flask, escape, request,  Response, g, make_response
from flask.templating import render_template
 
app = Flask(__name__)

def root_path():
	'''root 경로 유지'''
	real_path = os.path.dirname(os.path.realpath(__file__))
	sub_path = "\\".join(real_path.split("\\")[:-1])
	return os.chdir(sub_path)

# Main page
@app.route('/')
def index():
    return render_template('index.html')

#post_text
@app.route('/text_post', methods=['GET','POST'])
def text_post():
    if request.method == 'POST':
        root_path()

    user_text = request.args.get('user_text')
    return user_text

 
if __name__== "__main__":
    app.run()
