import matplotlib
matplotlib.use('agg')
import pandas as pd
from bottle import Bottle

app = Bottle()

@app.route('/index')
def index():
    title = 'Hello World'
    plot = 'plot placeholder'
    footer = 'created fron an android device using Termux'
    html = f'''<h1> {title} </h1>
             <br>
             {plot}
             <br>
             {footer}'''
    return html


if __name__ == '__main__':
    app.run()
