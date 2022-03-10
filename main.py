from flask import *
from pytube import YouTube
import dld
import random
import sched, time
from threading import Thread
import time
import glob
import os
files = glob.glob('downloads/*.mp4', recursive=True)
def deleteThread(files):
  while True:
    files = glob.glob('downloads/*.mp4', recursive=True)
    for f in files:
      os.remove(f)
    time.sleep(900)
app = Flask(__name__)
def do_something(sc): 
  print("Doing stuff...")
  # do your stuff
  sch.enter(60, 1, do_something, (sc,))
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
    thread = Thread(target = deleteThread, args = (files,))
    thread.start()
    app.run(debug = False, host="0.0.0.0",port=8080)
    thread.join()
    
    