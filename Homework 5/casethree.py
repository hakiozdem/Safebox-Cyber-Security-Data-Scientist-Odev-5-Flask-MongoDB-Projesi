from flask import url_for,redirect,Flask,render_template,request,flash
import pymongo
import time

app = Flask(__name__)
app.secret_key = "secretkeysecretkeysecretkey"
myclient = pymongo.MongoClient("Connection String Here")
db = myclient["flaskmongodb"]
collection = db["Users"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/40")
def query1():
    myquery={"age":{"$gt":40}}            #3. Sorgu
    doc = collection.find(myquery)
    liste = []
    for i in doc:
        liste.append(i)
    
    return render_template('example2.html', liste=liste)

@app.route("/all_users")
def query2():
    all_users = []
    doc = collection.find()
    for i in doc:
        all_users.append(i)
    return render_template("example3.html",all_users = all_users)

@app.route("/add_user",methods =["GET","POST"])
def add():
    if request.method =="GET":
        
        return render_template("add_user.html")
    
    elif request.method=="POST":
        name = request.form.get("namee")
        job = request.form.get("jobb")
        age = request.form.get("agee")
        last_user = collection.find().sort('_id', pymongo.DESCENDING).limit(1)[0]['_id']   
        user = {"_id":last_user+1,"name":name,"job":job,"age":age,"description":"1"}
        flash("Please Enter User informations")
        collection.insert_one(user)
        return redirect(url_for("query2"))
    

@app.route("/delete_user", methods = ["GET","POST"])
def delete():
    if request.method=="GET":
        return render_template("delete_user.html")
    if request.method=="POST":
        id = request.form.get("user_id")
        myquery = {"_id":id}
        collection.delete_one(myquery)
        return redirect(url_for("query2"))
        
if __name__ == "__main__":
    app.run()