from flask import *
from pytube import YouTube
import dld
import random

app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def download():
  link = request.form["linky"]
  file = dld.download(link)
  return redirect("/" + str(file), code=302)
  #return send_file("downloads/download" + str(file) + ".mp4")
@app.route('/<path:path>')
def now(path):
  return send_file("downloads/download" + path + ".mp4")
if __name__ == "__main__":
    app.run(debug = False, host="0.0.0.0",port=8080)