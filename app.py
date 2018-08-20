"""
Hidinetwork landing page temporary app
"""
import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """
    Landing page home
    :return: html
    """
    return render_template('index.html')

@app.route('/privacy',methods=['GET'])
def privacy_route():
    return render_template('privacy.html')

@app.errorhandler(404)
def not_found(e):
    """
    404 not found page
    :return: html
    """
    return render_template('404.html'), 404



#@app.route('/favicon.ico')
#def favicon():
#    return send_from_directory(os.path.join(app.root_path, 'static'),
#                          'favicon.ico',mimetype='image/x-icon')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)), debug=True)
