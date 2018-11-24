#-*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request, Response, jsonify
from flask import send_from_directory
import os
import Ransomwhere

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/analysis', methods=['POST'])
def analysis():
    f = request.files['enc_file']
    info = Ransomwhere.Analysis(f)
    info.analysis()
    return render_template('result.html', result=info.get())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88)