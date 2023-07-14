from flask import Flask
from pyfiglet import Figlet

'''banner_server main program

usage:
    python3 main.py
'''

# 参考: https://qiita.com/tommy_aka_jps/items/4cd675e3bea4c2632d4d
figlet_standard = Figlet(font='standard')
figlet_banner = Figlet(font='banner')
figlet_block = Figlet(font='block')
figlet_slant = Figlet(font='slant')
figlet_fuzzy = Figlet(font='fuzzy')

app = Flask(__name__)
header = {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/')
def _hello():
    return figlet_slant.renderText('Hello World!'), 200, header

@app.route('/<text>')
def _standard(text: str):
    return figlet_standard.renderText(text), 200, header

@app.route('/banner/<text>')
def _banner(text: str):
    return figlet_banner.renderText(text), 200, header

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
