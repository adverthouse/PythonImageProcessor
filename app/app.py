from flask import Flask, jsonify
import shutil
app = Flask(__name__)

def createfile():
     shutil.copyfile("/app/temp/66.jpg", "/app/temp/68886.jpg")

@app.route("/")
def home(): 
    return jsonify({ 'name' : 'yunus'}) 

@app.route("/CropFile")
def CropFile():
    createfile()
    return jsonify({ 'name' : 'yunus'})     

if (__name__ == '__main__'):
    app.run(debug=False,port=8000, host="0.0.0.0")