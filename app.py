from flask import Flask, flash, redirect, render_template, request, url_for
from pprint import pprint as pp
from weather import query_api


#From: https://medium.com/free-code-camp/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221
#Server that routs the users to the homepage
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Oslo'},
              {'name':'Trondheim'},
              {'name':'Bergen'},
              {'name':'Stavanger'},
              {'name':'Tønsberg'},]
    )



@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True)
